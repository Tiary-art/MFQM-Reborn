#!/usr/bin/env python3
"""Measure Minecraft status-PING/PONG RTT through the same loopback route.
This is not the player's keepalive latency field. Logs no response body/player listing.
"""
import asyncio,struct,time,json,sys

def vint(value):
 result=bytearray()
 while True:
  part=value&127;value>>=7;result.append(part|(128 if value else 0))
  if not value:return bytes(result)
def frame(data):return vint(len(data))+data
async def read_frame(reader):
 length=0
 for index in range(5):
  byte=(await reader.readexactly(1))[0];length|=(byte&127)<<(7*index)
  if not byte&128:break
 else:raise ValueError('varint bound')
 if not 1<=length<=65536:raise ValueError('packet bound')
 return await reader.readexactly(length)
async def ping(port):
 reader,writer=await asyncio.open_connection('127.0.0.1',port)
 try:
  host=b'127.0.0.1'
  writer.write(frame(b'\x00'+vint(763)+vint(len(host))+host+struct.pack('>H',port)+b'\x01')+frame(b'\x00'))
  await writer.drain();await asyncio.wait_for(read_frame(reader),5)
  stamp=time.monotonic_ns();payload=b'\x01'+struct.pack('>q',stamp)
  writer.write(frame(payload));await writer.drain()
  answer=await asyncio.wait_for(read_frame(reader),5);end=time.monotonic_ns()
  if answer!=payload:raise ValueError('PONG mismatch')
  return dict(port=port,point='minecraft_status_ping_pong',nano=stamp,rtt_ms=(end-stamp)/1e6)
 finally:writer.close();await writer.wait_closed()
async def main():
 for port in map(int,sys.argv[1:]):
  for _ in range(3):print(json.dumps(await ping(port)),flush=True)
asyncio.run(main())

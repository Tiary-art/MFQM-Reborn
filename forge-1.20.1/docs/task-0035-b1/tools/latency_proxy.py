#!/usr/bin/env python3
"""Loopback-only TCP delay fixture; opaque bytes, bounded chunks, no payload logging.
Adds a fixed delay on each read chunk in each direction (application proxy, not tc netem).
Head-of-line batching means nominal delay is not proof of measured RTT.
"""
import asyncio,sys,time,json
async def main():
 port=int(sys.argv[1]); delay=float(sys.argv[2])/1000
 if port not in (25566,25567,25568) or not 0<=delay<=0.2: raise ValueError('fixture bounds')
 async def client(reader,writer):
  start=time.monotonic_ns();print(json.dumps(dict(event='connect',port=port,delay_each_way_ms=delay*1000,nano=start)),flush=True)
  remote=None
  try:
   rr,remote=await asyncio.open_connection('127.0.0.1',25565)
   async def pump(src,dst):
    while data:=await src.read(65536):
     await asyncio.sleep(delay);dst.write(data);await dst.drain()
   tasks=[asyncio.create_task(pump(reader,remote)),asyncio.create_task(pump(rr,writer))]
   _,pending=await asyncio.wait(tasks,return_when=asyncio.FIRST_COMPLETED)
   for task in pending:task.cancel()
   await asyncio.gather(*tasks,return_exceptions=True)
  except (ConnectionError,OSError) as ex:print(json.dumps(dict(event='error',type=type(ex).__name__)),flush=True)
  finally:
   writer.close()
   if remote:remote.close()
   print(json.dumps(dict(event='disconnect',port=port,nano=time.monotonic_ns())),flush=True)
 server=await asyncio.start_server(client,'127.0.0.1',port,limit=65536)
 print(json.dumps(dict(event='listen',port=port,delay_each_way_ms=delay*1000)),flush=True)
 async with server:await server.serve_forever()
asyncio.run(main())

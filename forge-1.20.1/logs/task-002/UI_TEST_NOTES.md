# Actual graphical smoke test

- Cloud desktop, software OpenGL llvmpipe 4.5; Java17/Forge47.2.0 development runClient.
- Welcome screen -> Mods -> More Fun Quicksand Reborn 0.0.2-dev / mfqm, metadata screenshot saved.
- Singleplayer -> new Creative/Superflat world, seed4242002, structuresOFF, cheatsON.
- `/give @s mfqm:dev_test_block 4` succeeded. `/tp @s ~ ~ ~ 0 45` aimed at ground.
- Right mouse button placed the block. F3 Targeted Block confirmed mfqm:dev_test_block. Vanilla sand model rendered normally; screenshot saved.
- Save and Quit to Title -> Multiplayer -> Direct Connection -> 127.0.0.1:25565.
- A desktop-control call timed out after300s before entering the address; recovered using fresh desktop screenshots and native key input.
- Both server and client logs confirmed login/modded-server handshake. Creative inventory search `mfqm` showed the development block; screenshot saved.
- Disconnect -> main menu -> Quit Game. runClient finished normally with EXIT_CODE=0.
- No legacy texture resource pack was enabled. No audio test (OpenAL device unavailable). No licensed-account, public-network, two-client, or performance test.

Screenshots are in ../../docs/screenshots (relative to project root use docs/screenshots). They are runtime evidence, not source artwork.

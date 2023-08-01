# thePixelator
script-to-b64-to-pixel obfuscator and de-obfuscator script

What it says on the tin.
Really new to this coding scene and I have been watching a lot of John Hammond on YouTube. Always trying to de-obfuscate some endless procession of b64 strings from hell. Plus, I understand it's been getting a lot harder to sneak anything b64 decode/encode past modern malware protection.

Then I had what seemed like an epiphany. Which, as a concept, probably goes back all the way to the Cold War... at least.

Ladies and gentlemen... without further ado: The Pixelator!

Written and tested on Python 3.11(only... told you I am fresh off the boat...) the Pixelator.py script will turn any script into an image(basically a pixel array...potato, potahto). It will also export the key as a nifty little .csv file on the side.

The UnPixelator.py script will obviously do the exact opposite provided the image file and key .csv file are both in its parent directory, producing a workable script or readable text on the other side. Considering your chosen method of deployment, you might want to declare the key value implicitly into the UnPixelator.py. The world is literally your oyster.

This is a work in progress. I think. Actually, I can't think of anything else I want to do with it now but I might or might not return to spruce this up, later.

After going through all the popular .jpg injection methods out there, I have an idea how to spin this thing to embed code(or text...characters, ok?) onto an actual image, not just a random pixel array, but that implementation is still in the works.

Stay tuned for more!!! Much more!

(I don't know if anyone does it anymore these days and I certainly won't imply I deserve it =P but if you feel like donating some XMR, please do it here: 48WboL6fKdMiPPUHQcyUB5b4jtNAM2FjoPoiKAzWwL1b3Vwe375qNWBRUVpfTWaFC2EGfaGxzbiChPmuAmNzdgeWNMCxMGh)


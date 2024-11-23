# Stalker2Mods
Mod files for Stalker 2 enhancement


# Modding Steps:
Its challanging to find any concrete process of doing this, thus I tossed togather a small primer on how to decrypt, unpack, adn change the .cfg files included with stalker 2 in order to set/adjust any values you desire.
Not so much modding as it is simple value adjustments, but will affect the game nontheless.

# Needed Binaries:
- UnrealPak (version 5.1) - Install unreal Engine and find the binary in (C:\Program Files\Epic Games\UE_5.1\Engine\Binaries\Win64)
  - IF you installed unreal on a different drive letter, obviously change the path above to find your unreal pak binary
- AESDumpster - https://github.com/GHFear/AESDumpster

# Steps:
You will need to extract the encryption Key from the Shipping binary using AESDumpster.
Just drag the binary onto the AESDumpster binary and it will extract the key.
No need to perform DRM removal steps using Steamless etc.. this will work without perform such actions.

# Base64 Encode the key and setup crypto.json
1. Using the included Python script, Input the key and copy the resulting base64 encoded key.
2. Add ther resulting decoded key into the Crypto.json file in the "Key" section. (You will see <YourKeyHere>)

# Unpack Data
1. Run UnrealPak to extract the data
```
.\UnrealPak.exe "<pakfile path>" -Extract "<path to store unpacked data>" -CryptoKeys="<path to your Crypto.json file>"
```
The resulting data should all be unpacked for you to review. 

# RePack the file:
This is pretty simple, name the pak whatever you want, no need to encrypt it. Then in the -Create= flag, pass the file you are packing (after your modifications are done)
```
.\UnrealPak.exe "<namethiswhateveryouwant>.pak" -Create="<fileyouchanged>"
```
This can also be a directory etc.. if you have multiple files. 

# Notes:
Most of all the important data is stored in the pak file `pakchunk0-Windows.pak`. This is obvious since its the largest pak file. 
Feel free to extract others if this is not what you are looking for.


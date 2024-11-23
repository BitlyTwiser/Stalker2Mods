# Stalker2Mods
Mod files and steps for Stalker 2 enhancement

Note: I am not responsible for how you use this. The goal is to build a good community around a great game. Therefore, use responsibly please. 

# Modding Steps:
Its challanging to find any concrete process of doing this, thus I tossed togather a small primer on how to decrypt, unpack, and change the .cfg files included with stalker 2 in order to set/adjust any values you desire.

# Needed Binaries:
- UnrealPak (version 5.1) - Install unreal Engine and find the binary in (C:\Program Files\Epic Games\UE_5.1\Engine\Binaries\Win64)
  - IF you installed unreal on a different drive letter, obviously change the path above to find your unreal pak binary
- AESDumpster - https://github.com/GHFear/AESDumpster

# Steps:
You will need to extract the encryption Key from the Shipping binary using AESDumpster.
Just drag the binary (It will be labeled as -Shipping within your installation directory) onto the AESDumpster binary and it will extract the key.
No need to perform DRM removal steps using Steamless etc.. this will work without perform such actions.

# Base64 Encode the key and setup crypto.json
1. Using the included Python script to get the Base64 encoded key for the crypto file. Input the key you got from AESDumpster into the python script. After running the script, copy the resulting base64 encoded key.
2. Add ther resulting decoded key into the Crypto.json file in the "Key" section. (You will see <YourKeyHere> within the file )

# Unpack Data
1. Run UnrealPak to extract the data
```
.\UnrealPak.exe "<pakfile path>" -Extract "<path to store unpacked data>" -CryptoKeys="<path to your Crypto.json file>"
```
The resulting data should all be unpacked for you to review to the destination folder you provided.

Now you can search for whatever you want and adjust things as desired. When you adjsut them, following the re-pack steps to make the .pak file for your mod.

### Notes:
Most of all the important data is stored in the pak file `pakchunk0-Windows.pak`. This is obvious since its the largest pak file. 
Feel free to extract others if this is not what you are looking for.

# RePack the file:
This is pretty simple, name the pak whatever you want, no need to encrypt it. Then in the -Create= flag, pass the file you are packing (after your modifications are done)

One item to note, I had success with building out a folder structure to store the changed .csf files within:

So make a folder and add the changes files here:
```
Stalker2\Content\GameLite\GameData
```

This is generally the path where you originally changed the files from if you performed the above extraction steps.

Now re-pack and compress the folder
```
.\UnrealPak.exe "<namethiswhateveryouwant>.pak" -Create="<folderpath>" -Compress
```

# Add pack to the ~mods folder:
As the title says, create teh ~mods folder if it does not exist wihtin the dir: `S.T.A.L.K.E.R. 2 Heart of Chornobyl\Stalker2\Content\Paks\~mods`
Insert the newly curated pak files there. 
After restarting the game, hopefully everything works.


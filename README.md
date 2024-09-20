To use: 
Clone the repo 
```
git clone https://github.com/timi2506/iphone-mirroring-eu-activate.git
```
Change the activate Directory to the cloned repo
```
cd iphone-mirroring-eu-activate
```
Install the requirements
```
pip3 install -r requirements.txt
```
If you get an error like this: 
<img width="1006" alt="Screenshot 2024-09-20 at 20 51 42" src="https://github.com/user-attachments/assets/5a7c9ab0-eb49-4c18-aead-d3193a3f33b7">
run:
```
pip3 install -r requirements.txt --break-system-packages
```
instead (dw your system packages will not actually break)

Next, make the script files executeable
```
chmod +x ./*
```
and lastly running the script itself and follow all instructions
```
./run-macOS.command
```
Profit! :D
If you need any help, dm me on twitter x.com/timi2506


# Quick sparserestore exploit script 
### based on [TrollRestore](https://github.com/JJTech0130/TrollRestore)

This fork of the TrollRestore repository makes use of the exploit that installs TrollStore.

Guide for Apple Intelligence: https://gist.github.com/f1shy-dev/23b4a78dc283edd30ae2b2e6429129b5

## Changes from TrollRestore
- Does not install TrollStore
- Skips rebooting (disabled with an `if False:`)

# Credits
* [JJTech](https://github.com/JJTech0130) - Sparserestore (the main library used to restore the TrollHelper binary)
* [Nathan](https://github.com/verygenericname) - Turning sparserestore into a TrollStore installer
* [Mike](https://github.com/TheMasterOfMike), [Dhinak G](https://github.com/dhinakg) - Various improvements to the installer
* [doronz88](https://github.com/doronz88) - pymobiledevice3
* [opa334](https://github.com/opa334), [Alfie](https://github.com/alfiecg24) - TrollStore
* [Aaronp613](https://x.com/aaronp613) - Minor improvements
* [xezrunner](https://x.com/xezrunner) - helping to locate and modify eligibility.plist and changing the script to work with iPhone Mirroring


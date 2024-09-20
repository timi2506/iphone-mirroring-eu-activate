clear
echo Welcome
sleep 0.35
clear 
echo Welcome!
sleep 1
clear
echo "Ready to experience iPhone Mirroring on your EU Devices yet? You'll be guided on how to activate it, just follow the instructions and you should be good to go :D
"
sleep 1
read -n 1 -s -r -p "Press any key to continue..."
clear
echo "Step 1:
Patching eligibility.plist in macOS to make it think you can use iPhone Mirroring, you may have to enter your user account password.

Due to limitations in macOS, you sadly have to do this yourself, just replace /private/var/db/os_eligibility/eligibility.plist with the eligibility plist found in the xezrunner folder, both folders should open when you press a key"
read -n 1 -s -r -p "Press any key to continue..."

open /private/var/db/os_eligibility/
open ./xezrunner/eligibility.plist
read -n 1 -s -r -p "Press any key to continue..."
clear
echo "Done! Now well move over to..."
sleep 3
clear
echo "Step 2:
Patching your iPhones Eligibility.plist file! Please plug it in now to continue and hit Trust this computer when prompted"
read -n 1 -s -r -p "Press any key to continue..."
python3 eligibility.py
echo "Success! Now you have to reboot your Mac (DONT REBOOT YOUR IPHONE), after rebooting try opening iPhone Mirroring, if it doesnt work, go back to Terminal, cd into the Folder the script is in again and run the file called
run-ar-macOS.command"
read -n 1 -s -r -p "Press any key to reboot your Mac..."
sudo reboot

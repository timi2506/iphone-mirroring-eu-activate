clear 
echo Welcome! (again)
sleep 1
clear
echo "Last step to finish this is to clear the iPhone Mirroring Cache of your Mac, once you hit any Key to continue the script should finish that for you, if it fails or iPhone Mirroring still doesn't work i recommend using the free Application App Cleaner (https://freemacsoft.net/downloads/AppCleaner_3.6.8.zip) to clean the rest of iPhone Mirroring Application on macOS
"
sleep 1
read -n 1 -s -r -p "Press any key to continue..."
echo "Clearing iPhone Mirrorings Cache..."
rm -rf ~/Library/Containers/com.apple.ScreenContinuity
rm -rf ~/Library/Application\ Scripts/com.apple.ScreenContinuity
sleep 1
echo "
Done!"
read -n 1 -s -r -p "Press any key to open iPhone Mirroring..."
echo "Quick Tip before you open iPhone Mirroring: I recommend running the run-macOS.command script every time you reboot iPhone as the file could get overwritten on reboot"
read -n 1 -s -r -p "Press any key to continue opening iPhone Mirroring..."
open /System/Applications/iPhone\ Mirroring.app

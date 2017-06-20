# roku-steam-controller
Control your roku tv (or any roku device) from your steam controller.

## Setup
Figure out your roku device's ip address and enter it in settings.py.
Install dependencies by running `pip install -r requirements.txt`.
This should be done from within a virtualenv.
Modify the `hotkeys.ahk` file to point to the correct python installation on your machine, and modify `WorkingDir` to point to to directory of the `main.py` file.
Install [autohotkey](https://autohotkey.com/) and load the `hotkeys.ahk` script.Feel free to set the hotkeys to whatever you want. You then have to set up your steam controller to activate those keys for certain button presses. I configured the desktop layout to use the left grip as a mode switch for the joystick to control the arrow keys, and for the left trackpad to control the volume.

## Todo

* Create some kind of setup script that does this all automatically.
* Export my steam controller config and either add it to the repo or add a link to it so others can use it.
* Figure out how windows users usually have python installed.
* Figure out how pip normally is used from windows.
* Make these instructions more clear for those that have never written a line of code.

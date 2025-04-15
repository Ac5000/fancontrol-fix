# fancontrol-fix

Quick and dirty fix for fancontrol when hwmon path changes on boot.

## How it Works

The `update_fancontrol.py` script reads through HWMON paths looking for a `name`
file. When it finds `name` it opens and checks if the `DEVICE_NAME` is inside.

If `DEVICE_NAME` is inside the file, it will open `/etc/fancontrol` and find/replace
all instances of `hwmon\#` with the folder it found the matching `DEVICE_NAME`.

## How to Modify

For my specific case, I am using fancontrol to control my Aquacomputer Quadro.
I found the Quadro to have the name `quadro` inside of the `name` file.

For your use case, figure out what file(s) you can use to isolate the `hwmon#`
folder and add them to the initial loop.

## CAUTION / WARNING / DON'T CONTINUE WITHOUT UNDERSTANDING

I will repeat what is listed on the [Arch Wiki Fan speed control page](https://wiki.archlinux.org/title/Fan_speed_control)

> Doing this may make fancontrol write into files you gave it in the configuration
file, no matter what the file is. This can corrupt files if you provide the wrong
path. Be sure that you are using the correct path for your files.

So if you don't feel comfortable with how this works, don't risk it without testing!

> Another thing to note is that while doing this workaround, using pwmconfig to
create your script again will overwrite all of your absolute paths that you have
configured. Therefore, it is better to manually change the old paths to the new
paths if it is needed instead of using pwmconfig.

## How to Use

Put `update_fancontrol.py` in `/usr/bin/update_fancontrol.py`

Put `update_fancontrol.service` in `/etc/systemd/system/update_fancontrol.service`

Run `sudo systemctl enable --now update_fancontrol`

## Thank You

Thank you to [lukolszewski](https://github.com/lukolszewski) for the idea and code
from the fancontrol issues page.

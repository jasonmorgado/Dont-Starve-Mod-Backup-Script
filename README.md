# Dont Starve Mod Backup Script
 
This is a tool made to help modders look through mods downloaded from the steam workshop, for easier reference. 

Because mods from the workshop name their folders "workshop-#########", it can be difficult to see which mod is in each folder. This script copies these workshop mods to a new folder, using the mod's names as the names of the folders instead.

![screenshot](https://i.imgur.com/GVkl01g.png)

## Usage

Primarily, you can use this script via the command line with the following parameters:

`python backup_mods.py <mods_path> <destination_path>`

Where <mods_path> is the path to the game's mods folder, and <destination_path> is the path to the folder where the backups will be stored. 

For example:

`python backup_mods.py "C:\Program Files (x86)\Steam\steamapps\common\Don't Starve Together\mods" "C:\Users\UserName\Documents\DST_mod_backups"`

Alternatively one could open up the python file, change the paths defined in the top of the file, and run the file by itself. 

## Notes
- This copies mods to a new folder, it doesn't rename the original folders in mods folder. This is because simply renaming mod folders would likely cause the workshop to redownload copies of the mods.
- It does not update the copies if the mods get updates from the workshop. It only checks to see if the backup folders exist before copying them over.

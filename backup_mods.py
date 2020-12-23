import os
import shutil
import sys
import time

# Set these manually if not using command line
MODS_FOLDER_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Don't Starve Together\\mods"
MODS_BACKUP_LOCATION = "C:\\Users\\UserName\\Documents\\DST_mod_backups"

def move_folder(src_path, backup_path, mod_name):
    """
    Takes the location of a mod folder,
    Location of backup folder,
    and 
    Copies folder to MODS_BACKUP_LOCATION as a result,
    but with mod_name as the folder name instead.
    Will not copy if already exists there.
    """
    illegal_characters = "\"\\/:|<>*?"
    for character in illegal_characters:
        mod_name = mod_name.replace(character,'')
    mod_name = mod_name.strip(' \'')

    dst_path = backup_path + "\\{}".format(mod_name)
    if os.path.exists(dst_path):
        print("Path for {} already exists, skipping...".format(mod_name))
        return None
    new_path = shutil.copytree(src_path, dst_path)
    print("Created backup at:", new_path)


def backup_mods(mods_folder_path, backup_path):
    """Iterates through workshop mods, fetches name, copies folder"""

    # Verify paths
    mod_folder_exists = os.path.exists(mods_folder_path)
    backup_folder_exists = os.path.exists(backup_path)

    if not mod_folder_exists:
        print("Mods folder Path: {} does not exist. Change it in the python file."\
            .format(backup_path))
        return None
    if not backup_folder_exists:
        print("Backup Path: {} does not exist.".format(backup_path))
        print("Change it in the python file, or create it if that's where you want backups")
        return None

    # Get a list of workshop mods from mods folder
    mod_folder_list = os.listdir(mods_folder_path)
    workshop_folders = []
    for folder_name in mod_folder_list:
        if "workshop" in folder_name:
            workshop_folders.append(folder_name)

    # Get name and copy to backups folder
    for folder_name in workshop_folders:
        mod_path = mods_folder_path + "\\" +folder_name 
        modinfo_path = mod_path + "\\modinfo.lua"

        # Get mod name
        mod_name = ""
        workshop_id = folder_name.split("-")[1]
        try:
            with open(modinfo_path, 'r', encoding='utf-8') as modinfo_file:
                for line in modinfo_file:
                    if line[:4] == "name":
                        mod_name = line.split('=')[1].strip(" \n")
                        break
        except UnicodeDecodeError:
            print("Unexpected encoding, trying another way...")
            with open(modinfo_path, 'r', encoding='latin-1') as modinfo_file:
                for line in modinfo_file:
                    if line[:4] == "name":
                        mod_name = line.split('=')[1].strip(" \n")
                        break
        # Copy to dest
        move_folder(mod_path, backup_path, mod_name)
    print("Done!")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("No command line args, using default paths in file...")
        backup_mods(MODS_FOLDER_PATH, MODS_BACKUP_LOCATION)
    elif len(sys.argv) == 3:
        backup_mods(sys.argv[1], sys.argv[2])
    else:
        print("Got {} command line arguments, expected 2.".format(len(sys.argv)-1))
    time.sleep(10)
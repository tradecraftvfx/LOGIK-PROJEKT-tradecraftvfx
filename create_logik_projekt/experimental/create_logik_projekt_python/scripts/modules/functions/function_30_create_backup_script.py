#!/usr/bin/env python3

"""
File Name:        function_30-create_backup_script.py
Version:          2.1.5
Language:         Python 3
Flame Version:    2025.x
Author:           Phil MAN - phil_man@mac.com
Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
Modified:         2024-05-18
Modifier:         Phil MAN - phil_man@mac.com

Description:      This program contains function(s) that are used to
                  create new logik projekts.

Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
                  e.g. '/home/$USER/workspace/GitHub'

Changelist:       The full changelist is at the end of this document.
"""

import os
import shutil
import datetime

# Function to create backup script
def create_backup_script():
    """
    Create backup script.

    Copies the default job backup text to a new backup shell script.
    Copies the default exclusion list to the backup directory.
    Adds execution permissions to the new backup shell script.
    Replaces placeholders in the backup script with actual values.
    """
    src_rsync_script = "presets/templates/backup_template"
    tgt_rsync_script = os.path.join(tgt_rsync_dir, "backup_" + name + ".sh")
    
    # Copy the default job backup text to a new backup shell script
    shutil.copy(src_rsync_script, tgt_rsync_script)

    src_rsync_exclusion_list = "presets/templates/exclusion_list.txt"
    tgt_rsync_exclusion_list = os.path.join(tgt_rsync_dir, "exclusion_list.txt")
    
    # Copy the default exclusion list to the backup directory
    shutil.copy(src_rsync_exclusion_list, tgt_rsync_exclusion_list)

    # Add execution permissions to new backup shell script
    os.chmod(tgt_rsync_script, 0o755)

    # Set the search and replace strings
    search_replace = [
        ("BackupScriptName", "backup_" + name + ".sh"),
        ("BackupScriptProjekt", nickname),
        ("ScriptCreationDate", str(datetime.datetime.now())),
        ("LogikProjektClient", client),
        ("LogikProjektCampaign", campaign),
        ("LogikProjektName", nickname),
        ("FlameSoftwareVersion", max_sanitized_sw_ver),
        ("FlameWorkstationName", workstation_name)
    ]

    # Use sed to replace the strings in the backup script
    sed_command = "sed -i" if operating_system == "Linux" else "sed -i ''" if operating_system == "macOS" else None
    if sed_command is None:
        print("Unsupported operating system.")
        return 1

    for search, replace in search_replace:
        os.system(f"{sed_command} 's|{search}|{replace}|g' {tgt_rsync_script}")

    print("  logik projekt backup script created:\n")
    print(f"  {os.path.basename(tgt_rsync_script)}")
    print(f"\n{separator}\n")

# Check if the script is being sourced or executed
if __name__ == "__main__":
    create_backup_script()
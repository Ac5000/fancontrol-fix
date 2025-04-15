"""Update fancontrol when device name changes."""

import os
import re

TARGET_FILE = "name"
DEVICE_NAME = "quadro"
HWMON_PATH = "/sys/class/hwmon/"
found_folder = None

for folder in os.listdir(HWMON_PATH):
    if not re.match(r"hwmon\d+", folder):
        continue
    folder_path = os.path.join(HWMON_PATH, folder)
    # print(f"{folder_path=}")
    if TARGET_FILE not in os.listdir(folder_path):
        continue
    file_to_open = os.path.join(folder_path, TARGET_FILE)
    # print(f"{file_to_open=}")
    with open(file_to_open, "r", encoding="utf-8") as file:
        if file.read().strip() == DEVICE_NAME:
            print(f"FOUND {DEVICE_NAME=} in {folder=}")
            found_folder = folder
            break

# If we found the folder with our DEVICE_NAME, open fancontrol and replace.
if found_folder:
    with open("/etc/fancontrol", "r", encoding="utf-8") as file:
        fancontrol_content = file.read()

    updated_content = re.sub(r"hwmon\d+", found_folder, fancontrol_content)

    # Print the updated content instead of saving for testing
    # print(updated_content)  # uncomment for testing

    # Comment out for testing
    with open("/etc/fancontrol", "w", encoding="utf-8") as file:
        file.write(updated_content)
else:
    print("Target file/device not found in any hwmon folder.")

import os
import sys
import yaml
import re

# =============================
# Constants
# =============================
# Argument Index
ARG_INDEX_DIR_PATH = 1
ARG_INDEX_FILE_NAME = 2
ARG_INDEX_SORT_TYPE = 3

# Information Json File PAth
INFO_YAML_FILE_PATH = os.path.join(os.path.dirname(__file__), "parameters.yml")
YAML_KEY_DIR_PATH  = "dirPath"
YAML_KEY_FILE_NAME  = "fileName"
YAML_KEY_SORT_TYPE  = "sortType"

# Sort type
SORT_TYPE_CTIME = "ctime"
SORT_TYPE_NAME = "name"

# =============================
# Methods
# =============================
def checkParams(dirPath, fileName, sortType):
    log = ""
    if dirPath == "":
        log = "dirPath is empty"
    if not os.path.exists(dirPath):
        log = f"directory is not found ! -> {dirPath}"
    if fileName == "":
        log = "fileName is empty"
    if re.search(r'[\\|/|:|?|.|"|<|>|\|]', fileName):
        log = "fileName is invalid(fileName contains characters that cannot be used.)"
    if sortType == "":
        log = "sortType is empty"
    if sortType != "" and (sortType != SORT_TYPE_CTIME and sortType != SORT_TYPE_NAME):
        log = "sortType is invalid value"

    return log

def rename(dirPath, fileName, sortType):
    # find target files (ignore directory)
    files = os.listdir(dirPath)
    files = [f for f in files if os.path.isfile(os.path.join(dirPath, f))]

    if sortType == SORT_TYPE_CTIME:
        files = sorted(files, key=lambda f: os.stat(os.path.join(dirPath, f)).st_ctime, reverse=False)
    elif sortType == SORT_TYPE_NAME:
        files = sorted(files, key=lambda f: f, reverse=False)
    else:
        print(f"Invalid sortType -> {sortType}")
    
    # rename files
    for index, file in enumerate(files):
        filePath = os.path.join(dirPath, file)
        extension = file.split(".")[-1]

        newFileName = f"{fileName}{index}.{extension}"
        newFilePath = os.path.join(dirPath, newFileName)

        os.rename(filePath, newFilePath)

def main():
    print("Start !!!")
    print("...")
    print("loading information variables")
    print("...")

    # information variables
    dirPath = ""
    fileName = ""
    sortType = ""

    # set information
    args = sys.argv
    if len(args) == 4:
        dirPath = args[ARG_INDEX_DIR_PATH]
        fileName = args[ARG_INDEX_FILE_NAME]
        sortType = args[ARG_INDEX_SORT_TYPE]
    else:
        with open(INFO_YAML_FILE_PATH) as yamlFile:
            yamlText = yaml.safe_load(yamlFile)
            dirPath = yamlText[YAML_KEY_DIR_PATH]
            fileName = yamlText[YAML_KEY_FILE_NAME]
            sortType = yamlText[YAML_KEY_SORT_TYPE]

    print("checking variables")
    print("...")

    # check parameters
    log = checkParams(dirPath, fileName, sortType)
    if log != "":
        print(f"Rename failure !!!\n{log}")
        return

    print("renaming")
    print("...")

    # rename
    rename(dirPath, fileName, sortType)

    print("Completed !!!")


# =========================
# main
# =========================
main()
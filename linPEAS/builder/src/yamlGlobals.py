import os
import yaml

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
LINPEAS_BASE_PATH = CURRENT_DIR + "/../linpeas_base.sh"
FINAL_LINPEAS_PATH = CURRENT_DIR + "/../../" + "linpeas.sh"
YAML_NAME = "sensitive_files.yaml"
FILES_YAML = CURRENT_DIR + "/../../../build_lists/" + YAML_NAME

with open(FILES_YAML, 'r') as file:
    YAML_LOADED = yaml.load(file, Loader=yaml.FullLoader)

ROOT_FOLDER = YAML_LOADED["root_folders"]
DEFAULTS = YAML_LOADED["defaults"]
COMMON_FILE_FOLDERS = YAML_LOADED["common_file_folders"]
COMMON_DIR_FOLDERS = YAML_LOADED["common_directory_folders"]
assert all(f in ROOT_FOLDER for f in COMMON_FILE_FOLDERS)
assert all(f in ROOT_FOLDER for f in COMMON_DIR_FOLDERS)


PEAS_FINDS_MARKUP = YAML_LOADED["peas_finds_markup"]
FIND_LINE_MARKUP = YAML_LOADED["find_line_markup"]
FIND_TEMPLATE = YAML_LOADED["find_template"]

PEAS_STORAGES_MARKUP = YAML_LOADED["peas_storages_markup"]
STORAGE_LINE_MARKUP = YAML_LOADED["storage_line_markup"]
STORAGE_LINE_EXTRA_MARKUP = YAML_LOADED["storage_line_extra_markup"]
STORAGE_TEMPLATE = YAML_LOADED["storage_template"]

INT_HIDDEN_FILES_MARKUP = YAML_LOADED["int_hidden_files_markup"]
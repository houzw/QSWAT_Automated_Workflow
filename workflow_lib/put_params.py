"""
This Module inserts parameters from a model.in file into the model
"""
import cj_function_lib as cj
import mdbtools as mdb
import settings, zipfile, os
from init_file import root, DefaultSimDir

if settings.cal_file.strip(" ") != "":
    print("Applying user parameters...")
    back_up_files = cj.list_files_from("{0}TxtInOut/".format(DefaultSimDir), "")
    cj.copy_file("{0}Data/{1}".format(root, settings.cal_file), "{0}TxtInOut".format(DefaultSimDir))

    with zipfile.ZipFile(root + "/workflow_lib/cal_holders.zip","r") as zip_ref:
        zip_ref.extractall("{0}TxtInOut/".format(DefaultSimDir))
    if not os.path.isdir("{0}TxtInOut/Backup".format(DefaultSimDir)):
        os.makedirs("{0}TxtInOut/Backup".format(DefaultSimDir))
    else:
        list_old_bu = cj.list_files_from("{0}TxtInOut/Backup/".format(DefaultSimDir), "")
        for old_file in list_old_bu:
            os.remove(old_file)
    for file_ in back_up_files:
        cj.copy_file(file_, "{0}TxtInOut/Backup".format(DefaultSimDir))
    os.chdir("{0}TxtInOut/".format(DefaultSimDir))
    os.system("Swat_Edit.exe")


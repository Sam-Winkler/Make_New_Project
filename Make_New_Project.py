import os, tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

new_project = simpledialog.askstring(title=" ", prompt="New Project Name:")
new_project = new_project.replace(" ", "_")
new_project = new_project.upper()

path = os.path.dirname(__file__)
prj_dir = path + "\\" + new_project
os.mkdir(prj_dir)

main_directories = [
    "01_REFERENCE",
    "02_FOOTAGE",
    "03_ELEMENTS",
    "04_PROJECTS",
    "05_OUTPUT",
]

sub_directories = [
    ["01_INTERNAL", "02_FROM_CLIENT", "03_TO_CLIENT"],
    ["01_PLATES", "02_PRERENDERS"],
    [
        "01_STILLS",
        "02_PSD",
        "03_VECTOR",
        "04_MODEL",
        "05_VIDEO",
        "06_SOUND",
        "07_FONTS",
        "02_PRESETS",
    ],
    ["01_COMP", "02_3D", "03_TRACK", "04_EDIT"],
    ["01_REVIEW", "02_POSTING", "03_DELIVERY"],
]

for x in range(len(sub_directories)):
    os.mkdir(os.path.join(prj_dir, main_directories[x]))
    for y in range(len(sub_directories[x])):
        os.mkdir(os.path.join(prj_dir, main_directories[x], sub_directories[x][y]))

for z in range(len(sub_directories[4])):
    file_dir = prj_dir + "\\05_OUTPUT\\" + sub_directories[4][z]
    file_name = file_dir + "\\" + "Make_Date_Folder.py"

    f = open(file_name, "a")
    f.write(
        "import os \n"
        + "from datetime import date \n"
        + "today = date.today() \n"
        + 'datetime = today.strftime("%m/%d/%y") \n'
        + 'datetime = datetime.replace("/","") \n'
        + 'os.mkdir(os.path.dirname(__file__) + "\\\\" + datetime)'
    )
    f.close()

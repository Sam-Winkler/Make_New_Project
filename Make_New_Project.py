import os, tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

newProject = simpledialog.askstring(title=" ", prompt="New Project Name:")
newProject = newProject.replace(" ", "_")
newProject = newProject.upper()

path = os.path.dirname(__file__)
prjDir = path + "\\" + newProject
os.mkdir(prjDir)

mainDirectories = [
    "01_REFERENCE",
    "02_FOOTAGE",
    "03_ELEMENTS",
    "04_PROJECTS",
    "05_OUTPUT",
]

subDirectories = [
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

for x in range(len(subDirectories)):
    os.mkdir(os.path.join(prjDir, mainDirectories[x]))
    for y in range(len(subDirectories[x])):
        os.mkdir(os.path.join(prjDir, mainDirectories[x], subDirectories[x][y]))

for z in range(len(subDirectories[4])):
    fileDir = prjDir + "\\05_OUTPUT\\" + subDirectories[4][z]
    fileName = fileDir + "\\" + "Make_Date_Folder.py"

    f = open(fileName, "a")
    f.write(
        "import os \n"
        + "from datetime import date \n"
        + "today = date.today() \n"
        + 'datetime = today.strftime("%m/%d/%y") \n'
        + 'datetime = datetime.replace("/","") \n'
        + 'os.mkdir(os.path.dirname(__file__) + "\\\\" + datetime)'
    )
    f.close()

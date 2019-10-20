import cx_Freeze
import sys
import tkinter
import jinja2
import PIL

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Main.py", base=base, icon="favicon.ico", targetName="Forms")]

cx_Freeze.setup(
    name="Forms",
    options={
        "build_exe" : {
            "packages" : ["tkinter", "jinja2", "PIL", "Forms"],
            "include_files" : [
                "Dakhila.py",
                "Trial.py",
                "Naamsaari.py",
                "Form4.py",
                "FormUtils.py",
                "favicon.ico",
                "./Forms"
            ] 
        }
    },
    version="0.0.1",
    description="A GUI utility to facilitate filling of government forms",
    executables=executables
)
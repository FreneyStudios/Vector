import sys
import gc
import importlib
import json


SPEED : int
MXSPEED : int
SPEEDWLEV : int
RAISE : bool
GC : bool


#<----DEFS---------------->#
def SysSpeed()->int:
    try:
        sys.setrecursionlimit(2000)
        return 0;
    except Exception as e:
        return 1;

def SysExit(motive):
    sys.exit(motive)

def SysExitSuccess():
    sys.exit(0)

def CSysExit(condition:bool,motive:str):
    if condition:
        sys.exit(motive)

def GetSettings()->str:
    file_path = 'settings.json'

    #    Step 1: Open the file and load it into a Python dictionary
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Step 2: Convert the dictionary back to a string
    json_string = json.dumps(data, indent=4)

    # Step 3: Print or use the string
    print(json_string)
    
def Modular(modulename: str, modulepack: str):
    # Check if the module is already imported
    module = sys.modules.get(modulename)
    if not module:
        try:
            # Dynamically import the module using its name
            module = importlib.import_module(modulepack)
            sys.modules[modulename] = module
        except ImportError as e:
            print(f"Error importing {modulepack}: {e}")
    return module

def EnableGC():
    gc.enable()
    GC = True

def DisableGC():
    gc.disable()
    GC = False

def ManageGC():
    if GC:
        gc.disable()
    else:
        gc.enable()

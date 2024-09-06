import sys
import gc
import importlib



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

def CSysExit(condition:bool,motive:str):
    if condition:
        sys.exit(motive)
    
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

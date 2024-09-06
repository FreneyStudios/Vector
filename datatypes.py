import sys



VC_BOOL : int
VC_INPUT = sys.stdin.read()

def VC_PRINT(char:str):
    try:
        sys.stdout.write(char+"\n")
    except ValueError:
        sys.stdout.write(str(char)+"\n")
    except Exception as e:
        pass

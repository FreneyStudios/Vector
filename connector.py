import ctypes

# Load the DLL
'''IMPORTANT NOTE: edit if this gives error
<+-------------------------------------------+>'''
info = ctypes.CDLL(".\\Vector\\info.dll") 

# Define function prototypes
info.set_VEC_DATA_BUS.argtypes = [ctypes.c_int]
info.set_VEC_DATA_BUS.restype = None

info.get_VEC_DATA_BUS.restype = ctypes.c_int

info.set_GEN_COUNTER.argtypes = [ctypes.c_int]
info.set_GEN_COUNTER.restype = None

info.get_GEN_COUNTER.restype = ctypes.c_int

info.set_MAGIC.argtypes = [ctypes.c_int]
info.set_MAGIC.restype = None

info.get_MAGIC.restype = ctypes.c_int

info.set_VEC_DATA_BUS2.argtypes = [ctypes.c_int]
info.set_VEC_DATA_BUS2.restype = None

info.get_VEC_DATA_BUS2.restype = ctypes.c_int

info.set_VEC_LOGCAT.argtypes = [ctypes.c_int]
info.set_VEC_LOGCAT.restype = None

info.get_VEC_LOGCAT.restype = ctypes.c_int

info.set_VEC_DESC.argtypes = [ctypes.c_char_p]
info.set_VEC_DESC.restype = None

info.get_VEC_DESC.restype = ctypes.c_char_p

# Use the functions
info.set_VEC_DATA_BUS(0)
info.set_GEN_COUNTER(0)
info.set_MAGIC(212)
info.set_VEC_DATA_BUS2(1)
info.set_VEC_LOGCAT(0)
info.set_VEC_DESC(b"New Description")

print(info.get_VEC_DATA_BUS())
print(info.get_GEN_COUNTER())
print(info.get_MAGIC())
print(info.get_VEC_DATA_BUS2())
print(info.get_VEC_LOGCAT())
print(info.get_VEC_DESC().decode())

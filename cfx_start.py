# Sanitize user-level identity providers before running Cfx.re applications.

import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        
def uac_elevation():
	if not is_admin():
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
		return False
	return True

def nuke_file(file):
	if os.path.isfile(file):
		os.path.remove(file)

# Require admin rights.
if not uac_elevation():
	return

# NVIDIA GPUID
# NVIDIA Management Library + Interface
nuke_file("C:\\Windows\\System32\\nvml.dll")
nuke_file("C:\\Windows\\System32\\nvidia-smi.exe")
nuke_file("C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvml.dll")
nuke_file("C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.dll")

os.startfile(os.environ["CFX_PATH"])

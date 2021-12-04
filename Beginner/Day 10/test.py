import os
import sys

print("Hello")
tak=input("")
if tak=="w":
    os.execl(sys.executable,sys.executable, *sys.argv)
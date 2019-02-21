# Tool Name :- MyServer
# Author :- csdevro
# Date :- 22/5/2018
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from ux import *
from logo import *

if sys.argv[1]=="-s":
  if os.path.exists(spath+".serv.lock"):
    s=open(spath+".serv.lock","r")
    sr=s.read()
    s.close()
    if system=="ubuntu":
      os.system("sudo python2 core/server.py "+sr)
    else:
      os.system("python2 core/server.py "+sr)
  else:
    pass
elif sys.argv[1]=="-h":
  if os.path.exists(spath+".h.lock"):
    s=open(spath+".h.lock","r")
    sr=s.read()
    s.close()
    if system=="ubuntu":
      os.system("sudo python2 core/host.py "+sr)
    else:
      os.system("python2 core/host.py "+sr)
  else:
    pass

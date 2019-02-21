# Tool Name :- MyServer
# Author :- csdevro
# Date :- 23/5/2018
# Powered By :- Aex Software's

import sys
import os

if os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
  pac="pkg"
  home=os.getenv("HOME")+"/"
  bpath="/data/data/com.termux/files/usr/bin/"
  spath="/data/data/com.termux/files/usr/share/"
  system="termux"
elif os.path.exists("/usr/bin/apt") or os.path.exists("/usr/bin/apt-get") or os.path.exists("/bin/apt") or os.path.exists("/bin/apt"):
  if os.path.exists("/usr/lib/sudo") or os.path.exists("/usr/bin/sudo") or os.path.exists("/usr/sbin/sudo"):
      home=os.getenv("HOME")+"/"
      pac="sudo apt-get"
      bpath="/usr/bin/"
      spath="/usr/share/"
      system="ubuntu"
  else:
      home=os.getenv("HOME")+"/"
      pac="apt-get"
      bpath="/usr/bin/"
      spath="/usr/share/"
      system="debian"
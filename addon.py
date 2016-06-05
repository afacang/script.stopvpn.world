import xbmcaddon
import xbmcgui
import subprocess
import os
import re
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hello"
line2 = "VPN service stopped"
line3 = "VPN service was not running"
PROCNAME = "openvpn"

def is_running(process):
  s = subprocess.Popen(["ps","axw"],stdout=subprocess.PIPE)
  for x in s.stdout:
    if re.search(process, x):
      return True
  return False

if is_running(PROCNAME):
 p = subprocess.Popen("sudo kill -9 $(sudo ps aux| pgrep '(" + PROCNAME + ")')", shell=True, stdout=subprocess.PIPE)
 xbmcgui.Dialog().ok(addonname, line1, line2 )
else:
 xbmcgui.Dialog().ok(addonname, line1, line3)


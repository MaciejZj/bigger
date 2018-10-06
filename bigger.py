#!/usr/bin/python
import sys
from AppKit import NSScreen
from ScriptingBridge import SBApplication
from math import fabs

terminal=SBApplication.applicationWithBundleIdentifier_("com.apple.Terminal")
t_window=terminal.windows()[0]
toPrint=""

# finds current screen and sets its frame to pFrame
pFrame = None		
for screen in NSScreen.screens():
	if ((t_window.position().x > screen.frame().origin.x) and 
		(t_window.position().x < screen.frame().origin.x + screen.frame().size.width)):
		
		pFrame = screen.frame()
		break	

# get window properties
s_x=t_window.size().x
s_y=t_window.size().y

p_x=t_window.position().x
p_y=t_window.position().y

# get screen properties
screen_height = pFrame.size.height
screen_width = pFrame.size.width

screen_origin_x = pFrame.origin.x
screen_origin_y = pFrame.origin.y

# resizes screen
# medium
if sys.argv[1]=="m":
	factor=1.6
	new_x=p_x+(s_x-570*factor)/2
	new_y=p_y+(s_y-390*factor)/2
	s_x=570*factor
	s_y=390*factor
	toPrint="Medium size: {} by {}. ".format(s_x,s_y)
# big
elif sys.argv[1]=="b":
	factor=2

	s_x=570*factor
	s_y=390*factor
	new_x=(screen_width-s_x)/2
	new_y=(screen_height-s_y)/2-15
	toPrint="Large size: {} by {}. ".format(s_x,s_y)
#default (small)
elif sys.argv[1]=="s":
	new_x=p_x+(s_x-570)/2
	new_y=p_y+(s_y-390)/2
	s_x=570
	s_y=390
	toPrint="Small size (default): {} by {}. ".format(s_x,s_y)

# centers screen for c and b options
if (sys.argv[1]=="c" or sys.argv[1]=="b"):	
	new_x=screen_origin_x+screen_width/2-s_x/2
	new_y=+screen_height/2-s_y/2-15
	
	toPrint=toPrint + "Window centered"

t_window.setBounds_([[new_x, new_y], [s_x, s_y]])
print(toPrint)
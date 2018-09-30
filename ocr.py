from PIL import Image
import pytesseract
import os
import gtk.gdk
import webbrowser
import re
import numpy as np
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance
import requests
import pyscreenshot as ImageGrab

# AppCode
# MobShow 1
# Loco 2
# BrainBazi 3
# Cheez 4
# Stupid 5
# Qureka 6
# JustPlay 7
# NewsDog 8
# HQ 9
# IQ 10


appCode = 2

#w = gtk.gdk.get_default_root_window()
#sz = w.get_size()

#pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, sz[0], sz[1])
#pb = pb.get_from_drawable(w, w.get_colormap(), 60, 120, 0, 0, sz[0] / 4 + 20, sz[1] - 50)
#pb.save("example.jpeg", "jpeg")

filename = "example.jpeg"
image = cv2.imread(filename)
question = ""
option1 = ""
option2 = ""
option3 = ""

# image = cv2.imread(filename)
if appCode == 1:
    s = 280
    opw = 60
    qw = 120
    ques = image[s:s + qw, 0:sz[0] / 4 + 40]
    opt1 = image[s + qw:s + opw + qw, 40:sz[0] / 4 + 40]
    opt2 = image[s + qw + opw:s + qw + 2 * opw, 40:sz[0] / 4 + 40]
    opt3 = image[s + qw + 2 * opw:s + qw + 3 * opw, 40:sz[0] / 4 + 40]

if appCode == 2:
    s = 300
    opw = 67
    qw = 90
    # ques = image[s:s+qw, 0:sz[0]/4+40]
    ques = ImageGrab.grab(bbox=(80, s, 420, s + qw))
    sharper = ImageEnhance.Sharpness(ques)
    ques = sharper.enhance(9)
    brighter = ImageEnhance.Brightness(ques)
    ques = brighter.enhance(1)
    ques = ques.convert("L")
    #ques.show()
    # opt1 = image[s+qw:s+opw+qw, 30:sz[0]/4+40]
    opt1 = ImageGrab.grab(bbox=(80, s + qw, 420, s + qw + opw))
    opt1.show()
    # opt2 = image[s+qw+opw:s+qw+2*opw, 30:sz[0]/4+40]
    # opt2 = ImageGrab.grab(bbox=(60,s+qw+opw, 350,s+qw+2*opw))
    # opt3 = image[s+qw+2*opw:s+qw+3*opw, 30:sz[0]/4+40]
    # opt3= ImageGrab.grab(bbox=(60,s+qw+2*opw, 350,s+qw+3*opw))

if appCode == 3:
    s = 100
    opw = 55
    qw = 100
    ques = image[s:s + qw, 0:sz[0] / 4 + 40]
    opt1 = image[s + qw:s + opw + qw, 30:sz[0] / 4 + 40]
    opt2 = image[s + qw + opw:s + qw + 2 * opw, 30:sz[0] / 4 + 40]
    opt3 = image[s + qw + 2 * opw:s + qw + 3 * opw, 30:sz[0] / 4 + 40]

if appCode == 4:
    s = 70
    opw = 45
    qw = 95
    ques = image[s:s + qw, 0:sz[0] / 4 + 40]
    opt1 = image[s + qw:s + opw + qw, 30:sz[0] / 4 + 40]
    opt2 = image[s + qw + opw:s + qw + 2 * opw, 30:sz[0] / 4 + 40]
    opt3 = image[s + qw + 2 * opw:s + qw + 3 * opw, 30:sz[0] / 4 + 40]

if appCode == 5:
    s = 180
    opw = 80
    qw = 102
    ques = image[s:s + qw, 0:sz[0] / 4 + 40]
    opt1 = image[s + qw:s + opw + qw, 40:sz[0] / 4 + 40]
    opt2 = image[s + qw + opw:s + qw + 2 * opw, 40:sz[0] / 4 + 40]
    opt3 = image[s + qw + 2 * opw:s + qw + 3 * opw, 40:sz[0] / 4 + 40]

if appCode == 6:
    s = 210
    opw = 80
    qw = 105
    ques = image[s:s + qw, 0:sz[0] / 4 + 40]
    opt1 = image[s + qw:s + opw + qw, 30:sz[0] / 4 + 40]
    opt2 = image[s + qw + opw:s + qw + 2 * opw, 30:sz[0] / 4 + 40]
    opt3 = image[s + qw + 2 * opw:s + qw + 3 * opw, 30:sz[0] / 4 + 40]

# sharper = ImageEnhance.Sharpness(ques)
# ques = sharper.enhance(9)
# brighter = ImageEnhance.Brightness(ques)
# ques = brighter.enhance(1)
# ques = ques.convert("L")


# ques.show()
# opt1.show()
# opt2.show()
# opt3.show()
# question = pytesseract.image_to_string(ques,lang='eng')
# option1 = pytesseract.image_to_string(opt1,lang='eng')
# option2 = pytesseract.image_to_string(opt2,lang='eng')
# option3 = pytesseract.image_to_string(opt3,lang='eng')

# text = pytesseract.image_to_string(image,lang='eng')
# idx = 0
# flag = True
# for char in text:
#    if char=='?':
#       question += char
#       flag = False
#       continue
#    if char=='\n':
#       question += ' '
#       if flag == False :
#          idx += 1
#          continue
#    if flag == True :
#       question += char
#    else :
#       if idx == 0:
#          option1 += char
#       elif idx == 1:
#          option2 += char
#       else :
#          option3 += char

question = question.lower()
option1 = option1.lower()
option2 = option2.lower()
option3 = option3.lower()

# webbrowser.open("http://google.co.in/search?q=" + question+"")


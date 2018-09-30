import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import pyscreenshot as ImageGrab
from collections import Counter
from PIL import Image, ImageEnhance
import webbrowser

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
# 4X trivia 11
# weshow 12
   
appCode = 1

def extDataFromImage( img ) :
	 sharper = ImageEnhance.Sharpness(img.convert('RGB'))
	 img = sharper.enhance(9)
	 brighter = ImageEnhance.Brightness(img)
	 img = brighter.enhance(1)
	 img = img.convert("L")
	 #img.show()
	 question = pytesseract.image_to_string(img,lang='eng')
	 return question

def extractQes( string ) :
	ans = ""
	for char in string :
		if char == '?' :
			ans += char
			break
		ans += char
	return ans

def getLines( string ) :
	lines = 1
	chars = 0
	for char in string :
		chars += 1
		if char == '\n' :
			if chars >= 3 :
				lines += 1
			chars = 0
		if char == '?' :
			break
	return lines

def refineString( string ):
	ans = ""
	for x in range(0,len(string)) :
		if string[x].isalnum() :
			ans += string[x]
	return ans

def findCnt( data, string ) :
	ans = 0
	if len(string) == 0 :
		return 0
	for x in range(0,len(data)-len(string)) :
		mis = 0
		for y in range(0,len(string)) :
			if data[x+y] != string[y] :
				mis += 1
		if mis <= len(string)/4:
			ans += 1
	return ans

def getDataFromGoogle( question ) :
	r = requests.get('https://www.google.co.in/search?q='+question)
	soup = BeautifulSoup(r.text, "html.parser")
	ls = soup.body.getText().lower()
	data = refineString(ls)
	return data

if appCode == 1 :
#tested completly
	 s = 690
	 opw = 70
	 qw = 100
	 opt3 = ImageGrab.grab(bbox=(100, s - opw , 400, s  ))
	 opt2 = ImageGrab.grab(bbox=(100, s - 2*opw , 400, s - opw ))
	 opt1 = ImageGrab.grab(bbox=(100, s - 3*opw , 400, s - 2*opw ))

	 ques = ImageGrab.grab(bbox=(80, s - 3*opw - qw , 420, s - 3*opw))
	 question = extDataFromImage( ques )
	 question = extractQes( question )

if appCode == 2 :
#tested completly what maximum i can do
	 s = 315
	 opw = 67
	 qw = 75
	 diff = 10

	 ques = ImageGrab.grab(bbox=(80, s, 420, s + qw+50))
	 question = extDataFromImage( ques )
	 question = extractQes( question )

	 line = getLines( question )
	 print ( line )
	 qw += (line -2)*21

	 opt1 = ImageGrab.grab(bbox=(120, s + qw + diff, 380, s + qw + opw - diff))
	 opt2 = ImageGrab.grab(bbox=(120, s + qw + opw + diff, 380, s + qw + 2*opw - diff))
	 opt3 = ImageGrab.grab(bbox=(120, s + qw + 2*opw + diff, 380, s + qw + 3*opw - diff))

if appCode == 3 :
#tested completly
	 s = 260
	 opw = 57
	 qw = 125
	 chprln = 33
	 ques = ImageGrab.grab(bbox=(80, s, 420, s + qw ))
	 question = extDataFromImage( ques )
	 question = extractQes( question )

	 line = getLines( question )
	 print ( line )
	 qw += (line -3)*29
	 opt1 = ImageGrab.grab(bbox=(100, s + qw, 400, s + qw + opw))
	 opt2 = ImageGrab.grab(bbox=(100, s + qw + opw, 400, s + qw + 2*opw))
	 opt3 = ImageGrab.grab(bbox=(100, s + qw + 2*opw, 400, s + qw + 3*opw))

if appCode == 4 :
#tested completly
	 s = 250
	 opw = 58
	 qw = 90
	 diff  = 0
	 ques = ImageGrab.grab(bbox=(80, s, 420, s + qw))
	 question = extDataFromImage( ques )
	 question = extractQes( question )

	 lin = getLines( question )
	 print ( lin )
	 qw += (lin -3)*22

	 opt1 = ImageGrab.grab(bbox=(100, s + qw + diff, 400, s + qw + opw - diff))
	 opt2 = ImageGrab.grab(bbox=(100, s + qw + opw +  diff, 400, s + qw + 2*opw - diff))
	 opt3 = ImageGrab.grab(bbox=(100, s + qw + 2*opw +  diff, 400, s + qw + 3*opw -  diff))

if appCode == 5 :
#tested completly what maximum i can do
	s = 315
	opw = 80
	qw = 85
	diff = 10

	ques = ImageGrab.grab(bbox=(90, s, 410, s + qw+40))
	question = extDataFromImage( ques )
	question = extractQes( question )
	line = getLines( question )
	print ( line )
	qw += (line - 3)*23
	opt1 = ImageGrab.grab(bbox=(90, s + qw + diff, 400, s + qw + opw - diff))
	opt2 = ImageGrab.grab(bbox=(90, s + qw + opw + diff, 400, s + qw + 2*opw - diff))
	opt3 = ImageGrab.grab(bbox=(90, s + qw + 2*opw + diff, 400, s + qw + 3*opw - diff))

if appCode == 6 :
#tested completly
	 s = 321
	 opw = 80
	 qw = 105
	 diff = 20
	 ques = ImageGrab.grab(bbox=(80, s, 420, s + qw))
	 question = extDataFromImage( ques )
	 question = extractQes( question )
	 opt1 = ImageGrab.grab(bbox=(100, s + qw + diff, 400, s + qw + opw - diff ))
	 opt2 = ImageGrab.grab(bbox=(100, s + qw + opw + diff , 400, s + qw + 2*opw - diff))
	 opt3 = ImageGrab.grab(bbox=(100, s + qw + 2*opw + diff, 400, s + qw + 3*opw - diff))

if appCode == 10 :
#tested completly
	 s = 702
	 opw = 52
	 qw = 140
	 diff = 10
	 opt3 = ImageGrab.grab(bbox=(83, s - opw + diff, 400, s - diff ))
	 opt2 = ImageGrab.grab(bbox=(83, s - 2*opw + diff, 400, s - opw - diff ))
	 opt1 = ImageGrab.grab(bbox=(83, s - 3*opw + diff, 400, s - 2*opw - diff ))

	 ques = ImageGrab.grab(bbox=(80, s - 3*opw - qw , 420, s - 3*opw))
	 question = extDataFromImage( ques )
	 question = extractQes( question )

if appCode == 11 :
#tested completly
	 s = 680
	 opw = 70
	 qw = 165
	 diff = 20
	 opt3 = ImageGrab.grab(bbox=(100, s - opw + diff, 400, s - diff ))
	 opt2 = ImageGrab.grab(bbox=(100, s - 2*opw + diff, 400, s - opw - diff ))
	 opt1 = ImageGrab.grab(bbox=(100, s - 3*opw + diff, 400, s - 2*opw - diff ))

	 ques = ImageGrab.grab(bbox=(80, s - 3*opw - qw , 420, s - 3*opw))
	 question = extDataFromImage( ques )
	 question = extractQes( question )

if appCode == 12 :
#tested completly
	 s = 230
	 opw = 60
	 qw = 90
	 diff = 10
	 ques = ImageGrab.grab(bbox=(80, s, 420, s+ qw ))
	 question = extDataFromImage( ques )
	 question = extractQes( question )
	 #webbrowser.open("http://google.co.in/search?q=" + question+"")
	 line = getLines( question )
	 print ( line )
	 qw += (line - 2)*20

	 opt1 = ImageGrab.grab(bbox=(100, s + qw + diff, 400, s + qw + opw - diff))
	 opt2 = ImageGrab.grab(bbox=(100, s + qw + opw +  diff, 400, s + qw + 2*opw - diff))
	 opt3 = ImageGrab.grab(bbox=(100, s + qw + 2*opw +  diff, 400, s + qw + 3*opw -  diff))
	 opt4 = ImageGrab.grab(bbox=(100, s + qw + 3*opw +  diff, 400, s + qw + 4*opw -  diff))

	 option1 = extDataFromImage( opt1 ).lower()
	 option2 = extDataFromImage( opt2 ).lower()
	 option3 = extDataFromImage( opt3 ).lower()
	 option4 = extDataFromImage( opt4 ).lower()

	 op1 = refineString(option1)
	 op2 = refineString(option2)
	 op3 = refineString(option3)
	 op4 = refineString(option4)

	 data = getDataFromGoogle( question )


	 cnt1 = findCnt( data, op1 )
	 cnt2 = findCnt( data, op2 )
	 cnt3 = findCnt( data, op3 )
	 cnt4 = findCnt( data, op4 )

	 print( "A :" + str(cnt1) )
	 print( "B :" + str(cnt2) )
	 print( "C :" + str(cnt3) )
	 print( "D :" + str(cnt4) )

#question = extDataFromImage( ques )
#question = extractQes( question )
option1 = extDataFromImage( opt1 ).lower()
option2 = extDataFromImage( opt2 ).lower()
option3 = extDataFromImage( opt3 ).lower()

#webbrowser.open("http://google.co.in/search?q=" + question+"")
op1 = refineString(option1)
op2 = refineString(option2)
op3 = refineString(option3)

#print ( question )
#print( op1 )
#print( op2 )
#print( op3 )


data = getDataFromGoogle( question )


cnt1 = findCnt( data, op1 )
cnt2 = findCnt( data, op2 )
cnt3 = findCnt( data, op3 )

print( "A :" + str(cnt1) )
print( "B :" + str(cnt2) )
print( "C :" + str(cnt3) )




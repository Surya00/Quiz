op1 = ""
for char in option1 :
    if char.isalnum() :
       op1 += char

op2 = ""
for char in option2 :
    if char.isalnum() :
       op2 += char

op3 = ""
for char in option3 :
   if char.isalnum() :
      op3 += char

print(question)
print(op1)
print(op2)
print(op3)

url = "https://www.google.co.in/search?q='"+question+"'"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'html.parser')

for script in soup(["script", "style"]):
    script.extract() 

text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)
text = text.lower()

data = "";
for char in text :
    if char.isalnum() :
        data += char

cnt1 = 0
cnt2 = 0
cnt3 = 0


for x in range(0,len(text) ) :
    cnt = 0
    mis = 0
    if len(op1) == 0 :
       break
    for y in range(0,len(op1)-len(op1)) :
        if text[x+y] == op1[y] :
           cnt += 1
        else :
           mis += 1
    if cnt >8 :
       cnt1 += 1
       continue
    if mis < 2:
       cnt1 += 1 

for x in range(0,len(text)-len(op2)) :
    cnt = 0
    mis = 0
    if len(op2) == 0 :
       break
    for y in range(0,len(op2) ) :
        if text[x+y] == op2[y] :
           cnt += 1
        else :
           mis += 1
    if cnt >8 :
       cnt2 += 1
       continue
    if mis < 2:
       cnt2 += 1 

for x in range(0,len(text)-len(op3) ) :
    cnt = 0
    mis = 0
    if len(op3) == 0 :
       break
    for y in range(0,len(op3) ) :
        if text[x+y] == op3[y] :
           cnt += 1
        else :
           mis += 1
    if cnt >8 :
       cnt3 += 1
       continue
    if mis < 3:
       cnt3 += 1 

print(op1)
print(op2)
print(op3)
print(cnt1)
print(cnt2)
print(cnt3)

if cnt1 == 0 and cnt2 == 0 and cnt3 == 0 :
   print("Tukka maro")

if cnt1 > cnt2 and cnt1 > cnt3 :
   print("option1")

if cnt2 > cnt1 and cnt2 > cnt3 :
   print("Option2")

if cnt3 > cnt1 and cnt3 > cnt2 :
   print("Option3")





# -*- coding: utf-8 -*-
"""Science id cards.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ylVeo988lCQokmvag06tJdMVdOQj6rmg
"""

pip install pyPDF2

"""#Loading pdf data"""

import PyPDF2
sci=open('/content/drive/MyDrive/projects2023/IDGen2024/test/sci/Copy of ESIF_Registration_109991 science 2023.pdf','rb')
sciReader=PyPDF2.PdfReader(sci)
pageC=len(sciReader.pages)
print(pageC)

sBook=[]
for i in range (pageC):
  sBook.append(sciReader.pages[i].extract_text())
  #print(sBook[22])

#page1=sciReader.pages[22]
#pg1Txt=page1.extract_text()
#print(pg1Txt)
#sci.close()

word_list=[]
for i in range (pageC):
  word_list.append(sBook[i].splitlines())
#word_list=pg1Txt.splitlines()
print(word_list)

word_list[22]



"""#Formatting data for easy list access"""

#Configure loop -done
for j in range(pageC):
  x=word_list[j].index('RollSubject Opitonal Group Photo Signature')
  for i in range (x+1):
    word_list[j].pop(0)
#print((x))
# all pages of word list now has pure student data for extraction ranging from page 0-22

print(word_list[20])

word_list[20][3]# need to traverse 4 indexex(0-3) to accesss all info of  a student total traversal should be length of that page%4

round(len(word_list[20])/4)

word_list[0][4:8]

#optional testing
#data and code fixing block
#print(opt)
#cPage=word_list[2]
#cPage[4]=cPage[4]+' '+cPage[5]
#x=cPage[4:8]
#opt=x[3][-11:-7]
#print(x)
#word_list[2][4:8]
#word_list[2][4]=word_list[2][4]+' '+word_list[2][5]
#word_list[2].pop(5)
#word_list[13][8]=word_list[13][8]+' '+word_list[13][9]
#word_list[13][8:12]    big name
#word_list[18].pop(6)
#word_list[21][4]=word_list[21][4]+word_list[21][5]
#word_list[21].pop(5)
#word_list[21][4:8]
#word_list[21][4:8]
#testList=[]
#quad1=['name','roll','section','group']
#quad2=['name2','roll2','section2','group2']
#testList.append(quad1)
#testList.append([1,2,3,4])
#testList.append([5,6,'helo',8])
#print(testList)

#configure a loop for a whole page
sci=[]
for k in range(pageC):
  #traverse per page
  #current page
  cPage=word_list[k]
  o=round(len(cPage)/4)
  i=0
  for l in range(o):
    j=i+4
    x=cPage[i:j]#taking individual student
    y=x[3].split(',')#for roll
    n=len(y[0]) #here 4 means the roll is a number consisting only 1 digit, 5 means 2 digit roll and 6 means 3 digit roll
    student_name=x[0][((n-3)*2+1):]#name starts after the amount of digits in student roll determined by upper loop.
    roll=str(y[0][:(n-3)])#roll stops after its digit count.
    #group="science" #the whole book is about science group
    section= x[2][-1:]
    opt=x[3][-11:-7]
    if(int(opt)==265):
      optional="Higher Math"
    elif(int(opt)==178):
      optional="Biology"
    else:
      optional=str(opt)
    i=i+4
    #save student info in an array
    si=0
    sci.append([student_name,roll,section,optional])

    #print("\nstudent name: "+student_name+"\nroll        : "+roll+"\ngroup       : Science"+"\nSection     : "+section+"\noptional    : "+str(optional))

"""#To reuse the list in txt format"""

newBook=open('/content/drive/MyDrive/projects2023/IDGen2024/sci/ScienceInputBook.txt','r')
bookString=newBook.read()
StringList=bookString.splitlines()
sList=[]
length=len(StringList)/4

for i in range (int(length)):
  obj1=StringList.pop()
  obj2=StringList.pop()
  obj3=StringList.pop()
  obj4=StringList.pop()
  sList.append([obj4,obj3,obj2,obj1])
sList.reverse()
print(sList)
newBook.close()

sList[153]

"""#Card generation"""

#card generation
import pandas as pd
import cv2
from matplotlib import pyplot as plt #imported because cv2 imshow doesnt work in colab
import os
from PIL import Image, ImageDraw, ImageFont
parent='/content/drive/MyDrive/projects2023/IDGen2024'
images=parent+'/photos/picture'

#look discarded code in parent

#test block 2
sciImg[0]

#photo loading test
#photoPath=images'
#img1=cv2.imread(os.path.join(images,'01.JPG')) #joining path+filename
#img1RGB=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
#plt.imshow(img1RGB)
#plt.axis('off')
#plt.show()

sci[0][3]

#test block
#sid=2
#try:
#  #sci[student number][info number 0:name 1:roll 2:section 3:optional]
#  x='0'+str(sList[sid][1])+".JPG"#load student image by roll
#  front_photo = Image.open(os.path.join(images,x))
#except:
#  x=parent+'/Templates/blank Template.jpg'
#  front_photo = Image.open(os.path.join(images,x))

front_photo

len(sList)

width = 2026
height = 638
dpi = 300
font = ImageFont.truetype("/content/drive/MyDrive/projects2023/IDGEN/times-new-roman-grassetto.ttf", 38)  # Use any font of your choice
font1= ImageFont.truetype("/content/drive/MyDrive/projects2023/IDGEN/times-new-roman.ttf", 38)
main_photo = Image.open(parent+'/Templates/ComboV3.jpg')
sci=sList
files_made=[]
#sid=154
for sid in range(154):
  card = Image.new('RGB', (width, height), color='white')
  card.paste(main_photo, (0, 0))

  # student index

  try:
    #sci[student number][info number 0:name 1:roll 2:section 3:optional]
    sd=sci[sid][1]
    if(int(sd)<10):
      x='0'+str(sd)+".JPG"#load student image by roll
    else:
      x=str(sd)+".JPG"
    front_photo = Image.open(os.path.join(images,x))
  except:
    x=parent+'/Templates/blank Template.jpg'
    front_photo = Image.open(os.path.join(images,x))
  front_photo = front_photo.resize((225, 300))  # Resize to 0.5x
  card.paste(front_photo, (750, 225))

  # Draw text "Name field"
  draw = ImageDraw.Draw(card)
  draw.text((20, 225), sci[sid][0], font=font, fill="black")

  # Draw text "roll"
  draw.text((100, 375), str(sci[sid][1]), font=font1, fill="black")

  # Draw text "section"
  draw.text((150, 422), str(sci[sid][2]), font=font1, fill="black")
  # Draw text "optional"
  #draw.text((190, 478), str(sci[sid][3]), font=font1, fill="black")

  # Save the final card
  j=sd
  #output_dir=parent+'/test/out'
  output_dir=parent+'/Output cards/Science' #set back to H
  output_filename = os.path.join(output_dir, f"S_{j}.jpg")

  card.save(output_filename)
  files_made.append(output_filename)
#card.show(output_filename)
#performance record: no gpu 39s , T4 gpu: 56s, no gpu run2 1min32s

output_filename

"""#Binding cards"""

#test bind
idspath='/content/drive/MyDrive/projects2023/IDGEN/Output cards/S'
card = Image.new('RGB', (2480, 3508), color='white')
card1=Image.open('/content/drive/MyDrive/projects2023/IDGen2024/test/out/i_1.jpg')
card2=Image.open('/content/drive/MyDrive/projects2023/IDGen2024/test/out/i_185.jpg')
card3=Image.open('/content/drive/MyDrive/projects2023/IDGen2024/test/out/i_2.jpg')
card4=Image.open('/content/drive/MyDrive/projects2023/IDGen2024/test/out/i_99.jpg')
card5=Image.open('/content/drive/MyDrive/projects2023/IDGen2024/test/out/i_85.jpg')

card.paste(card1,(150,100))
card.paste(card2,(150,758))
card.paste(card3,(150,1416))
card.paste(card4,(150,2074))
card.paste(card5,(150,2732))
output_dir='/content/drive/MyDrive/projects2023/IDGen2024/test/out'
output_filename = os.path.join(output_dir, f"Bind_{i}.jpg")
card.save(output_filename)

#enlist cards

files_made[2]

len(files_made)

#making a page
#31 pages for Science

idspath=parent+'/Output cards/Science'
j=0 #total ids 154
i=0 #total pages
max=154
for i in range(31):
  card = Image.new('RGB', (2480, 3508), color='white')
  if(j<max):#
    #ids="S_"+str(j)+".jpg"
    card1=Image.open(files_made[j])
    card.paste(card1,(150,100))#
    j=j+1
    if(j<max):
      #ids="S_"+str(j)+".jpg"
      card1=Image.open(files_made[j])
      card.paste(card1,(150,758))#
      j=j+1
      if(j<max):
        #ids="S_"+str(j)+".jpg"
        card1=Image.open(files_made[j])
        card.paste(card1,(150,1416))#
        j=j+1
        if(j<max):
          #ids="S_"+str(j)+".jpg"
          card1=Image.open(files_made[j])
          card.paste(card1,(150,2074))#
          j=j+1
          if(j<max):
            #ids="S_"+str(j)+".jpg"
            card1=Image.open(files_made[j])
            card.paste(card1,(150,2732))#
            j=j+1
  # the loop looks inefficient but brain is not braining now
  output_dir=parent+'/Output books/Science'
  output_filename = os.path.join(output_dir, f"S_{i}.jpg")
  card.save(output_filename)
  #card.show("output_card.jpg")
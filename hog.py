from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import csv
import sys

xCenterMac = 2048
yCenterMac = 970
xCenterVeille = 2048
yCenterVeille = 950

xRBMac = 3100
yRBMac = 1300
yRB2Mac = 1600

xRBVeille = 3100
yRBVeille = 1350
yRB2Veille = 1650

continent = 4
rangee = 5
place = 6
battletag = 3
i = 0

fontCenter = ImageFont.truetype("Action of the Time.ttf", 400)
fontCenterCalc = ImageFont.truetype("Action of the Time.ttf", 200)
fontRB = ImageFont.truetype("Action of the Time.ttf", 240)
fontRBCalc = ImageFont.truetype("Action of the Time.ttf", 120)

with open('hog.csv', 'rt') as f :
	reader = csv.reader(f, delimiter=',', quotechar='|')
	for row in reader :
		if i == 0:
			i += 1
		elif (len(row[battletag]) > 0) :
			imgMac = Image.open("wpMac.png")
			imgVeille = Image.open("wpVeille.png")
			drawMac = ImageDraw.Draw(imgMac)
			drawVeille = ImageDraw.Draw(imgVeille)

			if "#" in row[battletag] :		
				pseudo = row[battletag].split('#')[0].strip()
			else:
				pseudo = row[battletag].strip()
			width, height = drawMac.textsize(pseudo, font=fontCenterCalc)
			startX = xCenterMac - width
			startY = yCenterMac - height - 50 
			drawMac.text((startX, startY), pseudo, (0, 0, 0), font=fontCenter)
			
			width, height = drawMac.textsize(row[continent], font=fontRBCalc)
			startX = xRBMac - width
			startY = yRBMac - height
			drawMac.text((startX, startY), row[continent], (0,0,0), font=fontRB)

			chaine = "R" + row[rangee] + "P" + row[place]
			width, height = drawMac.textsize(chaine, font=fontRBCalc)
			startX = xRBMac - width
			startY = yRB2Mac - height	
			drawMac.text((startX, startY), chaine, (0,0,0), font=fontRB)
			
			width, height = drawMac.textsize(pseudo, font=fontCenterCalc)
			startX = xCenterVeille - width
			startY = yCenterVeille - height - 45
			drawVeille.text((startX, startY), pseudo, (0,0,0), font=fontCenter)

			width, height = drawMac.textsize(row[continent], font=fontRBCalc)
			startX = xRBVeille - width
			startY = yRBVeille - height
			drawVeille.text((startX, startY), row[continent], (0,0,0), font=fontRB)

			width, height = drawMac.textsize(chaine, font=fontRBCalc)
			startX = xRBVeille - width
			startY = yRB2Veille - height
			drawVeille.text((startX, startY), chaine, (0,0,0), font=fontRB)
			
			imgMac.save("Wallpapers/" + row[battletag] + "-Mac.png")
			imgVeille.save("Wallpapers/" + row[battletag] + "-Veille.png")

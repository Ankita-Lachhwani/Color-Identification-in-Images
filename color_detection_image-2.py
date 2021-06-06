'''Ankita Lachhwani- author 
 Color Image Identification'''
# to instal cv2 and pandas
# write in the terminal "pip install cv2" and then write "pip install pandas"
# after installiing import it here

import cv2
from cv2 import cv2
import pandas as pd

# write where your image is located in your pc in image_path
# write where is your csv path located in your pc in csv_path

image_path = r'C:\Users\lenovo\Desktop\color-image-identification\CII.jpg'
csv_path = r'C:\Users\lenovo\Desktop\color-image-identification\colors2.csv'

# reading csv file
index = ['color', 'color_name', 'hex', 'Red', 'Green', 'Blue']
df = pd.read_csv(csv_path, names=index, header=None)

# reading image
jpg = cv2.imread(image_path)
jpg = cv2.resize(jpg, (800,600))

#declaring global variables 
clicked = False
r = g = b = xpos = ypos = 0

#function to calculate min distance from all colors to get the most matching color
def get_color_name(Red,Green,Blue):
	minimum = 50
	for i in range(len(df)):
		d = abs(Red - int(df.loc[i,'Red'])) + abs(Green - int(df.loc[i,'Green'])) + abs(Blue - int(df.loc[i,'Blue']))
		if d <= minimum:
			minimum = d
			cname = df.loc[i, 'color_name']

	return cname

#function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x
		ypos = y
		b,g,r = jpg[y,x]
		b = int(b)
		g = int(g)
		r = int(r)

# creating window
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
	cv2.imshow('image', jpg)
	if clicked:
		#cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
		cv2.rectangle(jpg, (20,20), (600,60), (b,g,r), -1)

		#Creating text string to display( Color name and RGB values )
		text = get_color_name(r,g,b) + ' Red=' + str(r) + ' Green=' + str(g) + ' Blue=' + str(b)
		#cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
		cv2.putText(jpg, text, (50,50), 1,0.8, (255,255,255),1,cv2.LINE_AA)

		#For very light colours we will display the text in black colour
		if r+g+b >=600:
			cv2.putText(jpg, text, (50,50), 1,0.8, (0,0,0),1,cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()

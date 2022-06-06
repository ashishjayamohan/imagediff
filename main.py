from PIL import Image

'''
bird1 - original image
bird2 - subtle difference
bird3 - different bird, same setting
'''

p1open = Image.open("bird1.jpg")
p2open = Image.open("bird2.jpg")
p3open = Image.open("bird3.jpg")

p1 = p1open.load()
p2 = p2open.load()
p3 = p3open.load()

diffscore1 = 0
diffscore2 = 0

for i in range(p1open.size[0]):
  for j in range(p1open.size[1]):
    diffscore1 += (p1[i,j][0] - p2[i,j][0] + p1[i,j][1] - p2[i,j][1] + p1[i,j][2] - p2[i,j][2])/3
    diffscore2 += (p1[i,j][0] - p3[i,j][0] + p1[i,j][1] - p3[i,j][1] + p1[i,j][2] - p3[i,j][2])/3

print(str(diffscore1))
print(str(diffscore2))
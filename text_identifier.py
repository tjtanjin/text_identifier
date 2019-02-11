# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[10].id)
# while True:
#   text = input("What would you like me to say?\n> ")
#   engine.say(text)
#   engine.runAndWait()

# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

# from PIL import Image
# import pytesseract

# print(pytesseract.image_to_string(Image.open('DL-1.png')))

import pytesseract
from pytesseract import Output
import cv2
img = cv2.imread('DL-5.png')
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])

test = ["Traffic Report"]
newtest =  [word for line in test for word in line.split()]
coordinates = []
width = 65
count = 0

for words in newtest:
    for y in d["text"]:
        if words == y:
            if coordinates != []:
                order = d["text"].index(words) - previous_index
                if order == 1 or order == -1:
                    coordinates.append(d["text"].index(words))
                    previous_index = d["text"].index(words)
                else:
                    d["text"][d["text"].index(words)] = ""
            else:
                coordinates.append(d["text"].index(words))
                previous_index = d["text"].index(words)

for i in range(len(coordinates)):
            width += d["width"][coordinates[i]]
print(coordinates)
left = d["left"][coordinates[0]] - 15
top = d["top"][coordinates[0]] - 10
height = d["height"][coordinates[0]] + 20
for i in range(n_boxes):
    (x, y, w, h) = (left, top, width, height)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)




# for x,y in d.items():
#     print(d["text"])
#     if type(y) != int:
#         if "TLA" in y:
#             position1 = y.index("Domain")
#             position2 = y.index("Name")
#             #position3 = y.index("is")
#             #position4 = y.index("required")

#             left = d["left"][position1] - 15
#             top = d["top"][position1] - 10
#             width = d["width"][position1] + d["width"][position2] +65#+ d["width"][position3] + d["width"][position4] + 65
#             height = d["height"][position1] + 20
#             for i in range(n_boxes):
#                 (x, y, w, h) = (left, top, width, height)
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


# for x,y in d.items():
#     print(d["text"])
#     if type(y) != int:
#         if "TLA" in y:
#             position = y.index("TLA")
#             left = d["left"][position]
#             top = d["top"][position]
#             width = d["width"][position]
#             height = d["height"][position]
#             for i in range(n_boxes):
#                 (x, y, w, h) = (left, top, width, height)
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# for x,y in d.items():
#     if type(y) != int:
#         if "Edit" in y:
#             position = y.index("Edit")
#             left = d["left"][position]
#             right = d["right"][position]
#             width = d["width"][position]
#             height = d["height"][position]
#             for z in x:
#                 if type(z) != int:
#                     for i in range(n_boxes):
#                         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#                         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite('NewDL-5.png',img)

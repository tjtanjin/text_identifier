import pytesseract, cv2
from pytesseract import Output

img = cv2.imread(image_name)
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])

test = [text_to_look_for]
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

cv2.imwrite(saved_image_name,img)

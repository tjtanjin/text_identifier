import pytesseract, cv2
from pytesseract import Output

#read and double image size for increased accuracy
img = cv2.imread(image_name)
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

#read data from image
d = pytesseract.image_to_data(img, output_type=Output.DICT)

#string to identify (separate multiple sentences with commas)
identify_string = [text_to_look_for_1, text_to_look_for_2]

#create an initially empty list to hold coordinates and set initial box with to 65
coordinates = []
width = 65

#repeat for every sentence in identify_string
for sentences in identify_string:
    sentences = [sentences]
    sentence = [word for line in sentences for word in line.split()]
    for words in sentence:
        for y in d["text"]:
            #check if words match
            if words == y:
                if coordinates != []:
                    order = d["text"].index(words) - previous_index
                    #append the coordinate only if they are within 1 index to ensure they are from the same sentence
                    if order == 1 or order == -1:
                        coordinates.append(d["text"].index(words))
                        previous_index = d["text"].index(words)
                    else:
                        d["text"][d["text"].index(words)] = ""
                else:
                    coordinates.append(d["text"].index(words))
                    previous_index = d["text"].index(words)
    #modify width for bounding box
    for i in range(len(coordinates)):
                width += d["width"][coordinates[i]]
    #print(coordinates) #uncomment to view coordinates of box drawn
    left = d["left"][coordinates[0]] - 15
    top = d["top"][coordinates[0]] - 10
    height = d["height"][coordinates[0]] + 20
    (x, y, w, h) = (left, top, width, height)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #reset coordinates and width after each sentence
    coordinates = []
    width = 65

#save image
cv2.imwrite(saved_image_name,img)

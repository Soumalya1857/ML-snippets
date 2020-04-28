import cv2
import numpy as np


#load yolo algo
net = cv2.dnn.readNet("yolov3.weights","yolov3.cfg")

classes = []
with open("coco.names","r") as f:
    classes = [line.strip() for line in f.readlines()]


layer_name = net.getLayerNames()
output_layers = [layer_name[i[0]-1]  for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0,255,size = (len(classes),3))

img = cv2.imread("yolo-object-detection/images/WhatsApp Image 2020-04-28 at 1.07.51 AM (2).jpeg")
img = cv2.resize(img,None, fx = 0.4, fy = 0.4)
height , width, channels = img.shape[:3]



blob = cv2.dnn.blobFromImage(img,0.00392,(416,416),(0,0,0),True,crop = False)


net.setInput(blob)
outs = net.forward(output_layers)

#slowing info on screen

boxes = []
confidences = []
class_ids = []


for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)

            x = int(center_x - w/2)
            y = int(center_y - h/2)

            #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
             
            #cv2.circle(img, (center_x,center_y),10,(0,255,0),2)

            boxes.append([x,y,w,h])
            confidences.append(float(confidence))
            class_ids.append(class_id)


number_object_detected = len(boxes)
indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)
font = cv2.FONT_HERSHEY_PLAIN
for i in range(number_object_detected):
    if i in indexes:
        x,y,w,h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[i]
        #cv2.rectangle(img, (x,y) ,color,2)
        #cv2.putText(img, label, (x,y+30),font, 3,color,3)
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, color, 2)




cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
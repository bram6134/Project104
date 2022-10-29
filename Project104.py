import cv2
import os

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"SUN",(80,75), cv2.FONT_HERSHEY_COMPLEX, 1.5, (1, 1, 255))
cv2.putText(img,"Mercury",(116,275), cv2.FONT_HERSHEY_COMPLEX, 0.5, (15,253,250))
cv2.putText(img,"Venus",(196,275), cv2.FONT_HERSHEY_COMPLEX, 0.5, (15,253,250))
cv2.putText(img,"Earth",(285,275), cv2.FONT_HERSHEY_COMPLEX, 0.5, (15,253,250))
cv2.putText(img,"Mars",(385,275), cv2.FONT_HERSHEY_COMPLEX, 0.5, (15,253,250))
cv2.putText(img,"Jupiter",(585,100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (15,253,250))
cv2.putText(img,"Saturn",(775,100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (15,253,250))
cv2.putText(img,"Uranus",(965,100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (15,253,250))
cv2.putText(img,"Neptune",(1110,100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (15,253,250))
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)

import cv2

img=cv2.imread('00-puppy.jpg')

while True:
    cv2.imshow('puppy',img)
    
    # if we waited 1 ms and pressed the escape key
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()


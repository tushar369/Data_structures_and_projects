import cv2

# pre-trained front face data(haarcascade_frontalface_defauld.xml)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('peaky2_color.jpg')  
g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
co_ordinates = trained_face_data.detectMultiScale(g_img)

for i in range(len(co_ordinates)):
    (x, y, w, h) = co_ordinates[i]
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
    
cv2.imshow('detection', img)
cv2.waitKey()


print('done')

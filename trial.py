import cv2
import numpy as np 
import pyscreenshot
import pyautogui

#img = cv2.imread("screenshot.jpg", 1)


def click(event,x,y,flags, params):
        global click1, point1
        if event == cv2.EVENT_LBUTTONDOWN:
                # if mousedown, store the x,y position of the mous
                click1 = True
                point1 = (x,y)
        elif event == cv2.EVENT_MOUSEMOVE and click1:
                # when dragging pressed, draw rectangle in image
                img_copy = img.copy()
                cv2.rectangle(img_copy, point1, (x,y), (0,0,255),2)
                cv2.imshow("Image", img_copy)
        elif event == cv2.EVENT_LBUTTONUP:
                # on mouseUp, create subimage
                click1 = False
                sub_img = img[point1[1]:y,point1[0]:x]
                cv2.imshow("subimg", sub_img)
def foo():
        image1=pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image1), cv2.COLOR_RGB2BGR)
        cv2.imwrite("mid.png", image)
#im42=image42.convert('RGB')
        img=cv2.imread("mid.png",1)
        click1 = False
        point1 = (0,0)

        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image", click)

        cv2.imshow("Image", img)
        cv2.waitKey(0)
cv2.destroyAllWindows()
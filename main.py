from PIL import Image
import pyscreenshot
import keyboard
import trial
import pyautogui

# import keyboard  # using module keyboard
# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#             print('You Pressed A Key!')
#             break  # finishing the loop
#     except:
#         break  # if user pressed a key other than the given key the loop will break
#image1 = Image.open(r'bunny.png')
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
                
image42 = Image.open(r'bunny.png')
im42=image42.convert('RGB')

imagelist=[]
while True:
	if(keyboard.is_pressed('s')):
		#trial.foo()


		image1=pyscreenshot.grab()
		im1=image1.convert('RGB')
		imagelist.append(im1)
	if(keyboard.is_pressed('q')):
		break;


#print(imagelist)
im42.save(r'final.pdf',save_all=True,append_images=imagelist)
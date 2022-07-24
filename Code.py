from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk #python3-pil.imagetk python3-imaging-tk
import cv2
import math


 
def showimage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG File", "*.jpg"), ("PNG file", "*.png"),("JPEG File", "*.jpeg"),("All Files", "*.*")))
    img = Image.open(fln)
    img.thumbnail((100,100))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    solve(fln)
    


def solve(path):



    img = cv2.imread(path)
    pointsList = []
     
    def mousePoints(event,x,y,flags,params):
        if event == cv2.EVENT_LBUTTONDOWN:
            size = len(pointsList)
            if size != 0 and size % 3 != 0:
                cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,0,255),2)
            cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
            pointsList.append([x,y])
     
     
    def gradient(pt1,pt2):
        return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
     
    def getAngle(pointsList):
        pt1, pt2, pt3 = pointsList[-3:]
        m1 = gradient(pt1,pt2)
        m2 = gradient(pt1,pt3)
        angR = math.atan((m2-m1)/(1+(m2*m1)))
        angD = round(math.degrees(angR))
        
        if(angD>0 and angD<=180):
         cv2.putText(img,str(angD),(pt1[0]-40,pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,
                    1.5,(0,0,255),2)
        else:
         angD=180-abs(angD)
         cv2.putText(img,str(angD),(pt1[0]-40,pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,
                    1.5,(0,0,255),2)
        
        


    cv2.imshow('Image',img)


    while True:

       

           
     
        if len(pointsList) % 3 == 0 and len(pointsList) !=0:
            getAngle(pointsList)
     
        cv2.imshow('Image',img)
        cv2.setMouseCallback('Image',mousePoints)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            pointsList = []
            img = cv2.imread(path)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit(0)


 
root = Tk()
 
 
frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)
 
lbl = Label(root)
lbl.pack()
 
btn = Button(frm, text="Browse Image", command=showimage)
btn.pack(side=tk.LEFT,padx=10)
 
btn2 = Button(frm, text="Exit", command=lambda: exit())
btn2.pack(side=tk.RIGHT,padx=10)

 
 
root.title("Image Browser")
root.geometry("500x450")
root.mainloop()

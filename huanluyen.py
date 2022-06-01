from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Huanluyen:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x140+400+300")
        self.root.title("HUẤN LUYỆN NHẬN DẠNG")

        btn_1=Button(self.root,command=self.batdauhuanluyen,text="BẮT ĐẦU HUẤN LUYỆN",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn_1.place(x=50,y=50,width=400,height=40)

    def batdauhuanluyen(self):
        data_dir=("anhchup")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training", imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("filehuanluyen.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("thanh cong","da huan luyen xong")


if __name__=="__main__":
    root=Tk()
    ojb=Huanluyen(root)
    root.mainloop()
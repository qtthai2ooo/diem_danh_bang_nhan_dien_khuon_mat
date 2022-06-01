from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Diemdanhbangkhuonmat:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x140+400+300")
        self.root.title("ĐIỂM DANH BẰNG KHUÔN MẶT")

        btn_1=Button(self.root,command=self.batdaudiemdanh,text="BẮT ĐẦU ĐIỂM DANH",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn_1.place(x=50,y=50,width=400,height=40)


    def bangdiemdanh(self,msv,r,l):
        with open("diemdanh.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((msv not in name_list) and (r not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{msv},{r},{l},{dtString},{d1}")


    def batdaudiemdanh(self):
        def draw_boundray(img,classifier,scaleFactor,minNeightbors,color,text,clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeightbors)
            
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0), 3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=(int(100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="",database="nhandangkhuonmat")
                my_cursor=conn.cursor()


                msv = str(id)

                my_cursor.execute("select hoten from hocsinh where msv="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)


                my_cursor.execute("select lop from hocsinh where msv="+str(id))
                l=my_cursor.fetchone()
                l="+".join(l)


                if confidence>77:
                    cv2.putText(img, f"MSV:{msv}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    cv2.putText(img, f"TEN:{r}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    cv2.putText(img, f"LOP:{l}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    self.bangdiemdanh(msv,r,l)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, f"khong the nhan dien", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                
                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img, faceCascade, 1.1, 10, (255,25,255), "face", clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("filehuanluyen.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("dng diem danh", img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__=="__main__":
    root=Tk()
    ojb=Diemdanhbangkhuonmat(root)
    root.mainloop()
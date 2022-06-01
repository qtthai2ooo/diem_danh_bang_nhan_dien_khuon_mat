from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from hocsinh import Hocsinh
from huanluyen import Huanluyen
from diemdanhbangkhuonmat import Diemdanhbangkhuonmat
from bangdiemdanh import Bangdiemdanh
import os

class Hethongnhandangkhuonmat:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("HỆ THỐNG ĐIỂM DANH BẰNG KHUÔN MẶT")


        img=Image.open(r"image_app\logovku.png")
        img=img.resize((1000,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=130)



        img1=Image.open(r"image_app\menubar.png")
        img1=img1.resize((1550,710),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="PHẦN MỀM ĐIỂM DANH BẰNG KHUÔN MẶT",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=-50,y=0,width=1530,height=45)



        img2=Image.open(r"image_app\student.jpg")
        img2=img2.resize((200,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2=Button(bg_img,image=self.photoimg2,command=self.btn_hocsinh,cursor="hand2")
        b2.place(x=200,y=50,width=200,height=200)

        b2_1=Button(bg_img,text="SINH VIÊN",command=self.btn_hocsinh,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=200,y=250,width=200,height=40)



        img3=Image.open(r"image_app\huanluyen.jpg")
        img3=img3.resize((200,200),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3=Button(bg_img,command=self.btn_huanluyen,image=self.photoimg3,cursor="hand2")
        b3.place(x=600,y=50,width=200,height=200)

        b3_1=Button(bg_img,command=self.btn_huanluyen,text="HUẤN LUYỆN",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=600,y=250,width=200,height=40)



        img4=Image.open(r"image_app\nhandang.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4=Button(bg_img,command=self.btn_nhandang,image=self.photoimg4,cursor="hand2")
        b4.place(x=1000,y=50,width=200,height=200)

        b4_1=Button(bg_img,command=self.btn_nhandang,text="NHẬN DẠNG",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1000,y=250,width=200,height=40)



        img5=Image.open(r"image_app\diemdanh.png")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5=Button(bg_img,command=self.btn_bangdiemdanh,image=self.photoimg5,cursor="hand2")
        b5.place(x=200,y=300,width=200,height=200)

        b5_1=Button(bg_img,command=self.btn_bangdiemdanh,text="BẢNG ĐIỂM DANH",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=500,width=200,height=40)


        img6=Image.open(r"image_app\anh.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6=Button(bg_img,command=self.mo_anh,image=self.photoimg6,cursor="hand2")
        b6.place(x=600,y=300,width=200,height=200)

        b6_1=Button(bg_img,command=self.mo_anh,text="ẢNH",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=600,y=500,width=200,height=40)


        img7=Image.open(r"image_app\thoat.png")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1000,y=300,width=200,height=200)

        b7_1=Button(bg_img,text="THOÁT",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=1000,y=500,width=200,height=40)
    

    def mo_anh(self):
        os.startfile("anhchup")

    def btn_hocsinh(self):
        self.new_window=Toplevel(self.root)
        self.app=Hocsinh(self.new_window)

    def btn_huanluyen(self):
        self.new_window=Toplevel(self.root)
        self.app=Huanluyen(self.new_window)

    def btn_nhandang(self):
        self.new_window=Toplevel(self.root)
        self.app=Diemdanhbangkhuonmat(self.new_window)
    def btn_bangdiemdanh(self):
        self.new_window=Toplevel(self.root)
        self.app=Bangdiemdanh(self.new_window)

if __name__=="__main__":
    root=Tk()
    ojb=Hethongnhandangkhuonmat(root)
    root.mainloop()
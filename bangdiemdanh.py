from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np
from time import strftime
from datetime import datetime

mydata=[]

class Bangdiemdanh:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("BẢNG ĐIỂM DANH SINH VIÊN BẰNG KHUÔN MẶT")

        self.var_msv=StringVar()
        self.var_hoten=StringVar()
        self.var_lop=StringVar()
        self.var_ngay=StringVar()
        self.var_thoigian=StringVar()
        self.var_status=StringVar()

        self.serch_var=StringVar()
        self.serchTxt_var=StringVar()
        



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


        title_lbl=Label(bg_img,text="BẢNG ĐIỂM DANH SINH VIÊN",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1400,height=600)

        #form chi tiết
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="THÔNG TIN CHI TIẾT SINH VIÊN ĐIỂM DANH",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=500)

        img_left=Image.open(r"image_app\student_detail.jpg")
        img_left=img_left.resize((450,100),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bg_img=Label(left_frame,image=self.photoimg_left)
        bg_img.place(x=20,y=0,width=600,height=100)

        #form thông tin sinh vien
        thongtinsinhvien_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="THÔNG TIN SINH VIÊN ĐIỂM DANH",font=("times new roman",12,"bold"))
        thongtinsinhvien_frame.place(x=5,y=150,width=650,height=300)

        #msv        
        msv_label=Label(thongtinsinhvien_frame,text="MSV:",font=("times new roman",12,"bold"))
        msv_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        msv_entry=ttk.Entry(thongtinsinhvien_frame,textvariable=self.var_msv,width=20,font=("times new roman",12,"bold"))
        msv_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #họ tên        
        hoten_label=Label(thongtinsinhvien_frame,text="HỌ VÀ TÊN:",font=("times new roman",12,"bold"))
        hoten_label.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        hoten_entry=ttk.Entry(thongtinsinhvien_frame,textvariable=self.var_hoten,width=20,font=("times new roman",12,"bold"))
        hoten_entry.grid(row=0,column=4,padx=10,pady=5,sticky=W)

          # lớp
        lop_label=Label(thongtinsinhvien_frame,text="LỚP",font=("times new roman",12,"bold"))
        lop_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        lop_entry=ttk.Entry(thongtinsinhvien_frame,textvariable=self.var_lop,width=20,font=("times new roman",12,"bold"))
        lop_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #ngay thang        
        ngay_label=Label(thongtinsinhvien_frame,text="NGÀY THÁNG:",font=("times new roman",12,"bold"))
        ngay_label.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        ngay_entry=ttk.Entry(thongtinsinhvien_frame,textvariable=self.var_ngay,width=20,font=("times new roman",12,"bold"))
        ngay_entry.grid(row=1,column=4,padx=10,pady=5,sticky=W)

        #thoi gian        
        thoigian_label=Label(thongtinsinhvien_frame,text="THỜI GIAN:",font=("times new roman",12,"bold"))
        thoigian_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        thoigian_entry=ttk.Entry(thongtinsinhvien_frame,textvariable=self.var_thoigian,width=20,font=("times new roman",12,"bold"))
        thoigian_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        

        #btn frame
        btn_frame=Frame(thongtinsinhvien_frame,bd=1,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,width=17,text="Mở file csv",command=self.importcsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,width=17,text="xuất file csv",command=self.exportcsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,width=17,text="cập nhập",font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,width=17,text="RESET",command=self.reset,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #form bảng
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="NHỮNG SINH VIÊN ĐÃ ĐIỂM DANH",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=500)


        #search frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="TÌM KIẾM",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=5,width=650,height=70)

        search_label=Label(search_frame,text="TÌM KIẾM THEO:",font=("times new roman",12,"bold"))
        search_label.grid(row=0,column=0,padx=2,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.serch_var,font=("times new roman",12,"bold"),state="readonly",width=12)
        search_combo["values"]=("msv","hoten","lop")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5)

        
        search_entry=ttk.Entry(search_frame,textvariable=self.serchTxt_var,width=17,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,sticky=W)

        search_btn=Button(search_frame,width=12,command=self.search_data,text="TÌM KIẾM",font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        showall_btn=Button(search_frame,width=12,text="XEM TẤT CẢ",font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)

        #TABLE frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=80,width=650,height=400)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.diemdanh_table=ttk.Treeview(table_frame,column=("msv","hoten","lop","thoigian","ngay"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.diemdanh_table.xview)
        scroll_y.config(command=self.diemdanh_table.yview)

        self.diemdanh_table.heading("msv",text="MSV")
        self.diemdanh_table.heading("hoten",text="HỌ VÀ TÊN")
        self.diemdanh_table.heading("lop",text="LỚP")
        self.diemdanh_table.heading("ngay",text="NGÀY THÁNG")
        self.diemdanh_table.heading("thoigian",text="THỜI GIAN")



        self.diemdanh_table["show"]="headings"

        self.diemdanh_table.column("msv",width=100)
        self.diemdanh_table.column("hoten",width=200)
        self.diemdanh_table.column("lop",width=100)
        self.diemdanh_table.column("ngay",width=100)
        self.diemdanh_table.column("thoigian",width=100)

        self.diemdanh_table.pack(fill=BOTH,expand=1)

        self.diemdanh_table.bind("<ButtonRelease>",self.getdata)

    def fetchdata(self,rows):
        self.diemdanh_table.delete(*self.diemdanh_table.get_children())
        for i in rows:
          self.diemdanh_table.insert("",END,values=i)
    
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
          csvread=csv.reader(myfile,delimiter=",")
          for i in csvread:
            mydata.append(i)
          self.fetchdata(mydata)

    def exportcsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("không có dữ liệu","không có dữ liệu để lưu",parent=self.root)
          return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
          exp_write=csv.writer(myfile,delimiter=",")
          for i in mydata:
            exp_write.writerow(i)
          messagebox.showinfo("lưu dữ liệu","Đã lưu dữ liệu tới:"+os.path.basename(fln)+" thành công")
      except EXCEPTION as es:
          messagebox.showerror("loi",f"loi:{str(es)}",parent=self.root)
    

    def search_data(self):
      if self.serchTxt_var.get()=="":
          messagebox.showerror("Lỗi","Không có dữ liệu tìm kiếm",parent=self.root)
      else:
          try:
              conn=mysql.connector.connect(host='localhost',username='root',password='',database='nhandangkhuonmat')
              my_cursor=conn.cursor()
              my_cursor.execute("select * from hocsinh where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
              rows=my_cursor.fetchall()         
              if len(rows)!=0:
                  self.student_table.delete(*self.student_table.get_children())
                  for i in rows:
                      self.student_table.insert("",END,values=i)
                  if rows==None:
                      messagebox.showerror("Lỗi","Không thấy dữ liệu",parent=self.root)
                      conn.commit()
              conn.close()
          except Exception as es:
              messagebox.showerror("Lỗi",f"Due To :{str(es)}",parent=self.root)

    def getdata(self,event=""):
      row= self.diemdanh_table.focus()
      noidung=self.diemdanh_table.item(row)
      rows=noidung['values']
      self.var_msv.set(rows[0])
      self.var_hoten.set(rows[1])
      self.var_lop.set(rows[2])
      self.var_thoigian.set(rows[3])
      self.var_ngay.set(rows[4])



    def reset(self):
      self.var_msv.set("")
      self.var_hoten.set("")
      self.var_lop.set("")
      self.var_thoigian.set("")
      self.var_ngay.set("")



if __name__=="__main__":
    root=Tk()
    ojb=Bangdiemdanh(root)
    root.mainloop()
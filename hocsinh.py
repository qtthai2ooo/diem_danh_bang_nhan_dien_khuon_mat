from os import system
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Hocsinh:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Quản lý sinh viên")


        self.var_msv=StringVar()
        self.var_hoten=StringVar()
        self.var_lop=StringVar()
        self.var_khoa=StringVar()
        self.var_gioitinh=StringVar()
        self.var_diachi=StringVar()
        self.var_email=StringVar()
        self.var_sdt=StringVar()
        
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


        title_lbl=Label(bg_img,text="Quản lý sinh viên",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1400,height=600)

        #form chi tiết
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="THÔNG TIN CHI TIẾT HỌC SINH",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=500)

        img_left=Image.open(r"image_app\student_detail.jpg")
        img_left=img_left.resize((450,100),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bg_img=Label(left_frame,image=self.photoimg_left)
        bg_img.place(x=20,y=0,width=600,height=100)

        #form thông tin khóa
        thongtinkhoa_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="THÔNG TIN lỚP HỌC SINH VIÊN",font=("times new roman",12,"bold"))
        thongtinkhoa_frame.place(x=5,y=120,width=650,height=70)


        # khoa
        khoa_label=Label(thongtinkhoa_frame,text="KHOA",font=("times new roman",12,"bold"))
        khoa_label.grid(row=0,column=0,padx=10,sticky=W)

        khoa_combo=ttk.Combobox(thongtinkhoa_frame,textvariable=self.var_khoa,width=25,font=("times new roman",12,"bold"),state="readonly")
        khoa_combo["values"]=("CHỌN KHOA","KHOA HỌC MÁY TÍNH","CÔNG NGHẸ THÔNG TIN")
        khoa_combo.current(0)
        khoa_combo.grid(row=0,column=1,padx=2,pady=10)


        # lớp
        lop_label=Label(thongtinkhoa_frame,text="LỚP",font=("times new roman",12,"bold"))
        lop_label.grid(row=0,column=2,padx=10,sticky=W)

        lop_combo=ttk.Combobox(thongtinkhoa_frame,textvariable=self.var_lop,font=("times new roman",12,"bold"),state="readonly")
        lop_combo["values"]=("CHỌN LỚP","18CE","18IT1","18IT2","18IT3")
        lop_combo.current(0)
        lop_combo.grid(row=0,column=3,padx=2,pady=10)

        #form thông tin sinh vien
        thongtinsinhvien_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="THÔNG TIN SINH VIÊN",font=("times new roman",12,"bold"))
        thongtinsinhvien_frame.place(x=5,y=200,width=650,height=250)

        #msv        
        msv_label=Label(thongtinsinhvien_frame,text="MSV:",font=("times new roman",12,"bold"))
        msv_label.grid(row=0,column=0,padx=10,sticky=W)

        msv_entry=ttk.Entry(thongtinsinhvien_frame,textvariable=self.var_msv,width=20,font=("times new roman",12,"bold"))
        msv_entry.grid(row=0,column=1,padx=10,sticky=W)

        #họ tên        
        hoten_label=Label(thongtinsinhvien_frame,text="HỌ VÀ TÊN:",font=("times new roman",12,"bold"))
        hoten_label.grid(row=0,column=3,padx=10,sticky=W)

        hoten_entry=ttk.Entry(thongtinsinhvien_frame,textvariable=self.var_hoten,width=20,font=("times new roman",12,"bold"))
        hoten_entry.grid(row=0,column=4,padx=10,sticky=W)

        #giới tính
        gioitinh_label=Label(thongtinsinhvien_frame,text="GIỚI TÍNH:",font=("times new roman",12,"bold"))
        gioitinh_label.grid(row=1,column=0,padx=10,sticky=W)

        gioitinh_combo=ttk.Combobox(thongtinsinhvien_frame,textvariable=self.var_gioitinh,font=("times new roman",12,"bold"),state="readonly",width=18)
        gioitinh_combo["values"]=("NAM","NỮ")
        gioitinh_combo.current(0)
        gioitinh_combo.grid(row=1,column=1,padx=2,pady=5)

        #địa chỉ        
        diachi_label=Label(thongtinsinhvien_frame,text="ĐỊA CHỈ:",font=("times new roman",12,"bold"))
        diachi_label.grid(row=1,column=3,padx=10,sticky=W)

        diachi_entry=ttk.Entry(thongtinsinhvien_frame,textvariable=self.var_diachi,width=20,font=("times new roman",12,"bold"))
        diachi_entry.grid(row=1,column=4,padx=10,sticky=W)

        #email        
        email_label=Label(thongtinsinhvien_frame,text="EMAIL:",font=("times new roman",12,"bold"))
        email_label.grid(row=2,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(thongtinsinhvien_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,sticky=W)
        
        #sdt        
        sdt_label=Label(thongtinsinhvien_frame,text="SỐ ĐIỆN THOẠI:",font=("times new roman",12,"bold"))
        sdt_label.grid(row=2,column=3,padx=10,sticky=W)

        sdt_entry=ttk.Entry(thongtinsinhvien_frame,textvariable=self.var_sdt,width=20,font=("times new roman",12,"bold"))
        sdt_entry.grid(row=2,column=4,padx=10,sticky=W)
        
        #btn frame
        btn_frame=Frame(thongtinsinhvien_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=150,width=715,height=70)

        save_btn=Button(btn_frame,width=17,command=self.add_data,text="LƯU",font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,width=17,command=self.update_data,text="SỬA",font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,width=17,command=self.delete_data,text="XÓA",font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,width=17,command=self.reset,text="RESET",font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(thongtinsinhvien_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=185,width=715,height=35)

        savephoto_btn=Button(btn_frame1,width=35,text="LƯU ẢNH",command=self.photo_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        savephoto_btn.grid(row=0,column=0)

        uploadphoto_btn=Button(btn_frame1,width=35,text="SỬA ẢNH",font=("times new roman",12,"bold"),bg="blue",fg="white")
        uploadphoto_btn.grid(row=0,column=1)
        
        #form bảng
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="BẢNG SINH VIÊN",font=("times new roman",12,"bold"))
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

        
        search_entry=ttk.Entry(search_frame,width=17,textvariable=self.serchTxt_var,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,sticky=W)

        search_btn=Button(search_frame,width=12,text="TÌM KIẾM",command=self.search_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        showall_btn=Button(search_frame,width=12,command=self.show_table,text="XEM TẤT CẢ",font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)

        #TABLE frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=80,width=650,height=400)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("msv","hoten","lop","khoa","gioitinh","diachi","email","sdt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("msv",text="MSV")
        self.student_table.heading("hoten",text="HỌ VÀ TÊN")
        self.student_table.heading("khoa",text="KHOA")
        self.student_table.heading("lop",text="LỚP")
        self.student_table.heading("gioitinh",text="GIỚI TÍNH")
        self.student_table.heading("diachi",text="ĐỊA CHỈ")
        self.student_table.heading("email",text="EMAIL")
        self.student_table.heading("sdt",text="SỐ ĐIỆN THOẠI")

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_data)
        self.show_table()



    def add_data(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="nhandangkhuonmat")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO hocsinh values(%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.var_msv.get(),
            self.var_hoten.get(),
            self.var_lop.get(),
            self.var_khoa.get(),
            self.var_gioitinh.get(),
            self.var_diachi.get(),
            self.var_email.get(),
            self.var_sdt.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Thành côg"," Đã thêm dữ liệu",parent=self.root)
            self.show_table()
        except EXCEPTION as es:
            messagebox.showerror("Thất bại",f"Lỗi:{str(es)}",parent=self.root)

    def show_table(self):

            conn=mysql.connector.connect(host="localhost",user="root",password="",database="nhandangkhuonmat")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from hocsinh")
            data=my_cursor.fetchall()
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END,values=i)
            conn.commit()
            conn.close()
    
    
    def get_data(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_msv.set(data[0])
        self.var_hoten.set(data[1])
        self.var_lop.set(data[2])
        self.var_khoa.set(data[3])
        self.var_gioitinh.set(data[4])
        self.var_diachi.set(data[5])
        self.var_email.set(data[6])
        self.var_sdt.set(data[7])

    def update_data(self):
        try:
            update=messagebox.askyesno("sửa","bạn có muốn sửa thông tin",parent=self.root)
            if update>0:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="nhandangkhuonmat")
                my_cursor=conn.cursor()
                my_cursor.execute("UPDATE `hocsinh` SET `hoten`=%s,`lop`=%s,`khoa`=%s,`gioitinh`=%s,`diachi`=%s,`email`=%s,`sdt`=%s WHERE msv=%s",(
                self.var_hoten.get(),
                self.var_lop.get(),
                self.var_khoa.get(),
                self.var_gioitinh.get(),
                self.var_diachi.get(),
                self.var_email.get(),
                self.var_sdt.get(),
                self.var_msv.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Thành công","đã sửa dữ liệu",parent=self.root)
                self.show_table()
            else:
                return
        except EXCEPTION as es:
            messagebox.showerror("Thất bại",f"Lỗi:{str(es)}",parent=self.root)

    def delete_data(self):

            try:
                delete=messagebox.askyesno("XÓA","BẠN CÓ MUỐN XÓA HỌC SINH",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="nhandangkhuonmat")
                    my_cursor=conn.cursor()
                    my_cursor.execute("delete from hocsinh where msv=%s",(self.var_msv.get(),))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("XÓA","ĐÃ XÓA",parent=self.root)
                    self.show_table()
                else:
                    return
            except EXCEPTION as es:
                messagebox.showerror("Thất bại",f"Lỗi:{str(es)}",parent=self.root)


    def reset(self):
        self.var_msv.set("")
        self.var_hoten.set("")
        self.var_lop.set("CHỌN LỚP")
        self.var_khoa.set("CHỌN KHOA")
        self.var_gioitinh.set("NAM")
        self.var_diachi.set("")
        self.var_email.set("")
        self.var_sdt.set("")

    def search_data(self):
      if self.serchTxt_var.get()=="":
          messagebox.showerror("Lỗi","Không có dữ liệu tìm kiếm",parent=self.root)
      else:
          try:
              conn=mysql.connector.connect(host='localhost',username='root',password='',database='nhandangkhuonmat')
              my_cursor=conn.cursor()
              my_cursor.execute("select * from hocsinh where " +self.serch_var.get()+" LIKE '%"+self.serchTxt_var.get()+"%'")
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

    def photo_data(self):
        if self.var_msv=="":
            messagebox.showerror("LỖI","CHƯA CÓ SINH VIÊN",parent=self.root)
        else:
            try:
                photo=messagebox.askyesno("Thêm ảnh","Thêm dữ liêu ảnh sinh viên",parent=self.root)
                if photo>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="nhandangkhuonmat")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from hocsinh")
                    myresult=my_cursor.fetchall()
                    id=0
                    id_msv=self.var_msv.get()
                    for x in myresult:
                        id+=1
                    my_cursor.execute("UPDATE `hocsinh` SET `hoten`=%s,`lop`=%s,`khoa`=%s,`gioitinh`=%s,`diachi`=%s,`email`=%s,`sdt`=%s WHERE msv=%s",(
                    self.var_hoten.get(),
                    self.var_lop.get(),
                    self.var_khoa.get(),
                    self.var_gioitinh.get(),
                    self.var_diachi.get(),
                    self.var_email.get(),
                    self.var_sdt.get(),
                    self.var_msv.get()
                    ))
                    self.get_data()
                    self.reset()

                    conn.commit()
                    conn.close()



                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)

                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                    
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame), (450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="anhchup/MSV."+str(id_msv)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                            cv2.imshow("Crooped Face", face)

                        if cv2.waitKey(1)==13 or int(img_id)==30:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Lưu ảnh","Lưu ảnh thành công")
                    
                else:
                    return
            except EXCEPTION as es:
                messagebox.showerror("Thất bại",f"Lỗi:{str(es)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    ojb=Hocsinh(root)
    root.mainloop()
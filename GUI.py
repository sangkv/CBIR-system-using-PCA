"""
    Created by Sang Kim date 19/12/2018
    Email: sangkimit@gmail.com
"""
# using python3
# import thu vien Gui Python
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
from tkinter.ttk import Combobox
from tkinter import filedialog
import tkinter

# Thư viện xử lý hình ảnh
from PIL import Image, ImageTk

# import module other
import distance
import image_query

# Khai bao cac bien



# Khoi tao doi tuong Gui là root thuộc lass tkinter
root = tkinter.Tk()
root.title("Tra cứu ảnh nội dung")
root.configure(background='gainsboro')

#Kick thuoc cua so
root.geometry("1280x768")
root.resizable(width = True, height=True)



# Menu
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = donothing)
filemenu.add_command(label = "Open", command = donothing)
filemenu.add_command(label = "Save", command = donothing)
filemenu.add_command(label = "Save as...", command = donothing)
filemenu.add_command(label = "Close", command = donothing)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Undo", command = donothing)

editmenu.add_separator()

editmenu.add_command(label = "Cut", command = donothing)
editmenu.add_command(label = "Copy", command = donothing)
editmenu.add_command(label = "Paste", command = donothing)
editmenu.add_command(label = "Delete", command = donothing)
editmenu.add_command(label = "Select All", command = donothing)

menubar.add_cascade(label = "Edit", menu = editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Help Index", command = donothing)
helpmenu.add_command(label = "About...", command = donothing)
menubar.add_cascade(label = "Help", menu = helpmenu)

root.config(menu = menubar)



#Tao labelframe kết quả
labelframe = LabelFrame(root, text = "Kết quả trả về", height = "600", width = 1280,bg = "snow")
labelframe.pack(fill = "x")

#Tạo labelframe combobox
labelframe_combobox = LabelFrame(root, text ="Lựa chọn số ảnh",)
labelframe_combobox.pack(side="left", fill = "y")

#Tạo labelframe button
labelframe_button = LabelFrame(root, text ="Truy vấn ảnh")
labelframe_button.pack(side= "right",fill = "y")



# show image

def show_imquery(seft,path):
	name_image =path
	load = Image.open(name_image)
	render = ImageTk.PhotoImage(load)

	img = Label(seft, image = render,bd="5",bg="red")
	img.image = render
	#Định vị trí hình ảnh cố định
	img.place(x=20,y=50)
	#Định vị vị trí hình ảnh theo các lề, mặc định là top
	#img.pack(side ="left",anchor=CENTER)

	# Hien thi text
	text = Label(seft, text = "Ảnh truy vấn",fg="red")
	text.place(x=30,y=20)
	#text.pack()

def showImg(seft,ds,i,x,y):
	name_image =ds[i][0]
	load = Image.open(name_image)
	render = ImageTk.PhotoImage(load)
	if name_image[0:7] in path:
		img = Label(seft, image = render,bd="5",bg="red")
	else:
		img = Label(seft, image = render,bd="5",bg="green")

	print("Lớp ảnh truy vấn là :",name_image[0:7])
	img.image = render
	#Định vị trí hình ảnh cố định
	img.place(x=x,y=y)
	#Định vị vị trí hình ảnh theo các lề, mặc định là top
	#img.pack(side ="left",anchor=CENTER)
	# Định vị trí dạng lưới (grid)
	# img.grid(row=r, column=c)

# Tạo combobox
v = list(range(1,11))
combo = Combobox(labelframe_combobox,values = v)
combo.set(10)
combo.pack()

def show_image():
	value = combo.get()
	value = int(value)

	# Lệnh trích xuất đặc trưng ảnh truy vấn
	anhtruyvan = image_query.imquery(path)


	# Trả về danh sách với số phần tử = value
	ds = distance.danhsach(value,anhtruyvan)
	# Show ảnh truy vấn
	show_imquery(labelframe,path)
	# show các ảnh là kết quả trả về
	if value <= 5:
		x_im = 250
		y_im = 70
		for i in range(0,value):
			showImg(labelframe,ds,i,x_im,y_im)
			x_im +=200
	elif value >5 and value<=10:
		x_im = 250
		y_im = 70
		for i in range(0,5):
			showImg(labelframe,ds,i,x_im,y_im)
			x_im +=200
		x_im = 250
		y_im = 300
		for i in range(5,value):
			showImg(labelframe,ds,i,x_im,y_im)
			x_im +=200


	msg = messagebox.showinfo("Hello Python", "Hoàn thành truy vấn!")

	

	
'''
# Hàm và button load Database
def loaddb():
	msg = messagebox.showinfo("Load Database", "Đã tải xong CSDL!")

btnLoaddB = Button(labelframe_button, text = "Load Database",relief=RAISED,bg = "red", command = loaddb)
#btnLoaddB.place(x = 100, y = 650)
btnLoaddB.pack(side= "left")
'''
# Hàm và Button load anh truy van
def loadimage():
	path_file = filedialog.askopenfilename()
	msg = messagebox.showinfo("Load Image Query", "Đã tải xong ảnh truy vấn!")
	global path
	path = path_file
	

btnLoadimage = Button(labelframe_button, text = "Load Image Query",relief=RAISED,bg = "green", command = loadimage)
#btnLoadimage.place(x = 250, y = 650)
btnLoadimage.pack(side="top")

# Button truy van
def query():
	msg = messagebox.showinfo("Hello Python", "Hoàn thành truy vấn!")

btnQuery = Button(labelframe_button, text = "Truy vấn",relief=RAISED,bg = "royal blue", command = show_image)
#btnQuery.place(x=400, y = 650)
btnQuery.pack(side="top")

#Ham main
root.mainloop()

from tkinter import *
from PIL import ImageTk, Image #add to requirements.txt

root = Tk()
root.title("A Cool Title")
#add an icon
root.iconbitmap("C:\\Users\\ckenn\\VS Studio\\Python\\tkinter\\img\\static\\img\\picture_photo_image_icon_131252.ico")

#define an image
my_img1 = ImageTk.PhotoImage(Image.open("static/img/sp10.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("static/img/sp11.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("static/img/sp12.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("static/img/sp13.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4]

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0, columnspan=3)

#define button functions
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number >= len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

#create a quit button
button_quit = Button(root, text="Exit Program", command=root.quit)

#create nav buttons
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))

#place quit button
button_back.grid(row=1,column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1,column=2)


root.mainloop()
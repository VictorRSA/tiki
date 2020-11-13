#creaated_by:VIctor NKuna
#Created_on: 10-November-2020



#Resturant Management system tkinter python

from tkinter import*
import time
import datetime

import tkinter.messagebox

root = tkinter.Tk()

root.geometry("1350x750+0+0")

root.configure(background='Cadet Blue')
Top_frame  = Frame(root,bg='Cadet Blue',bd=20,pady=5,relief=RIDGE)
Top_frame.pack(side=TOP)
label_titlte = Label(font=("arial",60),text="Retailer Inventory  Management System",bd=21,bg="Cadet Blue",fg="Cornsilk",justify=CENTER)
label_titlte.pack()

ReceiptCal_F= Frame(root,bg="Powder Blue",bd=10,relief=RIDGE)
ReceiptCal_F.pack(side =RIGHT)

Button_F= Frame(ReceiptCal_F,bg="Powder Blue",bd=3,relief=RIDGE)
Button_F.pack(side=BOTTOM)


Cal_F= Frame(ReceiptCal_F,bg="Powder Blue",bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg="Powder Blue",bd=4,relief=RIDGE)
ReceiptCal_F.pack(side=BOTTOM)

MenuFrame=Frame(root,bg="Cadet Blue",bd=10,relief=RIDGE,width=300,height=400)
MenuFrame.pack(side=LEFT)

Cost_F = Frame(MenuFrame,bg='Powder Blue',bd=4,width=300,height=400)
Cost_F.pack(side=BOTTOM)

"""Drinks_F==in my ticket class=Soccer"""
Soccer_F=Frame(MenuFrame,bg="Powder Blue",bd=10,width=300,height=400)
Soccer_F.pack(side=TOP)


Soccer_F= Frame(MenuFrame,bg='Cadet Blue',width=300,bd=10,relief=RIDGE,height=400)
Soccer_F.pack(side=LEFT)

Cake_F = Frame(MenuFrame,bg='Powder Blue',bd=10,relief=RIDGE)
Cake_F.pack(side=RIGHT)



root.mainloop()
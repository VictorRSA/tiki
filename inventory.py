from tkinter import ttk
import random

from tkinter import *
from tkinter import  messagebox

class Inventory:
    def __init__(self,root):

        self.root =root
        self.root.geometry("1350x800+0+0")
        root.title("Inventory Management System ")
#=========================================FRAME============================================
        MainFrame = Frame(self.root,bd=20,width=1350,height=700,bg="Cadet blue",relief=RIDGE)
        MainFrame.grid()

        LeftFrame = Frame(MainFrame, bd=10, width=560, height=600,padx=10,bg="Cadet blue", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        #
        # RightFrame = Frame(self.root, bd=10, width =712, height=143, padx=5,bg="Powder blue", relief=RIDGE)
        # RightFrame.pack(side=RIGHT)
        #
        # LeftFrame = Frame(LeftFrame,bd=5,width=522,height=200,relief=RIDGE,padx=5)
        # LeftFrame.pack(side=LEFT)

        RightFrame = Frame(MainFrame, bd=10, width =712, height=143, padx=5,bg="Cadet blue", relief=RIDGE)
        RightFrame.pack(side=RIGHT)


        # ================================FRAME for the following widget,Labels,Entry,Widget================================================

        LeftFrame0 = Frame(LeftFrame,bd=5,width=712,height=143,padx=5,bg="Powder blue",relief=RIDGE)
        LeftFrame0.grid(row=0,column=0)

        LeftFrame1 = Frame(LeftFrame,bd=10,width=712,height=170,padx=5,bg="Powder blue",relief=RIDGE)
        LeftFrame1.grid(row=1,column=0)

        LeftFrame2 = Frame(LeftFrame,bd=5,width=712,height=160,padx=5,bg="Powder blue",relief=RIDGE)
        LeftFrame2.grid(row=2,column=0)

        LeftFrame3 = Frame(LeftFrame,bd=5,width=712,height=95,padx=5,bg="Powder blue",relief=RIDGE)
        LeftFrame3.grid(row=3,column=0)



        RightFrame0 = Frame(RightFrame,bd=5,width=522,height=200,padx=5,bg="Powder blue",relief=RIDGE)
        RightFrame0.grid(row=5,column=0)

        RightFrame1 = Frame(RightFrame,bd=10,width=522,height=280,padx=5,bg="Powder blue",relief=RIDGE)
        RightFrame1.grid(row=1,column=0)

        RightFrame2 = Frame(RightFrame,bd=5,width=522,height=95,padx=5,bg="Powder blue",relief=RIDGE)
        RightFrame2.grid(row=2,column=0)


        AcctOpen = StringVar()
        AppDate  = StringVar()
        NextCreditReview = StringVar()
        LastCreditReview=StringVar()
        DateRev = StringVar()



        #================================LeftFrame0===========================================================
        self.lblAcctOpen = Label(LeftFrame0, font=("arial", 10, "bold"), padx=2, pady=2, bg="Powder blue",
                                 text="Account Opened:")
        self.lblAcctOpen.grid(row=0, column=0, sticky=W)

        self.cboAcctOpen = ttk.Combobox(LeftFrame0, textvariable=AcctOpen, width=19, font=("arial", 18, "bold"),
                                        state="randomly")
        self.cboAcctOpen["value"] = ("", "Select an option", "Yes", "No")
        self.cboAcctOpen.current(0)
        self.cboAcctOpen.grid(row=0, column=1, pady=2)

        # self.lblAcctOpen =Label(RightFrame0,font=("arial",10,"bold"),padx=2,pady=2,bg="Powder blue",text="Next Credit Review:",padx=3,pady=2)
        # self.lblAcctOpen.grid(row=0,column=0,sticky=W)

        self.lblAppDate = Label(LeftFrame0, font=("arial", 18, "bold"), padx=2, pady=2, bg="Powder blue",
                                text="Application Date:")
        self.lblAppDate.grid(row=4, column=0, sticky=W)
        self.cboAppDate = ttk.Combobox( LeftFrame0, textvariable=AppDate, width=19, font=("arial", 18, "bold"),
                                       state="randomly")
        self.cboAppDate["value"] = ("", "Student ", "Lecturer", "Admin Stuff")
        self.cboAppDate.current(0)
        self.cboAppDate.grid(row=1, column=1, padx=2)

        self.lblNCreR = Label(LeftFrame0, font=("arial", 18, "bold"), bg="Powder blue", text="Next Credit Review:",
                              padx=2, pady=2)
        self.lblNCreR.grid(row=2, column=0, sticky=W)
        self.cbolCReR = ttk.Combobox(LeftFrame0, textvariable=NextCreditReview, state="randomly",
                                     font=("arial", 18, "bold"), width=19)
        self.cbolCReR["value"] = ("", "Student", "Lecture", "Admin Staff")
        self.cbolCReR.current(0)
        self.cbolCReR.grid(row=3, column=1, pady=2)

        self.lbl_lastcredit = Label(LeftFrame0, font=("arial", 18, "bold"), text="Last Credit Review:", padx=2, pady=2)
        self.lbl_lastcredit.grid(row=3, column=0, sticky=W)
        self.cbo_lastcredit = ttk.Combobox(LeftFrame0, textvariable=LastCreditReview, state='randomly',
                                           font=("arial", 18, "bold"), width=19)

        self.cbo_lastcredit["value"] = ("", "Student ", "Lecturer", "Admin Stuff")
        self.cbo_lastcredit.current(0)
        self.cbo_lastcredit.grid(row=3, column=1, pady=2)

        # make for DATE REVIEW LASTONE

        self.lblDateRev = Label(LeftFrame0, font=("arial", 18, "bold"), text="Date Review:", padx=2, pady=2)
        self.lblDateRev.grid(row=4, column=0, sticky=W)
        self.cboDateRev = ttk.Combobox(LeftFrame0, textvariable=DateRev, state='randomly', font=("arial", 18, "bold"),
                                       width=19)
        self.cboDateRev["value"] = ("", "Student ", "Lecturer", "Admin Stuff")
        self.cboDateRev.current(0)
        self.cboDateRev.grid(row=4, column=1, pady=2)

        #================================LeftFrame1===========================================================
        #================================leftFrame2===========================================================
        #================================LeftFrame3===========================================================
        #================================RIghtFrame0===========================================================

        self.lblAcctOpen =Label(RightFrame0,font=("arial",10,"bold"),padx=2,pady=2,bg="Powder blue",text="Account Opened:")
        self.lblAcctOpen.grid(row=0,column=0,sticky=W)

        self.cboAcctOpen =  ttk.Combobox(RightFrame0,textvariable=AcctOpen,width=19,font=("arial",18,"bold"),state="randomly")
        self.cboAcctOpen["value"]=("","Select an option","Yes","No")
        self.cboAcctOpen.current(0)
        self.cboAcctOpen.grid(row=0,column=1,pady=2)


        # self.lblAcctOpen =Label(RightFrame0,font=("arial",10,"bold"),padx=2,pady=2,bg="Powder blue",text="Next Credit Review:",padx=3,pady=2)
        # self.lblAcctOpen.grid(row=0,column=0,sticky=W)


        self.lblAppDate = Label(RightFrame0, font=("arial", 18, "bold"), padx=2, pady=2, bg="Powder blue",  text="Application Date:")
        self.lblAppDate.grid(row=4,column=0,sticky=W)
        self.cboAppDate=  ttk.Combobox(RightFrame0,textvariable=AppDate,width=19,font=("arial",18,"bold"),state="randomly")
        self.cboAppDate["value"]=("","Student ","Lecturer","Admin Stuff")
        self.cboAppDate.current(0)
        self.cboAppDate.grid(row=1, column=1,padx=2)



        self.lblNCreR = Label(RightFrame0, font=("arial", 18, "bold"), bg="Powder blue",text="Next Credit Review:",padx=2,pady=2)
        self.lblNCreR.grid(row=2,column=0,sticky=W)
        self.cbolCReR = ttk.Combobox(RightFrame0, textvariable=NextCreditReview, state="randomly",font=("arial", 18, "bold"), width=19)
        self.cbolCReR["value"] =("","Student","Lecture","Admin Staff")
        self.cbolCReR.current(0)
        self.cbolCReR.grid(row=3, column=1,pady=2)




        self.lbl_lastcredit= Label(RightFrame0, font=("arial", 18, "bold"),text="Last Credit Review:", padx=2, pady=2)
        self.lbl_lastcredit.grid(row=3, column=0, sticky=W)
        self.cbo_lastcredit =ttk.Combobox(RightFrame0,textvariable=LastCreditReview,state='randomly',font=("arial",18,"bold"),width=19)

        self.cbo_lastcredit["value"] = ("", "Student ", "Lecturer", "Admin Stuff")
        self.cbo_lastcredit.current(0)
        self.cbo_lastcredit.grid(row=3, column=1,pady=2)

    #make for DATE REVIEW LASTONE


        self.lblDateRev= Label(RightFrame0, font=("arial", 18, "bold"),text="Date Review:", padx=2, pady=2)
        self.lblDateRev.grid(row=4, column=0, sticky=W)
        self.cboDateRev =ttk.Combobox(RightFrame0,textvariable=DateRev,state='randomly',font=("arial",18,"bold"),width=19)
        self.cboDateRev["value"] = ("", "Student ", "Lecturer", "Admin Stuff")
        self.cboDateRev.current(0)
        self.cboDateRev.grid(row=4, column=1,pady=2)



        #================================Text,Labels,ENtry,Widget================================================
        self.txtReciept=Text(RightFrame1,height=20,width=71,font=("arial",9,"bold"))
        self.txtReciept.grid(row=0,column=0)
       #================================Buttons RightFrame2==================================================================
        self.btnTotal =Button(RightFrame2,padx=18,pady=2,bd=4,fg="black",font=("arial",9,"bold"),
                              bg="Powder blue",text="Total").grid(row=0,column=0)

        self.btnReset =Button(RightFrame2,padx=18,pady=2,bd=4,fg="black",font=("arial",9,"bold"),width=9,
                              bg="Powder blue",text="Reset").grid(row=0,column=1)

        self.btnExit = Button(RightFrame2, padx=120, pady=2, bd=4, fg="black", font=("arial", 9, "bold"), width=9,
                               bg="Powder blue", text="Exit").grid(row=0, column=1)

      #I see the inheritance of Frames,widget,main RIGHT,LEFT PACK AND USE THEM TO POPULATE SUB FRMAE WITH THEM



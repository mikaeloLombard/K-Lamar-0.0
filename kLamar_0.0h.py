from tkinter import *
from tkinter import ttk
import shutil
import os
from tkinter import messagebox
import csv
import datetime as dt

date = dt.date.today()

# Set tkinter-variables to use them with widgets to get the values



root = Tk()

# App Name
root.title("K-Lamar 0.0    Address Research Organizer Tool")

# Window Size

root.geometry('{}x{}'.format(564, 290))
root.resizable(width=False, height=False)

# K-lamar Icon

root.iconbitmap(default='kala.ico')


# Create frame

frame = Frame(root)


# Ttk Style

style = ttk.Style()

# GUI style

ttk.Style().theme_use('clam')
# Top Label
# background image

background_image = PhotoImage(file="test2.gif")
Label(frame, bg="silver", text="Web Address Organizer Research Tool", fg="white", font="italic", width=565,
           height=20, relief=SUNKEN, image=background_image).grid(row=1, column=0, sticky=W, padx=0)


# Data processes


def newgroup():

    file = open("%s.csv" % (strEnt.get()), "a")
    file.writelines(" , , , \n")
    file.writelines("%s , %s, %s" % (linkNam.get(), desInfo.get(), date ))
    linkNam.delete(0, END)
    desInfo.delete(0, END)
    file.close()


def createfile():
    # Creates the file, also disables and activates buttons and entry.
    shutil.copy ("originalFile.csv", ("%s.csv" % (strEnt.get ())))
    file = open("%s.csv" % (strEnt.get()), "a")
    nameButton['state'] = 'disabled'
    linkButton['state'] = 'normal'



def writefile():

    file = open("%s.csv" % (strEnt.get()), "a")
    file.write ('URL \t \t, Comments \t \t , Access Date \n')
    file.write("%s,%s, %s \n" % (linkNam.get(), desInfo.get(), date ))
    linkNam.delete(0, END)
    desInfo.delete(0, END)
    file.close()


def reset():
    nameButton['state'] = 'normal'
    linkNam.delete(0, END)
    desInfo.delete(0, END)
    strEnt.delete(0,END)
    linkButton['state'] = 'disabled'
    

def ending():
    global root
    root.destroy()


# Reset Button

resetButton = Button(frame, text="Reset", width=5)
resetButton.grid(row=12, column=0, sticky=W, padx=15)
resetButton.bind("<Button-1>", lambda x: reset())

# Enter File Name

Label (frame, text="").grid (row=2, column=0, sticky=W, padx=4)
Label (frame, text="Project Title:").grid (row=3, column=0, sticky=W, padx=3)
strEnt = Entry (frame, width=27)
strEnt.grid (row=4, column=0, sticky=W, padx=6)

# Name File Button

nameButton = Button (frame, text="Create", width=8)
nameButton.grid(row=4, column=0, sticky=W, padx=180)
nameButton.bind("<Button-1>", lambda x: createfile())

# Pasted Link Entry
Label(frame, text="").grid (row=5, column=0, sticky=W, padx=4)
Label(frame, text="Enter Link:").grid (row=6, column=0, sticky=W, padx=3)
linkNam = Entry(frame, width=60)
linkNam.grid(row=6, column=0, sticky=N, padx=3, pady=3)




# Submit Button

linkButton = Button (frame, text="Submit", width=8)
linkButton.grid(row=6, column=0, sticky=E, padx=18)
linkButton.bind("<Button-1>", lambda x: writefile())
linkButton['state'] = 'disabled'


# Comment or description entry

Label(frame, text="").grid(row=7,column=0, sticky=W, padx=4)
Label(frame, text="Comment:").grid(row=8, column=0, sticky=W, padx=3)
desInfo = Entry(frame, width=60)
desInfo.grid(row=8, column=0, sticky=N, padx=100, pady=3)


# Separation for grouping (Empty Row)

Label(frame, text="").grid(row=9,column=0, sticky=W, padx=4)
Label(frame, text= "Together or Apart:").grid(row=10, column=0, sticky=E, padx=9)
empRow = Radiobutton(frame, text="Separated", value=1)
empRow.grid(row=11, column=0, sticky=E, padx=18)
empRow.bind("<Button-1>", lambda x: newgroup())
empRow2 = Radiobutton(frame, text="Group", value=2)
empRow2.grid(row=12, column=0, sticky=NE, padx=37)


# Quit Button

endB = Button(frame, text="Quit", width=4)
endB.grid(row=12, column=0, sticky=W, padx=70)
endB.bind("<Button-1>", lambda x: ending())


frame.grid()
root.mainloop()


# List of things to do:

#  *Also make the link address active in the file to be used (Tkinter Tables may be needed)
#  *Drop-down menus may be needed for other functions.
#  *Create a file in a dedicated directory.
#  *Give user the option of creating the location of repository directory.


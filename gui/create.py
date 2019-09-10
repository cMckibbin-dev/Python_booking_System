from tkinter import *
root = Tk()

options = [
    "Please select event type",
    "Conference",
    "Party",
    "Wedding"
]

bandOptions = [
    "Please select band",
    "Lil' Febrezey",
    "Prawn Mendes",
    "AB/CD"
]


yesno = IntVar()

variable = StringVar(root)
variable.set(options[0])  # default value
bandVariable = StringVar(root)
bandVariable.set(options[0])  # default value
bc = IntVar()
bcs = StringVar()

#  Band selection options
def boptions():
    bandNameLbl.grid(row=10, column=1)
    bandName.grid(row=10, column=2, padx=(0, 20), sticky=NSEW)

    bandCostLbl.grid(row=11, column=1)
    bandCostDisplay.grid(row=11, column=2, padx=(0, 20), sticky='w')

    if bandVariable.get() == "Lil' Febrezey":
        bcs.set("£{0}".format(100))
    elif bandVariable.get() == 'Prawn Mendes':
        bcs.set("£{0}".format(250))
    elif bandVariable.get() == 'AB/CD':
        bcs.set("£{0}".format(500))
    else:
        bcs.set("£{0}".format(0))


#  Enable save button function
def enablesavebtn(*args):
    if True:
        saveBtn.config(state='normal')


# Funtion to hide widgets(1 = conference, 2=party, 3=wedding)
def hidewidgets(int):
    if int == 1:
        bandNameLbl.grid_remove()
        bandName.grid_remove()
        bandCostLbl.grid_remove()
        bandCostDisplay.grid_remove()
        noOfRoomsLbl.grid_remove()
        noOfRoomsEntry.grid_remove()
    elif int == 2:
        companyLbl.grid_remove()
        companyEntry.grid_remove()
        noOfDaysLbl.grid_remove()
        noOfDaysEntry.grid_remove()
        projectorLbl.grid_remove()
        projectorCheck.grid_remove()
        noOfRoomsLbl.grid_remove()
        noOfRoomsEntry.grid_remove()
    elif int == 3:
        companyLbl.grid_remove()
        companyEntry.grid_remove()
        noOfDaysLbl.grid_remove()
        noOfDaysEntry.grid_remove()
        projectorLbl.grid_remove()
        projectorCheck.grid_remove()


#  Function to detect which option is selected in event list
def selectedvalue(*args):

    if variable.get() == 'Please select event type' or bandVariable.get() == 'Please select band':
        saveBtn.config(state=DISABLED)
    elif variable.get() == 'Conference':
        enablesavebtn()

        companyLbl.grid(row=10, column=1)
        companyEntry.grid(row=10, column=2, padx=(0, 20))

        noOfDaysLbl.grid(row=11, column=1)
        noOfDaysEntry.grid(row=11, column=2, padx=(0, 20))

        projectorLbl.grid(row=12, column=1)
        projectorCheck.grid(row=12, column=2, padx=(0, 20), sticky='w')

        hidewidgets(1)

    elif variable.get() == 'Party':
        enablesavebtn()
        boptions()

        hidewidgets(2)

    elif variable.get() == 'Wedding':
        enablesavebtn()
        boptions()

        noOfRoomsLbl.grid(row=12, column=1)
        noOfRoomsEntry.grid(row=12, column=2)

        hidewidgets(3)


# Widgets
label = Label(root, text="Create New Booking", font="Ariel, 16", height=2)

eventTypeLbl = Label(root, text="Select Event Type:", font="Ariel, 12", anchor='e', width=20)
eventType = OptionMenu(root, variable, *options, command=selectedvalue)


noGuestsLbl = Label(root, text="Number of Guests:", font="Ariel, 12", anchor='e', width=20)
noGuestsEntry = Entry(root)

nameOfContactLbl = Label(root, text="Name of Contact:", font="Ariel, 12", anchor='e', width=20)
nameOfContactEntry = Entry(root)

addressLbl = Label(root, text="Full Address of Contact:", font="Ariel, 12", anchor='e', width=20)
addressEntry = Entry(root)

contactNumberLbl = Label(root, text="Contact Number:", font="Ariel, 12", anchor='e', width=20)
contactNumberEntry = Entry(root)

roomNoLbl = Label(root, text="Event Room Number:", font="Ariel, 12", anchor='e', width=20)
roomNoEntry = Entry(root)

dateOfEventLbl = Label(root, text="Date of Event:", font="Ariel, 12", anchor='e', width=20)
dateOfEventEntry = Entry(root)

dateOfBookingLbl = Label(root, text="Date of Booking:", font="Ariel, 12", anchor='e', width=20)
dateOfBookingEntry = Entry(root)

companyLbl = Label(root, text="Company Name:", font="Ariel, 12", anchor='e', width=20)
companyEntry = Entry(root)

noOfDaysLbl = Label(root, text="Number of Days:", font="Ariel, 12", anchor='e', width=20)
noOfDaysEntry = Entry(root)

projectorLbl = Label(root, text="Projector Required?:", font="Ariel, 12", anchor='e', width=20)
projectorCheck = Checkbutton(root, variable=yesno)

costPerHeadLbl = Label(root, text="Cost Per Head:", font="Ariel, 12", anchor='e', width=20)
costPerHeadDisplay = Label(root, text="£000", font="Ariel, 12", anchor='e', width=20)

bandNameLbl = Label(root, text="Select Band:", font="Ariel, 12", anchor='e', width=20)
bandName = OptionMenu(root, bandVariable, *bandOptions, command=selectedvalue)

bandCostLbl = Label(root, text="Band Cost:", font="Ariel, 12", anchor='e', width=20)
bandCostDisplay = Label(root,  font="Ariel, 12", textvariable=bcs, anchor='e', width=20)

noOfRoomsLbl = Label(root, text="Number of Rooms:", font="Ariel, 12", anchor='e', width=20)
noOfRoomsEntry = Entry(root)

f1 = Frame(root)

backBtn = Button(f1, text="Back", width=10, height=2)
clearBtn = Button(f1, text="Clear", width=10, height=2)
saveBtn = Button(f1, text="Save", width=10, height=2)

# Positioning
label.grid(row=0, column=0, columnspan=5, pady=(10, 20))

eventType.grid(row=2, column=2, sticky=NSEW, pady=(0, 25), padx=(0, 20))
eventTypeLbl.grid(row=2, column=1, pady=(0, 25))

noGuestsLbl.grid(row=3, column=1)
noGuestsEntry.grid(row=3, column=2, padx=(0, 20))

nameOfContactLbl.grid(row=4, column=1)
nameOfContactEntry.grid(row=4, column=2, padx=(0, 20))

addressLbl.grid(row=5, column=1)
addressEntry.grid(row=5, column=2, padx=(0, 20))

contactNumberLbl.grid(row=6, column=1)
contactNumberEntry.grid(row=6, column=2, padx=(0, 20))

roomNoLbl.grid(row=7, column=1)
roomNoEntry.grid(row=7, column=2, padx=(0, 20))

dateOfEventLbl.grid(row=8, column=1)
dateOfEventEntry.grid(row=8, column=2, padx=(0, 20))

dateOfBookingLbl.grid(row=9, column=1)
dateOfBookingEntry.grid(row=9, column=2, padx=(0, 20))

costPerHeadLbl.grid(row=13, column=1)
costPerHeadDisplay.grid(row=13, column=2, padx=(0, 20), sticky='w')

f1.grid(row=14, columnspan=3, column=1, pady=(40, 40))

backBtn.pack(side="left", padx=(0, 5))
backBtn.config(bg='snow', highlightbackground='snow', state=DISABLED)
clearBtn.pack(side="left")
clearBtn.config(bg='salmon', highlightbackground='salmon', fg='white')
saveBtn.pack(side="left", padx=(5, 0))
saveBtn.config(bg='SteelBlue1', highlightbackground='SteelBlue1', fg='white')




root.mainloop()

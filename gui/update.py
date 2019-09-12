from tkinter import *


class UpdateConferenceUI:


    def __init__(self, root, eventtype):

        self.eventtype = eventtype
        self.root = root

        self.bandOptions = [
            "Please select band",
            "Lil' Febrezey",
            "Prawn Mendes",
            "AB/CD"
        ]

        self.yesno = IntVar()

        self.variable = StringVar(self.root)

        self.bandVariable = StringVar(self.root)
        self.bandVariable.set(self.bandOptions[0])  # default value
        self.bc = IntVar()
        self.bcs = StringVar()
        self.titleString = StringVar()

        # Widgets

        self.label = Label(self.root, textvariable=self.titleString, font="Ariel, 16", height=2)

        self.noGuestsLbl = Label(self.root, text="Number of Guests:", font="Ariel, 12", anchor='e', width=20)
        self.noGuestsEntry = Entry(self.root)

        self.nameOfContactLbl = Label(self.root, text="Name of Contact:", font="Ariel, 12", anchor='e', width=20)
        self.nameOfContactEntry = Entry(self.root)

        self.addressLbl = Label(self.root, text="Full Address of Contact:", font="Ariel, 12", anchor='e', width=20)
        self.addressEntry = Entry(self.root)

        self.contactNumberLbl = Label(self.root, text="Contact Number:", font="Ariel, 12", anchor='e', width=20)
        self.contactNumberEntry = Entry(self.root)

        self.roomNoLbl = Label(self.root, text="Event Room Number:", font="Ariel, 12", anchor='e', width=20)
        self.roomNoEntry = Entry(self.root)

        self.dateOfEventLbl = Label(self.root, text="Date of Event:", font="Ariel, 12", anchor='e', width=20)
        self.dateOfEventEntry = Entry(self.root)

        self.dateOfBookingLbl = Label(self.root, text="Date of Booking:", font="Ariel, 12", anchor='e', width=20)
        self.dateOfBookingEntry = Entry(self.root)

        self.companyLbl = Label(self.root, text="Company Name:", font="Ariel, 12", anchor='e', width=20)
        self.companyEntry = Entry(self.root)

        self.noOfDaysLbl = Label(self.root, text="Number of Days:", font="Ariel, 12", anchor='e', width=20)
        self.noOfDaysEntry = Entry(self.root)

        self.projectorLbl = Label(self.root, text="Projector Required?:", font="Ariel, 12", anchor='e', width=20)
        self.projectorCheck = Checkbutton(self.root, variable=self.yesno)

        self.costPerHeadLbl = Label(self.root, text="Cost Per Head:", font="Ariel, 12", anchor='e', width=20)
        self.costPerHeadDisplay = Label(self.root, text="£000", font="Ariel, 12", anchor='e', width=20)

        self.bandNameLbl = Label(self.root, text="Select Band:", font="Ariel, 12", anchor='e', width=20)
        self.bandName = OptionMenu(self.root, self.bandVariable, *self.bandOptions, command=self.boptions)

        self.bandCostLbl = Label(self.root, text="Band Cost:", font="Ariel, 12", anchor='e', width=20)
        self.bandCostDisplay = Label(self.root, font="Ariel, 12", textvariable=self.bcs, anchor='e', width=20)

        self.noOfRoomsLbl = Label(self.root, text="Number of Rooms:", font="Ariel, 12", anchor='e', width=20)
        self.noOfRoomsEntry = Entry(self.root)

        self.f1 = Frame(self.root)

        self.backBtn = Button(self.f1, text="Back", width=10, height=2)
        self.clearBtn = Button(self.f1, text="Clear", width=10, height=2)
        self.saveBtn = Button(self.f1, text="Save", width=10, height=2)

        self.mainui()
        if self.eventtype == 'conference':
            self.conferenceui()

        elif self.eventtype == 'party':
            self.partyui()

        elif self.eventtype == 'wedding':
            self.weddingui()




        #  Band selection options
    def boptions(self, *args):
        print("loaded boptions")
        self.bandNameLbl.grid(row=10, column=1)
        self.bandName.grid(row=10, column=2, padx=(0, 20), sticky=NSEW)

        self.bandCostLbl.grid(row=11, column=1)
        self.bandCostDisplay.grid(row=11, column=2, padx=(0, 20), sticky='w')
        print(str(self.bandVariable))
        if self.bandVariable.get() == "Lil' Febrezey":

            self.bcs.set("£{0}".format(100))
            print(str(self.bcs))
        elif self.bandVariable.get() == 'Prawn Mendes':
            self.bcs.set("£{0}".format(250))
            print(str(self.bcs))
        elif self.bandVariable.get() == 'AB/CD':
            self.bcs.set("£{0}".format(500))
            print(str(self.bcs))
        else:
            self.bcs.set("£{0}".format(0))

    #  Enable save button function
    def enablesavebtn(self, *args):
        if True:
            self.saveBtn.config(state='normal')

    # Function to hide widgets(1 = conference, 2=party, 3=wedding)
    def hidewidgets(self, eventtype):
        if eventtype == 'conference':
            self.bandNameLbl.grid_remove()
            self.bandName.grid_remove()
            self.bandCostLbl.grid_remove()
            self.bandCostDisplay.grid_remove()
            self.noOfRoomsLbl.grid_remove()
            self.noOfRoomsEntry.grid_remove()
        elif eventtype == 'party':
            self.companyLbl.grid_remove()
            self.companyEntry.grid_remove()
            self.noOfDaysLbl.grid_remove()
            self.noOfDaysEntry.grid_remove()
            self.projectorLbl.grid_remove()
            self.projectorCheck.grid_remove()
            self.noOfRoomsLbl.grid_remove()
            self.noOfRoomsEntry.grid_remove()
        elif eventtype == 'wedding':
            self.companyLbl.grid_remove()
            self.companyEntry.grid_remove()
            self.noOfDaysLbl.grid_remove()
            self.noOfDaysEntry.grid_remove()
            self.projectorLbl.grid_remove()
            self.projectorCheck.grid_remove()

    def mainui (self):
        self.noGuestsLbl.grid(row=3, column=1)
        self.noGuestsEntry.grid(row=3, column=2, padx=(0, 20))

        self.nameOfContactLbl.grid(row=4, column=1)
        self.nameOfContactEntry.grid(row=4, column=2, padx=(0, 20))

        self.addressLbl.grid(row=5, column=1)
        self.addressEntry.grid(row=5, column=2, padx=(0, 20))

        self.contactNumberLbl.grid(row=6, column=1)
        self.contactNumberEntry.grid(row=6, column=2, padx=(0, 20))

        self.roomNoLbl.grid(row=7, column=1)
        self.roomNoEntry.grid(row=7, column=2, padx=(0, 20))

        self.dateOfEventLbl.grid(row=8, column=1)
        self.dateOfEventEntry.grid(row=8, column=2, padx=(0, 20))

        self.dateOfBookingLbl.grid(row=9, column=1)
        self.dateOfBookingEntry.grid(row=9, column=2, padx=(0, 20))

        self.costPerHeadLbl.grid(row=13, column=1)
        self.costPerHeadDisplay.grid(row=13, column=2, padx=(0, 20), sticky='w')

        self.f1.grid(row=14, columnspan=3, column=1, pady=(40, 40))

        self.backBtn.pack(side="left", padx=(0, 5))
        self.backBtn.config(bg='snow', highlightbackground='snow', state=DISABLED)
        self.clearBtn.pack(side="left")
        self.clearBtn.config(bg='salmon', highlightbackground='salmon', fg='white')
        self.saveBtn.pack(side="left", padx=(5, 0))
        self.saveBtn.config(bg='SteelBlue1', highlightbackground='SteelBlue1', fg='white')

    def conferenceui(self):
        self.titleString.set("Update Conference")

        self.label.grid(row=0, column=0, columnspan=5, pady=(10, 20))

        self.enablesavebtn()

        self.companyLbl.grid(row=10, column=1)
        self.companyEntry.grid(row=10, column=2, padx=(0, 20))

        self.noOfDaysLbl.grid(row=11, column=1)
        self.noOfDaysEntry.grid(row=11, column=2, padx=(0, 20))

        self.projectorLbl.grid(row=12, column=1)
        self.projectorCheck.grid(row=12, column=2, padx=(0, 20), sticky='w')

        self.hidewidgets('conference')

    def partyui(self):
        self.titleString.set("Update Party")
        self.label.grid(row=0, column=0, columnspan=5, pady=(10, 20))

        self.enablesavebtn()
        self.boptions()

        self.hidewidgets('party')

    def weddingui(self):
        self.titleString.set("Update Wedding")
        self.label.grid(row=0, column=0, columnspan=5, pady=(10, 20))

        self.enablesavebtn()
        self.boptions()

        self.noOfRoomsLbl.grid(row=12, column=1)
        self.noOfRoomsEntry.grid(row=12, column=2)

        self.hidewidgets('wedding')


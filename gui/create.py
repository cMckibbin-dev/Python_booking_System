from tkinter import *
import tkinter.ttk as ttk
from Data_Access import data_access
from classes import *
import gui.top_level_functions as tlf


class CreateUI:


    def __init__(self, root):

        self.root = root
        # Event type options
        self.options = [
            "Please select event type",
            "Conference",
            "Party",
            "Wedding"
        ]
        # Band name options
        self.bandOptions = [
            "Please select band",
            "Lil' Febrezey",
            "Prawn Mendes",
            "AB/CD"
        ]
        # Conference room options
        self.conferenceRooms = [
            "Please select room",
            "A",
            "B",
            "C"
        ]

        # Party room options
        self.partyRooms = [
            "Please select room",
            "D",
            "E",
            "F",
            "G"
        ]

        # Wedding room options
        self.weddingRooms = [
            "Please select room",
            "H",
            "I"
        ]
        self.yesno = IntVar()

        # Variables for labels, prices and option menus.
        self.variable = StringVar(self.root)
        self.variable.set(self.options[0])  # default value
        self.bandVariable = StringVar(self.root)
        self.bandVariable.set(self.options[0])  # default value
        self.roomVariable = StringVar(self.root)
        self.roomVariable.set(self.options[0])  # default value
        self.bc = IntVar()
        self.bcs = StringVar()

        # Widgets
        self.label = Label(self.root, text="Create New Booking", font="Ariel, 16", height=2)

        self.eventTypeLbl = Label(self.root, text="Select Event Type:", font="Ariel, 12", anchor='e', width=20)
        self.eventType = OptionMenu(self.root, self.variable, *self.options, command=self.selectedvalue)

        self.noGuestsLbl = Label(self.root, text="Number of Guests:", font="Ariel, 12", anchor='e', width=20)
        self.noGuestsEntry = Entry(self.root)

        self.nameOfContactLbl = Label(self.root, text="Name of Contact:", font="Ariel, 12", anchor='e', width=20)
        self.nameOfContactEntry = Entry(self.root)

        self.addressLbl = Label(self.root, text="Full Address of Contact:", font="Ariel, 12", anchor='e', width=20)
        self.addressEntry = Entry(self.root)

        self.contactNumberLbl = Label(self.root, text="Contact Number:", font="Ariel, 12", anchor='e', width=20)
        self.contactNumberEntry = Entry(self.root)

        self.roomNoLbl = Label(self.root, text="Event Room Number:", font="Ariel, 12", anchor='e', width=20)
        # TODO Finish the room logic and selection options.
        self.roomNoEntryConference = OptionMenu(self.root, self.roomVariable, *self.conferenceRooms)
        self.roomNoEntryParty = OptionMenu(self.root, self.roomVariable, *self.partyRooms)
        self.roomNoEntryWedding = OptionMenu(self.root, self.roomVariable, *self.weddingRooms)

        self.dateOfEventLbl = Label(self.root, text="Date of Event:", font="Ariel, 12", anchor='e', width=20)
        self.dateOfEventEntry = Entry(self.root)
        self.dateOfEventEntry.bind('<Button-1>', lambda event: tlf.date_top_level(event, self.dateOfEventEntry))

        self.dateOfBookingLbl = Label(self.root, text="Date of Booking:", font="Ariel, 12", anchor='e', width=20)
        # TODO Change lbl2 to pull the date from system.
        self.dateOfBookingLbl2 = Label(self.root, text="Date will go here", font="Ariel, 12", anchor='e', width=20)

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

        # This frame houses the buttons at the bottom of the form
        f1 = Frame(self.root)

        self.backBtn = Button(f1, text="Back", width=10, height=2)
        self.clearBtn = Button(f1, text="Clear", width=10, height=2)
        self.saveBtn = Button(f1, text="Save", width=10, height=2, command=self.saveconference)

        # Positioning
        self.label.grid(row=0, column=0, columnspan=5, pady=(10, 20))

        self.eventType.grid(row=2, column=2, sticky=NSEW, pady=(0, 25), padx=(0, 20))
        self.eventTypeLbl.grid(row=2, column=1, pady=(0, 25))

        self.noGuestsLbl.grid(row=3, column=1)
        self.noGuestsEntry.grid(row=3, column=2, padx=(0, 20))

        self.nameOfContactLbl.grid(row=4, column=1)
        self.nameOfContactEntry.grid(row=4, column=2, padx=(0, 20))

        self.addressLbl.grid(row=5, column=1)
        self.addressEntry.grid(row=5, column=2, padx=(0, 20))

        self.contactNumberLbl.grid(row=6, column=1)
        self.contactNumberEntry.grid(row=6, column=2, padx=(0, 20))

        self.roomNoLbl.grid(row=7, column=1)

        self.dateOfEventLbl.grid(row=8, column=1)
        self.dateOfEventEntry.grid(row=8, column=2, padx=(0, 20))

        self.dateOfBookingLbl.grid(row=9, column=1)
        self.dateOfBookingLbl2.grid(row=9, column=2, padx=(0, 20))

        self.costPerHeadLbl.grid(row=13, column=1)
        self.costPerHeadDisplay.grid(row=13, column=2, padx=(0, 20), sticky='w')

        f1.grid(row=14, columnspan=3, column=1, pady=(40, 40))
        # The buttons are packed into the frame and they have a "highlightbackground" field so they will work on a Mac.
        # "highlightbackground" is not needed for windows.
        self.backBtn.pack(side="left", padx=(0, 5))
        self.backBtn.config(bg='snow', highlightbackground='snow', state=DISABLED)
        self.clearBtn.pack(side="left")
        self.clearBtn.config(bg='salmon', highlightbackground='salmon', fg='white')
        self.saveBtn.pack(side="left", padx=(5, 0))
        self.saveBtn.config(bg='SteelBlue1', highlightbackground='SteelBlue1', fg='white')

    #  Band selection options
    def boptions(self, *args):
        # bcs = band cost string, and is used to display the cost of the band selected.
        # bc = band cost
        self.bandNameLbl.grid(row=10, column=1)
        self.bandName.grid(row=10, column=2, padx=(0, 20), sticky=NSEW)

        self.bandCostLbl.grid(row=11, column=1)
        self.bandCostDisplay.grid(row=11, column=2, padx=(0, 20), sticky='w')

        if self.bandVariable.get() == "Lil' Febrezey":
            self.bcs.set("£{0}".format(100))
        elif self.bandVariable.get() == 'Prawn Mendes':
            self.bcs.set("£{0}".format(250))
        elif self.bandVariable.get() == 'AB/CD':
            self.bcs.set("£{0}".format(500))
        else:
            self.bcs.set("£{0}".format(0))

    #  Enable save button function
    def enablesavebtn(self, *args):
        if True:
            self.saveBtn.config(state='normal')

    def saveconference(self):
        db = data_access
        c = Conference(self.noGuestsEntry.get(), self.nameOfContactEntry.get(), self.addressEntry.get(),
                       # TODO Need to find a way to pull the value from the room drop down list
                       self.contactNumberEntry.get(), self.roomNoEntryConference.getvar(), self.dateOfEventEntry.get(),
                       self.companyEntry.get(),
                       self.noOfDaysEntry.get(), self.projectorCheck.getboolean(self), datetime.date,
                       self.noGuestsEntry.get())
        db.DBAccess.insert_conference(c)

    # Function to hide widgets(conference, party, wedding)
    def hidewidgets(self, eventtype):
        if eventtype == 'conference':
            self.bandNameLbl.grid_remove()
            self.bandName.grid_remove()
            self.bandCostLbl.grid_remove()
            self.bandCostDisplay.grid_remove()
            self.noOfRoomsLbl.grid_remove()
            self.noOfRoomsEntry.grid_remove()
            self.roomNoEntryParty.grid_remove()
            self.roomNoEntryWedding.grid_remove()
        elif eventtype == 'party':
            self.companyLbl.grid_remove()
            self.companyEntry.grid_remove()
            self.noOfDaysLbl.grid_remove()
            self.noOfDaysEntry.grid_remove()
            self.projectorLbl.grid_remove()
            self.projectorCheck.grid_remove()
            self.noOfRoomsLbl.grid_remove()
            self.noOfRoomsEntry.grid_remove()
            self.roomNoEntryConference.grid_remove()
            self.roomNoEntryWedding.grid_remove()
        elif eventtype == 'wedding':
            self.companyLbl.grid_remove()
            self.companyEntry.grid_remove()
            self.noOfDaysLbl.grid_remove()
            self.noOfDaysEntry.grid_remove()
            self.projectorLbl.grid_remove()
            self.projectorCheck.grid_remove()
            self.roomNoEntryParty.grid_remove()
            self.roomNoEntryConference.grid_remove()

    #  Function to detect which option is selected in event list
    def selectedvalue(self, *args):

        if self.variable.get() == 'Please select event type' or self.bandVariable.get() == 'Please select band':
            self.saveBtn.config(state=DISABLED)
        elif self.variable.get() == 'Conference':
            # This displays all necessary widgets and calls the function to hide the ones that aren't needed.
            self.enablesavebtn()

            self.roomNoEntryConference.grid(row=7, column=2, padx=(0, 20))
            self.companyLbl.grid(row=10, column=1)
            self.companyEntry.grid(row=10, column=2, padx=(0, 20))

            self.noOfDaysLbl.grid(row=11, column=1)
            self.noOfDaysEntry.grid(row=11, column=2, padx=(0, 20))

            self.projectorLbl.grid(row=12, column=1)
            self.projectorCheck.grid(row=12, column=2, padx=(0, 20), sticky='w')

            self.hidewidgets('conference')



        elif self.variable.get() == 'Party':
            # This displays all necessary widgets and calls the function to hide the ones that aren't needed.
            self.roomNoEntryParty.grid(row=7, column=2, padx=(0, 20))
            self.enablesavebtn()
            self.boptions()
            self.hidewidgets('party')

        elif self.variable.get() == 'Wedding':
            # This displays all necessary widgets and calls the function to hide the ones that aren't needed.
            self.roomNoEntryWedding.grid(row=7, column=2, padx=(0, 20))
            self.enablesavebtn()
            self.boptions()
            self.noOfRoomsLbl.grid(row=12, column=1)
            self.noOfRoomsEntry.grid(row=12, column=2)

            self.hidewidgets('wedding')

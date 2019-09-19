from tkinter import *
import tkinter as tk
import classes
from Data_Access import data_access
from Data_Access.data_access import DBAccess
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
        # bc = to band cost and is used to create a value which can be stored in the database
        # bcs = band cost string and is used to display the band cost to the user
        self.bc = IntVar()
        self.bcs = StringVar()
        # pCheck = projector check box and is used to store whether or not the user has checked the projector checkbox
        self.pCheck = tk.BooleanVar()

        # Widgets - All widgets are listed with their label and their input together.
        self.label = Label(self.root, text="Create New Booking", font="Ariel, 16", height=2)

        # Below is the event type lbl
        # And below that again is the event type option menu
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
        self.roomNoEntryConference = OptionMenu(self.root, self.roomVariable, *self.conferenceRooms)
        self.roomNoEntryParty = OptionMenu(self.root, self.roomVariable, *self.partyRooms)
        self.roomNoEntryWedding = OptionMenu(self.root, self.roomVariable, *self.weddingRooms)
        self.dateOfEventLbl = Label(self.root, text="Date of Event:", font="Ariel, 12", anchor='e', width=20)

        # Date of event entry has a calendar function bound to it. This creates a popup where the user is able
        # to select a date.
        self.dateOfEventEntry = Entry(self.root)
        self.dateOfEventEntry.bind('<Button-1>', lambda event: tlf.date_top_level(event, self.dateOfEventEntry))

        # the date of booking is set to the current date of the computer.
        self.dateOfBookingLbl = Label(self.root, text="Date of Booking:", font="Ariel, 12", anchor='e', width=20)
        self.dateOfBookingLbl2 = tk.Label(self.root, font="Ariel, 12", width=20)
        self.dt = datetime.datetime.now().date()
        self.dateOfBookingLbl2.config(text=self.dt)

        self.companyLbl = Label(self.root, text="Company Name:", font="Ariel, 12", anchor='e', width=20)
        self.companyEntry = Entry(self.root)
        self.noOfDaysLbl = Label(self.root, text="Number of Days:", font="Ariel, 12", anchor='e', width=20)
        self.noOfDaysEntry = Entry(self.root)
        self.projectorLbl = Label(self.root, text="Projector Required?:", font="Ariel, 12", anchor='e', width=20)
        self.projectorCheck = tk.Checkbutton(self.root, variable=self.pCheck)
        self.costPerHeadLbl = Label(self.root, text="Cost Per Head:", font="Ariel, 12", anchor='e', width=20)
        self.costPerHeadDisplay = tk.Label(self.root, text="£-", font="Ariel, 12", anchor='e', width=20)
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
        # The default command is "saveconference", this is then changed based on what event type is selected.
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

        # based on what option is selected, the band cost string and the band cost is set to the correct values.
        if self.bandVariable.get() == "Lil' Febrezey":
            self.bc.set(100)
            self.bcs.set("£{0}".format(self.bc))
        elif self.bandVariable.get() == 'Prawn Mendes':
            self.bc.set(250)
            self.bcs.set("£{0}".format(self.bc))
        elif self.bandVariable.get() == 'AB/CD':
            self.bc.set(500)
            self.bcs.set("£{0}".format(self.bc))
        else:
            self.bc.set(0)
            self.bcs.set("£{0}".format(self.bc))

    #  Enable save button function. This should be used to enable the save button when certain criteria is met.
    def enablesavebtn(self, *args):
        if True:
            self.saveBtn.config(state='normal')

    # This function assigns all the values necessary to save a conference and then pushes it to the database.
    def saveconference(self):
        db = data_access.DBAccess()
        c = Conference(
            self.noGuestsEntry.get(),
            self.nameOfContactEntry.get(),
            self.addressEntry.get(),
            self.contactNumberEntry.get(),
            self.roomVariable.get(),
            self.dateOfEventEntry.get(),
            self.companyEntry.get(),
            self.noOfDaysEntry.get(),
            self.pCheck.get(),
            self.dt
        )
        db.insert_(c)

    # This function assigns all the values necessary to save a wedding and then pushes it to the database.
    def savewedding(self):
        db = data_access.DBAccess()
        w = Wedding(
            self.bandVariable.get(),
            self.bc.get(),
            self.noGuestsEntry.get(),
            self.nameOfContactEntry.get(),
            self.addressEntry.get(),
            self.contactNumberEntry.get(),
            self.roomVariable.get(),
            self.dateOfEventEntry.get(),
            self.noOfRoomsEntry.get(),
            self.dt
        )
        db.insert_wedding(w)

    # This function assigns all the values necessary to save a party and then pushes it to the database.
    def saveparty(self):
        db = data_access.DBAccess()
        p = Party(
            self.noGuestsEntry.get(),
            self.nameOfContactEntry.get(),
            self.addressEntry.get(),
            self.contactNumberEntry.get(),
            self.roomVariable.get(),
            self.dateOfEventEntry.get(),
            self.bandVariable.get(),
            self.bc.get(),
            self.dt,
        )
        db.insert_party(p)

    # Function to hide widgets. This can be called using self.hidewidgets('conference'). Replace conference
    # with the event you are wanting to create a display for.
    def hidewidgets(self, eventtype):
        # Hides all widgets not related to the conference input. Called using self.hidewidgets('conference')
        if eventtype == 'conference':
            self.bandNameLbl.grid_remove()
            self.bandName.grid_remove()
            self.bandCostLbl.grid_remove()
            self.bandCostDisplay.grid_remove()
            self.noOfRoomsLbl.grid_remove()
            self.noOfRoomsEntry.grid_remove()
            self.roomNoEntryParty.grid_remove()
            self.roomNoEntryWedding.grid_remove()
        # Hides all widgets not related to the party input. Called using self.hidewidgets('party')
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
        # Hides all widgets not related to the wedding input. Called using self.hidewidgets('wedding')
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
            self.costPerHeadDisplay.config(text="£-")
        elif self.variable.get() == 'Conference':

            # This displays all necessary widgets and calls the function to hide the ones that aren't needed.
            self.enablesavebtn()
            self.costPerHeadDisplay.config(text="£20")
            self.saveBtn.config(command=self.saveconference)
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
            self.costPerHeadDisplay.config(text="£15")
            self.saveBtn.config(command=self.saveparty)
            self.roomNoEntryParty.grid(row=7, column=2, padx=(0, 20))
            self.enablesavebtn()
            self.boptions()

            self.hidewidgets('party')

        elif self.variable.get() == 'Wedding':

            # This displays all necessary widgets and calls the function to hide the ones that aren't needed.
            self.costPerHeadDisplay.config(text="£30")
            self.saveBtn.config(command=self.savewedding)
            self.roomNoEntryWedding.grid(row=7, column=2, padx=(0, 20))
            self.enablesavebtn()
            self.boptions()
            self.noOfRoomsLbl.grid(row=12, column=1)
            self.noOfRoomsEntry.grid(row=12, column=2, padx=(0, 20))

            self.hidewidgets('wedding')
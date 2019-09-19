from abc import abstractmethod
from tkinter import *
from tkinter import messagebox

import gui.top_level_functions as tlf
from classes import *
import tkinter.ttk as ttk
from Data_Access import data_access as da


def save_update(booking):
    db = da.DBAccess()
    if isinstance(booking, Conference):
        db.update_conference(booking)
    elif isinstance(booking, Wedding):
        db.update_wedding(booking)
    elif isinstance(booking, Party):
        db.update_party(booking)
    db.disconnect_db()


class UpdateUIBase:
    def __init__(self, master, event):
        self.master = master
        self.event = event

        # configure master
        self.master.configure(background='white')
        # vars
        # self.yesno = IntVar()
        self.roomNumbers = ['select option']

        # widget padding
        self.paddingX = 5
        self.paddingY = 5

        # button sizes
        self.buttonWidth = 10
        self.buttonHeight = 2
        # widget background colour
        self.widgetBG = 'white'

        # widget
        self.title = Label(self.master, text='Heading', font="Ariel, 16", height=2, bg=self.widgetBG)

        self.noGuestsLbl = Label(self.master, text="Number of Guests:", font="Ariel, 12", anchor='e', width=20,
                                 bg=self.widgetBG)
        self.noGuestsEntry = Entry(self.master, bg=self.widgetBG)
        self.noGuestsEntry.insert(0, event.noGuests)

        self.nameOfContactLbl = Label(self.master, text="Name of Contact:", font="Ariel, 12", anchor='e', width=20,
                                      bg=self.widgetBG)
        self.nameOfContactEntry = Entry(self.master, bg=self.widgetBG)
        self.nameOfContactEntry.insert(0, event.nameofContact)

        self.addressLbl = Label(self.master, text="Full Address of Contact:", font="Ariel, 12", anchor='e', width=20,
                                bg=self.widgetBG)
        self.addressEntry = Entry(self.master, bg=self.widgetBG)
        self.addressEntry.insert(0, event.address)

        self.contactNumberLbl = Label(self.master, text="Contact Number:", font="Ariel, 12", anchor='e', width=20,
                                      bg=self.widgetBG)
        self.contactNumberEntry = Entry(self.master, bg=self.widgetBG)
        self.contactNumberEntry.insert(0, event.contactNo)

        self.roomNoLbl = Label(self.master, text="Event Room Number:", font="Ariel, 12", anchor='e', width=20,
                               bg=self.widgetBG)
        self.roomNoCombo = ttk.Combobox(self.master, value=self.roomNumbers, state='readonly')

        self.dateOfEventLbl = Label(self.master, text="Date of Event:", font="Ariel, 12", anchor='e', width=20,
                                    bg=self.widgetBG)

        self.dateOfEventEntry = Entry(self.master, bg=self.widgetBG)
        self.dateOfEventEntry.configure(disabledbackground="white", disabledforeground="black")
        self.dateOfEventEntry.insert(0, event.dateOfEvent)
        self.dateOfEventEntry.configure(state='readonly')

        self.dateOfEventEntry.bind('<Button-1>', lambda e: tlf.date_top_level(e, self.master, self.dateOfEventEntry))

        self.costPerHeadLbl = Label(self.master, text="Cost Per Head:", font="Ariel, 12", anchor='e', width=20,
                                    bg=self.widgetBG)
        self.costPerHeadDisplay = Label(self.master, font="Ariel, 12", anchor=W, width=20,
                                        text=self.event.costPerhead, bg=self.widgetBG)

        # frame for buttons
        self.frame = Frame(self.master, bg=self.widgetBG)

        # buttons for bottom of form
        self.buttonBack = Button(self.frame, text='Back', bg='snow', width=self.buttonWidth, height=self.buttonHeight,
                                 command=self.master.destroy)
        self.buttonDelete = Button(self.frame, text='Delete', bg='salmon1', width=self.buttonWidth,
                                   height=self.buttonHeight, command=self.delete_booking)

        self.buttonSave = Button(self.frame, text='Save', bg='deep sky blue', width=self.buttonWidth,
                                 height=self.buttonHeight, command=self.create_booking)

        # layout for widget
        # heading
        self.title.grid(columnspan=5)

        self.noGuestsLbl.grid(row=1, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.noGuestsEntry.grid(row=1, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.nameOfContactLbl.grid(row=2, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.nameOfContactEntry.grid(row=2, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.addressLbl.grid(row=3, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.addressEntry.grid(row=3, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.contactNumberLbl.grid(row=4, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.contactNumberEntry.grid(row=4, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.roomNoLbl.grid(row=5, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.roomNoCombo.grid(row=5, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.dateOfEventLbl.grid(row=6, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.dateOfEventEntry.grid(row=6, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.costPerHeadLbl.grid(row=100, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.costPerHeadDisplay.grid(row=100, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.frame.grid(row=101, columnspan=2)

        self.buttonBack.pack(side=LEFT, padx=self.paddingX, pady=self.paddingY)
        self.buttonDelete.pack(side=LEFT, padx=self.paddingX, pady=self.paddingY)
        self.buttonSave.pack(side=LEFT, padx=self.paddingX, pady=self.paddingY)

    def delete_booking(self):
        result = messagebox.askquestion('Delete Booking', 'Deleting booking cannot be undone', icon='warning')
        if result == 'yes':
            db = da.DBAccess()
            print(str(self.event.__class__.__name__))
            db.delete_booking(self.event, str(self.event.__class__.__name__))
            self.master.destroy()
            print('delete')
        else:
            print('not deleted')

    @abstractmethod
    def create_booking(self):
        pass

# Update UI for conference
class UpdateConferenceUI(UpdateUIBase):
    def __init__(self, master, event):
        super().__init__(master, event)

        self.roomNumbers = [
            "A",
            "B",
            "C"
        ]
        self.title.configure(text='Update Conference')
        self.yesno = BooleanVar(self.master, event.projectorRequired)
        # overriding room numbers from super
        self.roomNoCombo.configure(values=self.roomNumbers)
        self.roomNoCombo.current(self.roomNumbers.index(self.event.eventRoomNo))

        self.companyLbl = Label(self.master, text="Company Name:", font="Ariel, 12", anchor='e', width=20,
                                bg=self.widgetBG)
        self.companyEntry = Entry(self.master, bg=self.widgetBG)
        self.companyEntry.insert(0, event.companyName)

        self.noOfDaysLbl = Label(self.master, text="Number of Days:", font="Ariel, 12", anchor='e', width=20,
                                 bg=self.widgetBG)
        self.noOfDaysEntry = Entry(self.master, bg=self.widgetBG)
        self.noOfDaysEntry.insert(0, event.noOfDays)

        self.projectorLbl = Label(self.master, text="Projector Required?:", font="Ariel, 12", anchor='e', width=20,
                                  bg=self.widgetBG)
        self.projectorCheck = Checkbutton(self.master, variable=self.yesno, bg=self.widgetBG)

        # layout for from
        self.companyLbl.grid(row=10, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.companyEntry.grid(row=10, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.noOfDaysLbl.grid(row=11, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.noOfDaysEntry.grid(row=11, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.projectorLbl.grid(row=12, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.projectorCheck.grid(row=12, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

    def create_booking(self):
        c = Conference(ID=self.event.id, noGuests=self.noGuestsEntry.get(), nameofContact=self.nameOfContactEntry.get(),
                       address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                       eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                       companyName=self.companyEntry.get(), noOfDays=self.noOfDaysEntry.get(),
                       projectorRequired=self.yesno.get(), dateofBooking=self.event.dateOfBooking,
                       costPerhead=self.event.costPerhead)
        save_update(c)
        print('updated booking')

# update UI for party
class UpdatePartyUI(UpdateUIBase):
    def __init__(self, master, event):
        super().__init__(master, event)
        self.master = master
        self.event = event

        # vars
        self.roomNumbers = [
            "D",
            "E",
            "F",
            "G"
        ]
        self.bandOptions = [
            "Lil' Febrezey",
            "Prawn Mendes",
            "AB/CD"
        ]

        self.bandChose = StringVar(self.master, self.event.bandPrice)
        self.bandVariable = StringVar()

        # window configure
        self.master.title('Update Party')
        self.title.configure(text='Update Party')

        # overriding super room numbers
        self.roomNoCombo.configure(values=self.roomNumbers)
        if not isinstance(event, Wedding):
            self.roomNoCombo.current(self.roomNumbers.index(self.event.eventRoomNo))
        # window Labels
        self.bandNameLbl = Label(self.master, text="Select Band:", font="Ariel, 12", anchor='e', width=20,
                                 bg=self.widgetBG)
        self.bandName = ttk.Combobox(self.master, values=self.bandOptions, state='readonly',
                                     postcommand=self.band_options)
        self.bandName.current(self.bandOptions.index(self.event.bandName))
        self.bandName.bind('<<ComboboxSelected>>', self.band_options)
        self.bandCostLbl = Label(self.master, text="Band Cost:", font="Ariel, 12", anchor='e', width=20,
                                 bg=self.widgetBG)
        self.bandCostDisplay = Label(self.master, font="Ariel, 12", textvariable=self.bandChose, anchor=W, width=20,
                                     bg=self.widgetBG)

        # grid layout for widgets
        self.bandNameLbl.grid(row=10, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.bandName.grid(row=10, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.bandCostLbl.grid(row=11, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.bandCostDisplay.grid(row=11, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

    def band_options(self, *args):
        if self.bandName.get() == "Lil' Febrezey":
            self.bandChose.set("£{0}".format(100))

        elif self.bandName.get() == "Prawn Mendes":
            self.bandChose.set("£{0}".format(250))

        elif self.bandName.get() == "AB/CD":
            self.bandChose.set("£{0}".format(500))

        else:
            self.bandChose.set("£{0}".format(0))

    def create_booking(self):
        p = Party(ID=self.event.id, noGuests=self.noGuestsEntry.get(), nameofContact=self.nameOfContactEntry.get(),
                  address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                  eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                  dateofBooking=self.event.dateOfBooking, bandName=self.bandName.get(),
                  bandPrice=self.bandChose.get(), costPerhead=self.event.costPerhead)
        save_update(p)

# Update UI for wedding
class UpdateWeddingUI(UpdatePartyUI):
    def __init__(self, master, event):
        super().__init__(master, event)
        self.master = master
        self.event = event

        # configure window
        self.master.title('Update Wedding')
        self.title.configure(text='Update Wedding')

        # overriding super room number options
        self.roomNumbers = ["H", "I"]
        self.roomNoCombo.configure(values=self.roomNumbers)
        self.roomNoCombo.current(self.roomNumbers.index(self.event.eventRoomNo))

        # widgets for form
        self.noOfRoomsLbl = Label(self.master, text="Number of Rooms:", font="Ariel, 12", anchor='e', width=20,
                                  bg=self.widgetBG)
        self.noOfRoomsEntry = Entry(self.master, bg=self.widgetBG)
        self.noOfRoomsEntry.insert(0, str(event.noBedroomsReserved))

        # grid layout for widgets
        self.noOfRoomsLbl.grid(row=12, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.noOfRoomsEntry.grid(row=12, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

    def create_booking(self):
        w = Wedding(ID=self.event.id, noGuests=self.noGuestsEntry.get(), nameofContact=self.nameOfContactEntry.get(),
                    address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                    eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                    dateOfBooking=self.event.dateOfBooking, bandName=self.bandName.get(),
                    bandPrice=self.bandChose.get(), costPerhead=self.event.costPerhead,
                    noBedroomsReserved=self.noOfRoomsEntry.get())
        save_update(w)
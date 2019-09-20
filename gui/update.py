from abc import abstractmethod
from tkinter import *
from tkinter import messagebox
import money_convert as mc
import gui.top_level_functions as tlf
from classes import *
import tkinter.ttk as ttk
from Data_Access import data_access as da
from gui import tkinter_styling as style
import validation


def save_update(booking):
    db = da.DBAccess()
    if isinstance(booking, Conference):
        db.update_conference(booking)
    elif isinstance(booking, Wedding):
        db.update_wedding(booking)
    elif isinstance(booking, Party):
        db.update_party(booking)


def number_only(value, event):
    if event == '1':
        if not value.isdigit():
            return False
    return True


def getFreeRooms(listRooms, event):
    db = da.DBAccess()
    usedRooms = db.getBookedRooms(event.__class__.__name__, event.dateOfEvent, event.id)
    freeRooms = []
    for room in listRooms:
        if room not in list(usedRooms):
            freeRooms.append(room)
    return freeRooms


def getFreeBands(bandNames, event):
    db = da.DBAccess()
    userBands = db.getBookedBands(event.dateOfEvent, str(event.__class__.__name__).lower(), event.id)
    freeBands = []
    for band in bandNames:
        if band not in userBands:
            freeBands.append(band)
    return freeBands


class UpdateUIBase:
    def __init__(self, master, event):
        self.master = master
        self.event = event

        # configure master
        self.master.configure(background='white')
        self.roomNumbers = ['select option']

        # widget
        self.title = Label(self.master, text='Heading', font=style.textHeading, height=2, bg=style.widgetBG)

        self.noGuestsLbl = Label(self.master, text="Number of Guests:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)
        self.noGuestsEntry = Entry(self.master, bg=style.widgetBG, validate='key')
        self.noGuestsEntry.configure(validatecommand=(self.noGuestsEntry.register(validation.NumbersOnly), '%S', '%d'))
        self.noGuestsEntry.insert(0, event.noGuests)

        self.nameOfContactLbl = Label(self.master, text="Name of Contact:", font=style.textNormal, anchor='e', width=20,
                                      bg=style.widgetBG)
        self.nameOfContactEntry = Entry(self.master, bg=style.widgetBG, validate='key')
        self.nameOfContactEntry.configure(validatecommand=(self.nameOfContactEntry.register(validation.lettersOnly),
                                                           '%S', '%d'))
        self.nameOfContactEntry.insert(0, event.nameofContact)

        self.addressLbl = Label(self.master, text="Full Address of Contact:", font=style.textNormal, anchor='e',
                                width=20,
                                bg=style.widgetBG)
        self.addressEntry = Entry(self.master, bg=style.widgetBG, validate='key')
        self.addressEntry.configure(validatecommand=(self.addressEntry.register(validation.noSpecialCharacter), '%S', '%d'))
        self.addressEntry.insert(0, event.address)

        self.contactNumberLbl = Label(self.master, text="Contact Number:", font=style.textNormal, anchor='e', width=20,
                                      bg=style.widgetBG)
        self.contactNumberEntry = Entry(self.master, bg=style.widgetBG, validate='key')
        self.contactNumberEntry['validatecommand'] = (self.contactNumberEntry.register(validation.NumbersOnly),
                                                      '%S', '%d')
        self.contactNumberEntry.insert(0, event.contactNo)

        self.roomNoLbl = Label(self.master, text="Event Room Number:", font=style.textNormal, anchor='e', width=20,
                               bg=style.widgetBG)
        self.roomNoCombo = ttk.Combobox(self.master, value=self.roomNumbers, state='readonly')

        self.dateOfEventLbl = Label(self.master, text="Date of Event:", font=style.textNormal, anchor='e', width=20,
                                    bg=style.widgetBG)

        self.dateOfEventEntry = Entry(self.master, bg=style.widgetBG)
        self.dateOfEventEntry.configure(disabledbackground="white", disabledforeground="black")
        self.dateOfEventEntry.insert(0, event.dateOfEvent)
        self.dateOfEventEntry.configure(state='readonly')

        self.dateOfEventEntry.bind('<Button-1>', lambda e: tlf.date_top_level(e, self.master, self.dateOfEventEntry))

        self.costPerHeadLbl = Label(self.master, text="Cost Per Head:", font=style.textNormal, anchor='e', width=20,
                                    bg=style.widgetBG)
        self.costPerHeadDisplay = Label(self.master, font=style.textNormal, anchor=W, width=20,
                                        text=mc.pound_string(self.event.costPerhead), bg=style.widgetBG)

        # frame for buttons
        self.frame = Frame(self.master, bg=style.widgetBG)

        # buttons for bottom of form
        self.buttonBack = Button(self.frame, text='Back', bg='snow', width=style.buttonWidth, height=style.buttonHeight,
                                 command=self.master.destroy)
        self.buttonDelete = Button(self.frame, text='Delete', bg='salmon1', width=style.buttonWidth,
                                   height=style.buttonHeight, command=self.delete_booking)

        self.buttonSave = Button(self.frame, text='Save', bg='deep sky blue', width=style.buttonWidth,
                                 height=style.buttonHeight, command=self.create_booking)

        # layout for widget
        # heading
        self.title.grid(columnspan=5)

        self.noGuestsLbl.grid(row=1, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.noGuestsEntry.grid(row=1, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.nameOfContactLbl.grid(row=2, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.nameOfContactEntry.grid(row=2, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.addressLbl.grid(row=3, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.addressEntry.grid(row=3, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.contactNumberLbl.grid(row=4, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.contactNumberEntry.grid(row=4, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.roomNoLbl.grid(row=5, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.roomNoCombo.grid(row=5, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.dateOfEventLbl.grid(row=6, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.dateOfEventEntry.grid(row=6, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.costPerHeadLbl.grid(row=100, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.costPerHeadDisplay.grid(row=100, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.frame.grid(row=101, columnspan=2)

        self.buttonBack.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)
        self.buttonDelete.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)
        self.buttonSave.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)

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
        # todo add conference room validation
        self.title.configure(text='Update Conference')
        self.yesno = BooleanVar(self.master, event.projectorRequired)
        # overriding room numbers from super
        self.roomNoCombo.configure(values=self.roomNumbers)
        self.roomNoCombo.current(self.roomNumbers.index(self.event.eventRoomNo))

        self.companyLbl = Label(self.master, text="Company Name:", font=style.textNormal, anchor='e', width=20,
                                bg=style.widgetBG)
        self.companyEntry = Entry(self.master, bg=style.widgetBG)
        self.companyEntry.insert(0, event.companyName)

        self.noOfDaysLbl = Label(self.master, text="Number of Days:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)
        self.noOfDaysEntry = Entry(self.master, bg=style.widgetBG, validate='key')
        self.noOfDaysEntry.configure(validatecommand=(self.noOfDaysEntry.register(validation.NumbersOnly), '%S', '%d'))
        self.noOfDaysEntry.insert(0, event.noOfDays)

        self.projectorLbl = Label(self.master, text="Projector Required?:", font=style.textNormal, anchor='e', width=20,
                                  bg=style.widgetBG)
        self.projectorCheck = Checkbutton(self.master, variable=self.yesno, bg=style.widgetBG)

        # layout for from
        self.companyLbl.grid(row=10, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.companyEntry.grid(row=10, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.noOfDaysLbl.grid(row=11, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.noOfDaysEntry.grid(row=11, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.projectorLbl.grid(row=12, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.projectorCheck.grid(row=12, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

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
        self.bandOptions = getFreeBands(self.bandOptions, self.event)
        self.roomNumbers = getFreeRooms(self.roomNumbers, self.event)

        self.bandChose = StringVar(self.master, mc.pound_string(event.bandPrice))
        self.bandVariable = StringVar()
        self.bandCost = 0

        # window configure
        self.master.title('Update Party')
        self.title.configure(text='Update Party')

        # overriding super room numbers
        self.roomNoCombo.configure(values=self.roomNumbers)
        if not isinstance(event, Wedding):
            self.roomNoCombo.current(self.roomNumbers.index(self.event.eventRoomNo))
        # window Labels
        self.bandNameLbl = Label(self.master, text="Select Band:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)
        self.bandName = ttk.Combobox(self.master, values=self.bandOptions, state='readonly',
                                     postcommand=self.band_options)
        self.bandName.current(self.bandOptions.index(self.event.bandName))
        self.bandName.bind('<<ComboboxSelected>>', self.band_options)
        self.bandCostLbl = Label(self.master, text="Band Cost:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)
        self.bandCostDisplay = Label(self.master, font=style.textNormal, textvariable=self.bandChose, anchor=W,
                                     width=20,
                                     bg=style.widgetBG)

        # grid layout for widgets
        self.bandNameLbl.grid(row=10, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.bandName.grid(row=10, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.bandCostLbl.grid(row=11, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.bandCostDisplay.grid(row=11, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

    def band_options(self, *args):
        if self.bandName.get() == "Lil' Febrezey":
            self.bandChose.set(mc.pound_string(100))
            self.bandCost = 100

        elif self.bandName.get() == "Prawn Mendes":
            self.bandChose.set(mc.pound_string(250))
            self.bandCost = 250

        elif self.bandName.get() == "AB/CD":
            self.bandChose.set(mc.pound_string(500))
            self.bandCost = 500

        else:
            self.bandChose.set(mc.pound_string(0))
            self.bandCost = 0

    def create_booking(self):
        p = Party(ID=self.event.id, noGuests=self.noGuestsEntry.get(), nameofContact=self.nameOfContactEntry.get(),
                  address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                  eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                  dateofBooking=self.event.dateOfBooking, bandName=self.bandName.get(),
                  bandPrice=self.bandCost, costPerhead=self.event.costPerhead)
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
        self.roomNumbers = getFreeRooms(self.roomNumbers, self.event)
        self.roomNoCombo.configure(values=self.roomNumbers)
        self.roomNoCombo.current(self.roomNumbers.index(self.event.eventRoomNo))

        # widgets for form
        self.noOfRoomsLbl = Label(self.master, text="Number of Rooms:", font=style.textNormal, anchor='e', width=20,
                                  bg=style.widgetBG)
        self.noOfRoomsEntry = Entry(self.master, bg=style.widgetBG)
        self.noOfRoomsEntry.insert(0, str(event.noBedroomsReserved))

        # grid layout for widgets
        self.noOfRoomsLbl.grid(row=12, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.noOfRoomsEntry.grid(row=12, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

    def create_booking(self):
        w = Wedding(ID=self.event.id, noGuests=self.noGuestsEntry.get(), nameofContact=self.nameOfContactEntry.get(),
                    address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                    eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                    dateOfBooking=self.event.dateOfBooking, bandName=self.bandName.get(),
                    bandPrice=self.bandCost, costPerhead=self.event.costPerhead,
                    noBedroomsReserved=self.noOfRoomsEntry.get())
        save_update(w)

"""module contains the classes and functions needed to update a booking for party, wedding and conference"""
from abc import abstractmethod
from tkinter import *
from tkinter import messagebox
import money_convert as mc
import gui.top_level_functions as tlf
from classes import *
import tkinter.ttk as ttk
from Data_Access import data_access as da
from gui import tkinter_styling as style, dialogs
import validation
import constvalues as CONST

db = da.DBAccess()


def save_update(booking, master):
    """function to save updated booking information into database"""
    if isinstance(booking, Conference):
        db.update_conference(booking)
    elif isinstance(booking, Wedding):
        db.update_wedding(booking)
    elif isinstance(booking, Party):
        db.update_party(booking)
    dialogs.updated(master)


class UpdateUIBase:
    """class is used as the base for the UpdateConferenceUI class and UpdatePartyUI class"""

    def __init__(self, master, event):

        self.master = master
        self.master.resizable(0, 0)
        self.master.iconbitmap(str(style.logo))
        self.event = event

        # rooms combobox string for default option
        self.roomComboText = StringVar()

        # bool to track if room number selected
        self.roomSelected = False

        # string to track value of date of event
        self.dateOfEventValue = StringVar(self.master, self.event.dateOfEvent)

        # configure master
        self.master.configure(background=style.windowBG)
        self.roomNumbers = ['select option']

        # widgets
        # form title
        self.title = Label(self.master, text='Heading', font=style.textHeading, height=2, bg=style.widgetBG)

        # number of guests widgets
        self.noGuestsLbl = Label(self.master, text="Number of Guests:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)

        self.noGuestsEntry = Entry(self.master, validate='key')
        self.noGuestsEntry.configure(validatecommand=(self.noGuestsEntry.register(validation.NumbersOnly), '%S', '%d'))

        self.noGuestsEntry.insert(0, event.noGuests)

        # name of contact widgets
        self.nameOfContactLbl = Label(self.master, text="Name of Contact:", font=style.textNormal, anchor='e', width=20,
                                      bg=style.widgetBG)

        self.nameOfContactEntry = Entry(self.master, validate='key')
        self.nameOfContactEntry.configure(validatecommand=(self.nameOfContactEntry.register(
            lambda S, P, d, parent=self.master: validation.lettersOnly(S, P, d, parent)), '%S', '%P', '%d'))

        self.nameOfContactEntry.insert(0, event.nameofContact)

        # address widgets
        self.addressLbl = Label(self.master, text="Full Address of Contact:", font=style.textNormal, anchor='e',
                                width=20, bg=style.widgetBG)
        self.addressEntry = Entry(self.master, validate='key')
        self.addressEntry.configure(
            validatecommand=(self.addressEntry.register(
                lambda S, P, d, parent=self.master: validation.check_address(S, P, d, parent)), '%S', '%P', '%d'))
        self.addressEntry.insert(0, event.address)

        # contact number widgets
        self.contactNumberLbl = Label(self.master, text="Contact Number:", font=style.textNormal, anchor='e', width=20,
                                      bg=style.widgetBG)
        self.contactNumberEntry = Entry(self.master, validate='key')
        self.contactNumberEntry['validatecommand'] = (self.contactNumberEntry.register(
            lambda S, P, d, parent=self.master: validation.ValidatePhoneNumber(S, P, d, parent)), '%S', '%P', '%d')
        self.contactNumberEntry.insert(0, event.contactNo)

        # room number widgets
        self.roomNoLbl = Label(self.master, text="Event Room Number:", font=style.textNormal, anchor='e', width=20,
                               bg=style.widgetBG)
        self.roomNoCombo = ttk.Combobox(self.master, value=self.roomNumbers, state='readonly',
                                        textvariable=self.roomComboText)
        self.roomNoCombo.bind('<<ComboboxSelected>>', self.room_pick)

        # date of event widgets
        self.dateOfEventLbl = Label(self.master, text="Date of Event:", font=style.textNormal, anchor='e', width=20,
                                    bg=style.widgetBG)

        self.dateOfEventEntry = Entry(self.master, textvariable=self.dateOfEventValue)
        self.dateOfEventEntry.configure(disabledbackground="white", disabledforeground="black")
        self.dateOfEventEntry.configure(state='readonly')

        # if date of event can only be changed if date not in the pasted
        if not self.event.dateOfEvent < datetime.datetime.now().date():
            self.dateOfEventEntry.bind('<Button-1>', lambda e: tlf.calendar_popup(e, self.master, self.dateOfEventValue,
                                                                                  self.dateOfEventValue.get()))

        # cost per head widgets
        self.costPerHeadLbl = Label(self.master, text="Cost Per Head:", font=style.textNormal, anchor='e', width=20,
                                    bg=style.widgetBG)
        self.costPerHeadDisplay = Label(self.master, font=style.textNormal, anchor=W, width=20,
                                        text=mc.pound_string(self.event.costPerhead), bg=style.widgetBG)

        # frame for buttons
        self.frame = Frame(self.master, bg=style.widgetBG)

        # buttons for bottom of form
        self.buttonBack = Button(self.frame, text='Back', bg='snow', width=style.buttonWidth, height=style.buttonHeight,
                                 command=self.master.destroy)
        self.buttonDelete = Button(self.frame, text='Delete', bg=style.buttonColour1, width=style.buttonWidth,
                                   height=style.buttonHeight, command=self.delete_booking)

        self.buttonSave = Button(self.frame, text='Save', bg=style.buttonColour2, width=style.buttonWidth,
                                 height=style.buttonHeight, command=self.update_booking)

        # layout for widget
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
        """method that will delete booking from database"""
        result = messagebox.askquestion('Delete Booking', 'Deleting booking cannot be undone\nAre you Sure?',
                                        icon='warning')
        if result == 'yes':
            db = da.DBAccess()
            print(str(self.event.__class__.__name__))
            db.delete_booking(self.event, str(self.event.__class__.__name__))
            dialogs.deleted(self.master)
            self.master.destroy()
            print('delete')
        else:
            print('not deleted')

    @abstractmethod
    def update_booking(self):
        """method to be given body by child classes. method is used to update the booking"""
        pass

    def guests_entered(self):
        """method to check if number of guests is between 0 and 1000"""
        if 0 <= int(self.noGuestsEntry.get()) <= 1000:
            return True
        return False

    def room_pick(self, event=None):
        """check if room selected is in the roomNumbers list and not the default option"""
        if self.roomNoCombo.get() in self.roomNumbers:
            self.roomSelected = True
        else:
            self.roomSelected = False


class UpdateConferenceUI(UpdateUIBase):
    """# Update UI for conference based of UpdateUIBase contains the methods and UI elements needed to update a
    conference booking """

    def __init__(self, master, event):
        super().__init__(master, event)

        # overriding room numbers from super
        self.roomNumbers = CONST.CONFERENCE_ROOMS
        self.title.configure(text='Update Conference')
        self.yesno = BooleanVar(self.master, event.projectorRequired)
        self.roomNoCombo.configure(values=self.roomNumbers)
        self.roomNoCombo.current(self.roomNumbers.index(self.event.eventRoomNo))
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.conference_room_check(event=NONE))

        # widget for company name
        self.companyLbl = Label(self.master, text="Company Name:", font=style.textNormal, anchor='e', width=20,
                                bg=style.widgetBG)
        self.companyEntry = Entry(self.master, font=style.textNormal, validate='key')
        self.companyEntry.configure(validatecommand=(self.companyEntry.register(
            lambda P, limit=int(100), parent=self.master: validation.char_limit(P, limit, parent)), '%P'))
        self.companyEntry.insert(0, event.companyName)

        # number of days widgets
        self.noOfDaysLbl = Label(self.master, text="Number of Days:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)

        self.noOfDaysValue = StringVar(self.master, self.event.noOfDays)
        self.noOfDaysEntry = Entry(self.master, validate='key', textvariable=self.noOfDaysValue)
        self.noOfDaysEntry.configure(validatecommand=(self.noOfDaysEntry.register(
            lambda S, d, P, limit=50, parent=self.master: validation.NumbersOnly(S, d, P, limit, parent)), '%S', '%d',
                                                      '%P'))
        self.noOfDaysValue.trace('w', lambda name, index, mode: self.conference_room_check(event=None))

        # projector required widgets
        self.projectorLbl = Label(self.master, text="Projector Required?:", font=style.textNormal, anchor='e', width=20,
                                  bg=style.widgetBG)
        self.projectorCheck = Checkbutton(self.master, text="Tick for Yes", variable=self.yesno, bg=style.widgetBG)

        # layout for from using gird layout
        self.companyLbl.grid(row=10, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.companyEntry.grid(row=10, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.noOfDaysLbl.grid(row=11, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.noOfDaysEntry.grid(row=11, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.projectorLbl.grid(row=12, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.projectorCheck.grid(row=12, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        # updating room list to remove any rooms that would be double booked on date of event
        self.conference_room_check(None)

    def update_booking(self):
        """method to ensure that information entered into form is validated and if correct will save this information in
            a conference booking object to be update in the database """
        if not validation.EntriesNotEmpty(self.master):
            dialogs.not_completed(self.master)
        elif not self.guests_entered():
            dialogs.not_completed(self.master, 'Number of guests must be greater than 0 and no more than 1000')
        elif not self.number_days_entered():
            dialogs.not_completed(self.master, 'Number of days must be greater than 0 and no more than 50')
        elif not self.roomSelected:
            dialogs.not_completed(self.master, 'A Room must be Selected')
        else:
            c = Conference(ID=self.event.id, noGuests=self.noGuestsEntry.get(),
                           nameofContact=self.nameOfContactEntry.get(),
                           address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                           eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                           companyName=self.companyEntry.get(), noOfDays=self.noOfDaysEntry.get(),
                           projectorRequired=self.yesno.get(), dateofBooking=self.event.dateOfBooking,
                           costPerhead=self.event.costPerhead)
            save_update(c, self.master)
            self.master.destroy()
            print('updated booking')

    def conference_room_check(self, event):
        """method to check for rooms that would be double booked on the date of event and remove them as options in
        the room number drop down """
        if self.dateOfEventValue.get() != '' and self.noOfDaysEntry.get() != '':
            bookedRooms = db.booked_conference_rooms(datetime.datetime.strptime(self.dateOfEventValue.get(), '%Y-%m-%d')
                                                     , int(self.noOfDaysEntry.get()), self.event.id)
            freeRooms = []
            for rooms in CONST.CONFERENCE_ROOMS:
                if rooms not in bookedRooms:
                    freeRooms.append(rooms)
            self.roomNumbers = freeRooms
            self.roomNoCombo.configure(values=self.roomNumbers)
            if self.roomNoCombo.get() not in freeRooms:
                self.roomSelected = False
                self.roomNoCombo.delete(0, 'end')
                if len(freeRooms) > 0:
                    self.roomComboText.set('please select room')
                else:
                    self.roomComboText.set('No Rooms available')
            else:
                self.roomSelected = True

    def number_days_entered(self):
        """checks that the number of days is between 0 and 50"""
        if 0 < int(self.noOfDaysEntry.get()) <= 50:
            return True
        return False


class UpdatePartyUI(UpdateUIBase):
    """update UI for party based on UpdateUIBase class"""

    def __init__(self, master, event):
        super().__init__(master, event)
        self.master = master
        self.event = event

        # vars
        self.roomNumbers = CONST.PARTY_ROOMS
        self.bandOptions = list(CONST.BANDS.keys())

        self.bandChose = StringVar(self.master, mc.pound_string(event.bandPrice))
        self.bandVariable = StringVar()
        self.bandCost = 0

        # window configure
        self.master.title('Update Party')
        self.title.configure(text='Update Party')

        # overriding super room numbers
        self.roomNoCombo.configure(values=self.roomNumbers)
        # overriding super date of event entry widget bind events
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeBands(list(CONST.BANDS.keys()), 'party'))
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeRooms(CONST.PARTY_ROOMS, 'party'))

        # if type of event is party then select room booked on create from roomNumber list
        if type(event) == Party:
            self.roomNoCombo.current(self.roomNumbers.index(self.event.eventRoomNo))

        # widgets for selecting a band
        self.bandNameLbl = Label(self.master, text="Select Band:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)
        self.bandNameCombobox = ttk.Combobox(self.master, values=self.bandOptions, state='readonly',
                                             postcommand=self.band_options, textvariable=self.bandVariable)
        self.bandNameCombobox.current(self.bandOptions.index(self.event.bandName))
        self.bandNameCombobox.bind('<<ComboboxSelected>>', self.band_options)

        self.bandCostLbl = Label(self.master, text="Band Cost:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)
        self.bandCostDisplay = Label(self.master, font=style.textNormal, textvariable=self.bandChose, anchor=W,
                                     width=20,
                                     bg=style.widgetBG)

        # grid layout for widgets
        self.bandNameLbl.grid(row=10, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.bandNameCombobox.grid(row=10, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.bandCostLbl.grid(row=11, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.bandCostDisplay.grid(row=11, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        # if event is a type of party then check for free bands and rooms for party
        if type(self.event) == Party:
            self.freeBands(list(CONST.BANDS.keys()), 'party')
            self.freeRooms(CONST.PARTY_ROOMS, 'party')
            self.band_options()

    def band_options(self, *args):
        """
        method to change displayed band price when a band is selected in combobox, also changes to band cost value
        """
        bandPrice = CONST.BANDS.get(self.bandNameCombobox.get())
        if bandPrice:
            self.bandChose.set(mc.pound_string(bandPrice))
            self.bandCost = bandPrice
        else:
            self.bandCost = 0
            self.bandChose.set(mc.pound_string(0))

    def update_booking(self):
        """method to ensure that information entered into form is validated and if correct will save this information in
            a party booking object to be update in the database """
        if not validation.EntriesNotEmpty(self.master):
            dialogs.not_completed(self.master)
        elif not self.band_selected():
            dialogs.not_completed(self.master, 'Band must be selected')
        elif not self.guests_entered():
            dialogs.not_completed(self.master, 'Number of guests must be greater than 0 and no more than 1000')
        elif not self.roomSelected:
            dialogs.not_completed(self.master, 'A Room must be Selected')
        else:
            p = Party(ID=self.event.id, noGuests=self.noGuestsEntry.get(), nameofContact=self.nameOfContactEntry.get(),
                      address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                      eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                      dateofBooking=self.event.dateOfBooking, bandName=self.bandNameCombobox.get(),
                      bandPrice=self.bandCost, costPerhead=self.event.costPerhead)
            save_update(p, self.master)
            self.master.destroy()

    def band_selected(self):
        """returns True if selected band name is in the bandOptions list else False"""
        return True if self.bandNameCombobox.get() in self.bandOptions else False

    def freeRooms(self, roomList, eventType, event=None):
        """methods checks for rooms that would be double booked on a given date and will remove these as options from
        the room combobox.  Method takes a list of room numbers, what type of event (ether party or wedding)
        event if method bind to event """

        if eventType.lower() != 'party' and eventType.lower() != 'wedding':
            raise ValueError('event type must be either party or wedding')
        if self.dateOfEventValue.get() != '':
            bookedRooms = db.getBookedRooms(eventType, self.dateOfEventValue.get(), self.event.id)
            freeRooms = []
            for room in roomList:
                if room not in bookedRooms:
                    freeRooms.append(room)
                self.roomNumbers = freeRooms
            self.roomNoCombo.configure(values=self.roomNumbers)
            if self.roomNoCombo.get() not in freeRooms:
                self.roomSelected = False
                self.roomNoCombo.delete(0, 'end')
                if len(freeRooms) > 0:
                    self.roomComboText.set('Please Select a Room')
                else:
                    self.roomComboText.set('No Rooms available')
            else:
                self.roomSelected = True

    def freeBands(self, bandList, eventType, event=None):
        """method checks for bands that would be double booked on the selected date of event and removes these as
        options from the band combobox.  Method takes a list of bandNames, event type (either party or wedding) and
        event if method is bind to event"""

        if eventType.lower() != 'party' and eventType.lower() != 'wedding':
            raise ValueError('event type must be either party or wedding')

        if self.dateOfEventValue.get() != '':
            bookedBands = db.getBookedBands(self.dateOfEventValue.get(), eventType, self.event.id)
            freeBands = []
            for band in bandList:
                if band not in bookedBands or band == 'No band':
                    freeBands.append(band)
            self.bandOptions = freeBands
            self.bandNameCombobox.configure(values=self.bandOptions)
            if self.bandNameCombobox.get() not in freeBands:
                self.bandNameCombobox.delete(0, 'end')
                self.bandVariable.set('Please Select a Band')
                self.band_options()


class UpdateWeddingUI(UpdatePartyUI):
    """Update UI for wedding based of the UpdatePartyUI class"""

    def __init__(self, master, event):
        super().__init__(master, event)
        self.master = master
        self.event = event

        # configure window
        self.master.title('Update Wedding')
        self.title.configure(text='Update Wedding')

        # overriding super room number options
        self.roomNumbers = CONST.WEDDING_ROOMS
        self.roomNoCombo.configure(values=self.roomNumbers)

        self.roomNoCombo.current(self.roomNumbers.index(self.event.eventRoomNo))

        # overriding parent class trace events
        for ti in self.dateOfEventValue.trace_vinfo():
            self.dateOfEventValue.trace_vdelete(*ti)

        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeBands(list(CONST.BANDS.keys()),
                                                                                  'wedding'))
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeRooms(CONST.WEDDING_ROOMS, 'wedding'))

        # widgets for form
        self.noOfRoomsLbl = Label(self.master, text="Number of Rooms:", font=style.textNormal, anchor='e', width=20,
                                  bg=style.widgetBG)
        self.noOfRoomsEntry = Entry(self.master, font=style.textNormal, validate='key')
        self.noOfRoomsEntry.configure(
            validatecommand=(self.noOfRoomsEntry.register(
                lambda S, d, parent=self.master: validation.NumbersOnly(S, d, parent=parent)), '%S', '%d'))
        self.noOfRoomsEntry.insert(0, str(event.noBedroomsReserved))

        # grid layout for widgets
        self.noOfRoomsLbl.grid(row=12, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.noOfRoomsEntry.grid(row=12, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.freeRooms(CONST.WEDDING_ROOMS, 'wedding')
        self.freeBands(list(CONST.BANDS.keys()), 'wedding')
        self.band_options()

    def update_booking(self):
        """method to ensure that information entered into form is validated and if correct will save this information in
                    a wedding booking object to be update in the database"""
        if not validation.EntriesNotEmpty(self.master):
            dialogs.not_completed(self.master)
        elif not self.band_selected():
            dialogs.not_completed(self.master, 'Band must be selected')
        elif not self.guests_entered():
            dialogs.not_completed(self.master, 'Number of guests must be greater than 0 and no more than 1000')
        elif not self.number_room_entered():
            dialogs.not_completed(self.master, 'Number of Rooms reserved must be at least 0 and no more than 1000')
        else:
            w = Wedding(ID=self.event.id, noGuests=self.noGuestsEntry.get(),
                        nameofContact=self.nameOfContactEntry.get(),
                        address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                        eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                        dateOfBooking=self.event.dateOfBooking, bandName=self.bandNameCombobox.get(),
                        bandPrice=self.bandCost, costPerhead=self.event.costPerhead,
                        noBedroomsReserved=self.noOfRoomsEntry.get())
            save_update(w, self.master)
            self.master.destroy()

    def number_room_entered(self):
        """method to check if number of rooms entered is between 0 and 200"""
        if 0 <= int(self.noOfRoomsEntry.get()) <= 200:
            return True
        return False

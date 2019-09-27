from tkinter import *
import tkinter.ttk as ttk
import constvalues as CONST
import gui.top_level_functions as tlf
from abc import abstractmethod
from gui import tkinter_styling as style
import validation
import money_convert as mc
from Data_Access import data_access as da
from gui import dialogs, main_menu
from classes import *


def clear(master):
    """function that clears all the entry boxes, option menus and date of event"""
    widgets = master.winfo_children()
    for widget in widgets:
        if type(widget) == Entry:
            widget.delete(0, 'end')  # clears all entry boxes
        elif type(widget) == Frame:
            clear(widget)


def back_to_main(master):
    """function to close create window and bring user back to main menu to do this it finds the parent root of the
    window and destroys it and creates a new root for the main menu"""
    root = master
    while type(root) != Tk:
        root = root.master
    root.destroy()
    newRoot = Tk()
    main_menu.MainMenuUI(newRoot)
    newRoot.mainloop()


class CreateMenu:
    """class for the first loaded menu on the create window.  The class contains a frame which the rest of the create UI
    will be displayed when the user selects which type of event is being booked"""
    def __init__(self, master):
        self.master = master
        self.master.configure(background=style.windowBG)
        self.master.resizable(0, 0)
        self.master.iconbitmap(str(style.logo))
        self.master.title('Create Booking')

        self.master.protocol('WM_DELETE_WINDOW', self.back_to_main_menu)

        self.UI = None  # variable used to  store UI class being displayed in UI_Frame
        self.buttonActive = False  # boolean to track when the save and clear buttons are in normal state

        self.title = Label(self.master, text='Create New Booking', font=style.textHeading, bg=style.widgetBG)
        self.chooseEventTypeLabel = Label(self.master, text='Choose Event Type:', font=style.textNormal,
                                          bg=style.widgetBG)
        self.eventTypeVar = StringVar(self.master, 'Choose Event Type')
        self.choseEventTypeCombobox = ttk.Combobox(self.master, state='readonly', font=style.textNormal,
                                                   value=CONST.EVENT_TYPES, textvariable=self.eventTypeVar)
        self.choseEventTypeCombobox.bind('<<ComboboxSelected>>', self.display_Create_form)

        self.buttonFrame = Frame(self.master, bg=style.widgetBG)
        self.backButton = Button(self.buttonFrame, text='Back', bg='snow', height=style.buttonHeight,
                                 width=style.buttonWidth, font=style.textNormal, command=self.back_to_main_menu)
        self.clearButton = Button(self.buttonFrame, bg=style.buttonColour1, height=style.buttonHeight,
                                  width=style.buttonWidth, text='Clear', font=style.textNormal, state='disabled')
        self.saveButton = Button(self.buttonFrame, bg=style.buttonColour2, height=style.buttonHeight,
                                 width=style.buttonWidth, text='Save', font=style.textNormal, state='disabled')
        self.UI_Frame = Frame(self.master, bg=style.widgetBG)

        # grid layout for widgets
        self.title.grid(row=0, column=0, columnspan=2, padx=style.paddingX, pady=style.paddingY)

        self.chooseEventTypeLabel.grid(row=1, column=0, padx=style.paddingX, pady=style.paddingY, sticky=E)
        self.choseEventTypeCombobox.grid(row=1, column=1, padx=style.paddingX, pady=style.paddingY, sticky=W)
        self.UI_Frame.grid(row=2, column=0, columnspan=2)
        self.buttonFrame.grid(row=3, column=0, columnspan=2)
        self.backButton.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)
        self.clearButton.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)
        self.saveButton.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)

    def display_Create_form(self, event=None):
        """method to display the create UI for the selected Event type in the chosen event type combobox"""
        eventDic = {'Conference': CreateConference, 'Party': CreateParty, 'Wedding': CreateWedding}
        self.UI = eventDic.get(self.choseEventTypeCombobox.get())
        if self.UI:
            for widget in self.UI_Frame.winfo_children():
                widget.destroy()
            self.UI = self.UI(self.UI_Frame)
            self.saveButton.configure(command=self.UI.create_booking)
            self.clearButton.configure(command=self.UI.clear)

            if not self.buttonActive:
                self.saveButton.configure(state='normal')
                self.clearButton.configure(state='normal')
                self.buttonActive = True

    def back_to_main_menu(self):
        """method to close create window and open a new main menu window"""
        self.master.destroy()
        root = Tk()
        main_menu.MainMenuUI(root)
        root.mainloop()


class BaseCreate:
    """Class that is the base for all create booking classes for each event type"""
    def __init__(self, master):
        self.master = master

        self.roomNumbers = []
        self.roomComboText = StringVar(self.master, 'Please select a Room')
        self.roomSelected = False

        self.dateOfEventValue = StringVar(self.master, datetime.datetime.now().date())

        self.noGuestsLbl = Label(self.master, text="Number of Guests:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)

        self.noGuestsEntry = Entry(self.master, validate='key')
        self.noGuestsEntry.configure(validatecommand=(self.noGuestsEntry.register(validation.NumbersOnly), '%S', '%d'))

        self.nameOfContactLbl = Label(self.master, text="Name of Contact:", font=style.textNormal, anchor='e', width=20,
                                      bg=style.widgetBG)

        self.nameOfContactEntry = Entry(self.master, validate='key')
        self.nameOfContactEntry.configure(validatecommand=(self.nameOfContactEntry.register(validation.lettersOnly),
                                                           '%S', '%P', '%d'))

        self.addressLbl = Label(self.master, text="Full Address of Contact:", font=style.textNormal, anchor='e',
                                width=20,
                                bg=style.widgetBG)
        self.addressEntry = Entry(self.master, validate='key')
        self.addressEntry.configure(
            validatecommand=(self.addressEntry.register(validation.noSpecialCharacter), '%S', '%P', '%d'))

        self.contactNumberLbl = Label(self.master, text="Contact Number:", font=style.textNormal, anchor='e', width=20,
                                      bg=style.widgetBG)
        self.contactNumberEntry = Entry(self.master, validate='key')
        self.contactNumberEntry['validatecommand'] = (self.contactNumberEntry.register(validation.ValidatePhoneNumber),
                                                      '%S', '%P', '%d')

        self.roomNoLbl = Label(self.master, text="Event Room Number:", font=style.textNormal, anchor='e', width=20,
                               bg=style.widgetBG)
        self.roomNoCombo = ttk.Combobox(self.master, value=self.roomNumbers, state='readonly',
                                        textvariable=self.roomComboText)
        self.roomNoCombo.bind('<<ComboboxSelected>>', self.room_pick)

        self.dateOfEventLbl = Label(self.master, text="Date of Event:", font=style.textNormal, anchor='e', width=20,
                                    bg=style.widgetBG)

        self.dateOfEventEntry = Entry(self.master, textvariable=self.dateOfEventValue, font=style.textNormal,
                                      state='readonly')
        self.dateOfEventEntry.bind('<Button-1>', self.selectDate)

        self.costPerHeadLbl = Label(self.master, text="Cost Per Head:", font=style.textNormal, anchor='e', width=20,
                                    bg=style.widgetBG)
        self.costPerHeadDisplay = Label(self.master, font=style.textNormal, anchor=W, width=20,
                                        text=mc.pound_string(0), bg=style.widgetBG)

        # grid layout
        self.noGuestsLbl.grid(row=0, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.noGuestsEntry.grid(row=0, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.nameOfContactLbl.grid(row=1, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.nameOfContactEntry.grid(row=1, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.addressLbl.grid(row=2, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.addressEntry.grid(row=2, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.contactNumberLbl.grid(row=3, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.contactNumberEntry.grid(row=3, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.roomNoLbl.grid(row=4, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.roomNoCombo.grid(row=4, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.dateOfEventLbl.grid(row=5, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.dateOfEventEntry.grid(row=5, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.costPerHeadLbl.grid(row=100, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.costPerHeadDisplay.grid(row=100, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

    def guests_entered(self):
        """method that checks that a number of guests greater than 0"""
        if 0 <= int(self.noGuestsEntry.get()) <= 100:
            return True
        return False

    def selectDate(self, event=None):
        """method to display calendar dialog when user clicks on the date of event entry"""
        startDate = self.dateOfEventValue.get() if self.dateOfEventValue.get() != '' else None
        tlf.calendar_popup(event, self.master, self.dateOfEventValue, startDate)

    def room_pick(self, event=None):
        if self.roomNoCombo.get() in self.roomNumbers:
            self.roomSelected = True
        else:
            self.roomSelected = False


    @abstractmethod
    def create_booking(self):
        """abstract method for each child class to have a method to create a booking once all infomration enterd
        correctly"""
        pass

    @abstractmethod
    def clear(self):
        """abstract method for all child classes to have a method to clear all user inputs in the create form"""
        pass


class CreateConference(BaseCreate):
    """Class based of BaseCreate class.  this class contains the extra UI elements and function to book and
    validate a conference"""
    def __init__(self, master):
        self.master = master
        super().__init__(master)
        # overriding room number configuration from parent class
        self.roomNumbers = CONST.CONFERENCE_ROOMS
        self.roomNoCombo.configure(values=self.roomNumbers)
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.conference_room_check(event=NONE))

        self.costPerHeadDisplay.configure(text=mc.pound_string(CONST.EVENT_COST_PER_HEAD.get('Conference')))

        self.projectorRequired = BooleanVar()

        # widgets
        self.companyLbl = Label(self.master, text="Company Name:", font=style.textNormal, anchor='e', width=20,
                                bg=style.widgetBG)
        self.companyEntry = Entry(self.master, font=style.textNormal, validate='key')
        self.companyEntry.configure(validatecommand=(self.companyEntry.register(validation.char_limit), '%P'))

        self.noOfDaysLbl = Label(self.master, text="Number of Days:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)

        self.noOfDaysValue = StringVar()
        self.noOfDaysEntry = Entry(self.master, validate='key', textvariable=self.noOfDaysValue)
        self.noOfDaysEntry.configure(validatecommand=(self.noOfDaysEntry.register(validation.NumbersOnly),
                                                      '%S', '%d'))
        self.noOfDaysValue.trace('wr', lambda name, index, mode: self.conference_room_check(event=None))

        self.projectorLbl = Label(self.master, text="Projector Required?:", font=style.textNormal, anchor='e', width=20,
                                  bg=style.widgetBG)
        self.projectorCheck = Checkbutton(self.master, variable=self.projectorRequired, bg=style.widgetBG)

        # layout for from
        self.companyLbl.grid(row=10, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.companyEntry.grid(row=10, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.noOfDaysLbl.grid(row=11, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.noOfDaysEntry.grid(row=11, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.projectorLbl.grid(row=12, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.projectorCheck.grid(row=12, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

    def conference_room_check(self, event):
        """Method that checks for free conference rooms for a given date if the room the user has selected is not free
        then there option is removed"""
        if self.dateOfEventValue.get() != '' and self.noOfDaysEntry.get() != '':
            db = da.DBAccess()
            bookedRooms = db.booked_conference_rooms(datetime.datetime.strptime(self.dateOfEventValue.get(), '%Y-%m-%d')
                                                     , int(self.noOfDaysEntry.get()))
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
                    self.roomComboText.set('Please select a Room')
                else:
                    self.roomComboText.set('No Rooms available')

            else:
                self.roomSelected = True

    def clear(self):
        """method to clear all inputs on the create form"""
        clear(self.master)
        self.dateOfEventValue.set('')
        self.roomComboText.set('Please select a Room')
        self.projectorRequired.set(False)

    def number_days_entered(self):
        """method to ensure that the number of days entered is greater than 0"""
        if 0 <= int(self.noOfDaysEntry.get()) <= 50:
            return True
        return False

    def create_booking(self):
        """method to create the conference booking and store it in the database if all validation is passed"""
        if not validation.EntriesNotEmpty(self.master):
            dialogs.not_completed(self.master)
        elif not self.guests_entered():
            dialogs.not_completed(self.master, 'Number of guests must be greater than 0')
        elif not self.number_days_entered():
            dialogs.not_completed(self.master, 'Number of days must be greater than 0 and no more than 30')
        elif not self.roomSelected:
            dialogs.not_completed(self.master, 'Room must be selected for Conference')
        else:
            db = da.DBAccess()
            c = Conference(noGuests=self.noGuestsEntry.get(),
                           nameofContact=self.nameOfContactEntry.get(),
                           address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                           eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                           companyName=self.companyEntry.get(), noOfDays=self.noOfDaysEntry.get(),
                           projectorRequired=self.projectorRequired.get(), dateofBooking=datetime.datetime.now().date(),
                           costPerhead=CONST.EVENT_COST_PER_HEAD.get('Conference'))
            db.insert_conference(c)
            dialogs.saved(self.master)
            back_to_main(self.master)


class CreateParty(BaseCreate):
    """class based on the baseCreate class that contains the extra UI elements and methods to book a party.  This class
    is also used as the base for the Create Wedding class"""
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # overriding parent values
        # overriding room number configuration from parent class
        self.roomNumbers = CONST.PARTY_ROOMS
        self.roomNoCombo.configure(values=self.roomNumbers)
        self.costPerHeadDisplay.configure(text=mc.pound_string(CONST.EVENT_COST_PER_HEAD.get('Party')))

        # overriding super date of event entry widget bind events
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeBands(list(CONST.BANDS.keys()), 'party'))
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeRooms(CONST.PARTY_ROOMS, 'party'))

        # party class variables
        self.bandCost = StringVar(self.master, mc.pound_string(0))
        self.bandOptions = list(CONST.BANDS.keys())
        self.bandSelected = StringVar(self.master, 'Please select a Band')
        self.bandPrice = 0

        self.bandNameLbl = Label(self.master, text="Select Band:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)
        self.bandName = ttk.Combobox(self.master, values=self.bandOptions, state='readonly',
                                     textvariable=self.bandSelected)
        self.bandName.bind('<<ComboboxSelected>>', self.band_options)

        self.bandCostLbl = Label(self.master, text="Band Cost:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)
        self.bandCostDisplay = Label(self.master, font=style.textNormal, textvariable=self.bandCost, anchor=W,
                                     width=20,
                                     bg=style.widgetBG)

        # grid layout for widgets
        self.bandNameLbl.grid(row=10, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.bandName.grid(row=10, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.bandCostLbl.grid(row=11, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.bandCostDisplay.grid(row=11, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

    def band_options(self, *args):
        """method to change the bandcost being display and the background band price being stored when the user selects
        an option in the band combobox"""
        bandPrice = CONST.BANDS.get(self.bandName.get())
        print(bandPrice)
        if bandPrice:
            self.bandCost.set(mc.pound_string(bandPrice))
            self.bandPrice = bandPrice
        else:
            self.bandCost.set(mc.pound_string(0))
            self.bandPrice = 0

    def create_booking(self):
        """method to create a party booking when and store it in the database when all validation has been passed"""
        if not validation.EntriesNotEmpty(self.master):
            dialogs.not_completed(self.master)
        elif not self.band_selected():
            dialogs.not_completed(self.master, 'Band must be selected')
        elif not self.guests_entered():
            dialogs.not_completed(self.master, 'Number of guests must be greater than 0')
        elif not self.roomSelected:
            dialogs.not_completed(self.master, 'Room must be selected for Party')
        else:
            db = da.DBAccess()
            p = Party(noGuests=self.noGuestsEntry.get(), nameofContact=self.nameOfContactEntry.get(),
                      address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                      eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                      bandName=self.bandName.get(), bandPrice=self.bandPrice,
                      costPerhead=CONST.EVENT_COST_PER_HEAD.get('Party'))
            db.insert_party(p)
            dialogs.saved(self.master)
            back_to_main(self.master)

    def band_selected(self):
        """method that returns true if the selected band name is in the bandOptions list else it returns false"""
        return True if self.bandName.get() in self.bandOptions else False

    def freeRooms(self, roomList, eventType, event=None):
        """method that checks for free rooms for a given event type on a the selected date and updates the room combobox
         to show only free rooms"""
        if self.dateOfEventEntry.get() != '':
            db = da.DBAccess()
            bookedRooms = db.getBookedRooms(eventType, self.dateOfEventValue.get())
            freeRooms = []
            for room in roomList:
                if room not in bookedRooms:
                    freeRooms.append(room)

            self.roomNumbers = freeRooms
            print(freeRooms)
            print(self.roomNumbers)
            print(bookedRooms)
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
        """method to check for free bands on the selected date and only show these is the band combobox.
        If user selected a band that is not free on a give date they must reselect their option"""
        if self.dateOfEventEntry.get() != '':
            db = da.DBAccess()
            bookedBands = db.getBookedBands(self.dateOfEventValue.get(), eventType)
            freeBands = []
            for band in bandList:
                if band not in bookedBands or band == 'No band selected':
                    freeBands.append(band)
            self.bandOptions = freeBands
            self.bandName.configure(values=self.bandOptions)
            if self.bandName.get() not in freeBands:
                self.bandName.delete(0, 'end')
                self.bandSelected.set('Please Select a Band')
                self.band_options()

    def clear(self):
        """method to clear all inputs on the create party form"""
        clear(self.master)
        self.roomComboText.set('Please select a Room')
        self.dateOfEventValue.set('')
        self.bandSelected.set('Please select a Band')


class CreateWedding(CreateParty):
    """class based on the CreateParty class and contain the extra UI elements and methods to validate and
    create a wedding booking"""
    def __init__(self, master):
        super().__init__(master)

        # overriding super room number options
        self.roomNumbers = CONST.WEDDING_ROOMS
        self.roomNoCombo.configure(values=self.roomNumbers)

        self.costPerHeadDisplay.configure(text=mc.pound_string(CONST.EVENT_COST_PER_HEAD.get('Wedding')))

        for ti in self.dateOfEventValue.trace_vinfo():
            self.dateOfEventValue.trace_vdelete(*ti)

        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeBands(list(CONST.BANDS.keys()), 'wedding'))
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeRooms(CONST.WEDDING_ROOMS, 'wedding'))

        # widgets for form
        self.noOfRoomsLbl = Label(self.master, text="Number of Rooms:", font=style.textNormal, anchor='e', width=20,
                                  bg=style.widgetBG)
        self.noOfRoomsEntry = Entry(self.master, font=style.textNormal, validate='key')
        self.noOfRoomsEntry.configure(
            validatecommand=(self.noOfRoomsEntry.register(validation.NumbersOnly), '%S', '%d'))

        # grid layout for widgets
        self.noOfRoomsLbl.grid(row=12, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.noOfRoomsEntry.grid(row=12, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

    def create_booking(self):
        """method to create a wedding booking and store it in the database if all validation is passed"""
        if not validation.EntriesNotEmpty(self.master):
            dialogs.not_completed(self.master)
        elif not self.band_selected():
            dialogs.not_completed(self.master, 'Band must be selected')
        elif not self.guests_entered():
            dialogs.not_completed(self.master, 'Number of guests must be greater than 0')
        elif not self.number_room_entered():
            dialogs.not_completed(self.master, 'Number of Rooms reserved must be 0 and no more than 1000')
        elif not self.roomSelected:
            dialogs.not_completed(self.master, 'Room must be selected for Wedding')
        else:
            db = da.DBAccess()
            w = Wedding(noGuests=self.noGuestsEntry.get(), nameofContact=self.nameOfContactEntry.get(),
                        address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                        eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                        bandName=self.bandName.get(), bandPrice=CONST.BANDS.get(self.bandName.get()),
                        costPerhead=CONST.EVENT_COST_PER_HEAD.get('Wedding'),
                        noBedroomsReserved=self.noOfRoomsEntry.get())
            db.insert_wedding(w)
            dialogs.saved(self.master)
            back_to_main(self.master)

    def number_room_entered(self):
        """method to ensure that a number of rooms entered is between 0 and 1000"""
        if 0 <= int(self.noOfRoomsEntry.get()) <= 1000:
            return True
        return False

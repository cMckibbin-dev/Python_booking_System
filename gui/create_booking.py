from tkinter import *
import tkinter.ttk as ttk
import tkcalendar
import constvalues as CONST
import gui.top_level_functions as tlf
from abc import abstractmethod
from gui import tkinter_styling as style
import validation
import money_convert as mc
from Data_Access import data_access as da
import datetime
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

        # CreateUI.set_default(context)  # calls the function to reset option menu
        # CreateUI.clear_date(context)  # calls the function to clear the date
        # CreateUI.clear_check(context)  # calls the function to clear the checkbox


class CreateMenu:
    def __init__(self, master):
        self.master = master
        self.master.configure(background=style.windowBG)
        self.master.title('Create Booking')

        self.master.protocol('WM_DELETE_WINDOW', self.back_to_main_menu)

        self.UI = None  # variable used to  store UI class being displayed in UI_Frame
        self.buttonActive = False  # boolean to track when the save and clear buttons are in normal state

        self.title = Label(self.master, text='Create New Booking', font=style.textHeading, bg=style.widgetBG)
        self.chooseEventTypeLabel = Label(self.master, text='Choose Event Type:', font=style.textNormal,
                                          bg=style.widgetBG)
        self.eventTypeVar = StringVar(self.master, 'Choose Event Type')
        self.chooseEventTypeCombobox = ttk.Combobox(self.master, state='readonly', font=style.textNormal,
                                                    value=CONST.EVENT_TYPES, textvariable=self.eventTypeVar)
        self.chooseEventTypeCombobox.bind('<<ComboboxSelected>>', self.display_Create_form)

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
        self.chooseEventTypeCombobox.grid(row=1, column=1, padx=style.paddingX, pady=style.paddingY, sticky=W)
        self.UI_Frame.grid(row=2, column=0, columnspan=2)
        self.buttonFrame.grid(row=3, column=0, columnspan=2)
        self.backButton.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)
        self.clearButton.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)
        self.saveButton.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)

    def display_Create_form(self, event=None):
        eventDic = {'Conference': CreateConference, 'Party': CreateParty, 'Wedding': CreateWedding}
        self.UI = eventDic.get(self.chooseEventTypeCombobox.get())
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
        self.master.destroy()
        root = Tk()
        main_menu.MainMenuUI(root)
        root.mainloop()


class BaseCreate:
    def __init__(self, master):
        self.master = master

        self.roomNumbers = []
        self.roomComboText = StringVar(self.master, 'Please select a Room')

        self.dateOfEventValue = StringVar()

        self.noGuestsLbl = Label(self.master, text="Number of Guests:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)

        self.noGuestsEntry = Entry(self.master, validate='key')
        self.noGuestsEntry.configure(validatecommand=(self.noGuestsEntry.register(validation.NumbersOnly), '%S', '%d'))

        self.nameOfContactLbl = Label(self.master, text="Name of Contact:", font=style.textNormal, anchor='e', width=20,
                                      bg=style.widgetBG)

        self.nameOfContactEntry = Entry(self.master, validate='key')
        self.nameOfContactEntry.configure(validatecommand=(self.nameOfContactEntry.register(validation.lettersOnly),
                                                           '%S', '%d'))

        self.addressLbl = Label(self.master, text="Full Address of Contact:", font=style.textNormal, anchor='e',
                                width=20,
                                bg=style.widgetBG)
        self.addressEntry = Entry(self.master, validate='key')
        self.addressEntry.configure(
            validatecommand=(self.addressEntry.register(validation.noSpecialCharacter), '%S', '%d'))

        self.contactNumberLbl = Label(self.master, text="Contact Number:", font=style.textNormal, anchor='e', width=20,
                                      bg=style.widgetBG)
        self.contactNumberEntry = Entry(self.master, validate='key')
        self.contactNumberEntry['validatecommand'] = (self.contactNumberEntry.register(validation.NumbersOnly),
                                                      '%S', '%d')

        self.roomNoLbl = Label(self.master, text="Event Room Number:", font=style.textNormal, anchor='e', width=20,
                               bg=style.widgetBG)
        self.roomNoCombo = ttk.Combobox(self.master, value=self.roomNumbers, state='readonly',
                                        textvariable=self.roomComboText)

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
        if int(self.noGuestsEntry.get()) > 0:
            return True
        return False

    def selectDate(self, event=None):
        startDate = self.dateOfEventValue.get() if self.dateOfEventValue.get() != '' else None
        tlf.calendar_popup(event, self.master, self.dateOfEventValue, startDate)

    @abstractmethod
    def create_booking(self):
        pass

    @abstractmethod
    def clear(self):
        pass


class CreateConference(BaseCreate):
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
        self.companyEntry = Entry(self.master, font=style.textNormal)

        self.noOfDaysLbl = Label(self.master, text="Number of Days:", font=style.textNormal, anchor='e', width=20,
                                 bg=style.widgetBG)

        self.noOfDaysEntry = Entry(self.master, validate='key')
        self.noOfDaysEntry.configure(validatecommand=(self.noOfDaysEntry.register(validation.NumbersOnly), '%S', '%d'))
        self.noOfDaysEntry.bind('<Leave>', self.conference_room_check)
        self.noOfDaysEntry.bind('<FocusOut>', self.conference_room_check)

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
                self.roomNoCombo.delete(0, 'end')
                if len(freeRooms) > 0:
                    self.roomComboText.set('Select an Option')
                else:
                    self.roomComboText.set('No Rooms available for this date')

    def number_days_entered(self):
        if int(self.noOfDaysEntry.get()) > 0:
            return True
        return False

    def clear(self):
        clear(self.master)
        self.dateOfEventValue.set('')
        self.roomComboText.set('Please select a Room')
        self.projectorRequired.set(False)

    def create_booking(self):
        if not validation.EntriesNotEmpty(self.master):
            dialogs.not_completed(self.master)
        elif not self.guests_entered():
            dialogs.not_completed(self.master, 'Number of guests must be greater than 0')
        elif not self.number_days_entered():
            dialogs.not_completed(self.master, 'Number of days must be greater than 0')
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
            self.master.destroy()
            print('Created booking')


class CreateParty(BaseCreate):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # overriding parent values
        # overriding room number configuration from parent class
        self.roomNumbers = CONST.PARTY_ROOMS
        self.roomNoCombo.configure(values=self.roomNumbers)
        self.costPerHeadDisplay.configure(text=mc.pound_string(CONST.EVENT_COST_PER_HEAD.get('Party')))

        # overriding super date of event entry widget bind events
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeBands(list(CONST.BANDS.keys())))
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeRooms(CONST.PARTY_ROOMS))

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

        bandPrice = CONST.BANDS.get(self.bandName.get())
        print(bandPrice)
        if bandPrice:
            self.bandCost.set(mc.pound_string(bandPrice))
            self.bandPrice = bandPrice
        else:
            self.bandCost.set(mc.pound_string(0))
            self.bandPrice = 0

    def create_booking(self):
        if not validation.EntriesNotEmpty(self.master):
            dialogs.not_completed(self.master)
        elif not self.band_selected():
            dialogs.not_completed(self.master, 'Band must be selected')
        elif not self.guests_entered():
            dialogs.not_completed(self.master, 'Number of guests must be greater than 0')
        else:
            db = da.DBAccess()
            p = Party(noGuests=self.noGuestsEntry.get(), nameofContact=self.nameOfContactEntry.get(),
                      address=self.addressEntry.get(), contactNo=self.contactNumberEntry.get(),
                      eventRoomNo=self.roomNoCombo.get(), dateOfEvent=self.dateOfEventEntry.get(),
                      bandName=self.bandName.get(), bandPrice=self.bandPrice,
                      costPerhead=CONST.EVENT_COST_PER_HEAD.get('Party'))
            db.insert_party(p)
            dialogs.saved(self.master)
            self.master.destroy()

    def band_selected(self):
        return True if self.bandName.get() in self.bandOptions else False

    def freeRooms(self, roomList, event=None):
        if self.dateOfEventEntry.get() != '':
            db = da.DBAccess()
            bookedRooms = db.getBookedRooms('party', self.dateOfEventValue.get())
            freeRooms = []
            for room in roomList:
                if room not in bookedRooms:
                    freeRooms.append(room)
                self.roomNumbers = freeRooms
            self.roomNoCombo.configure(values=self.roomNumbers)
            if self.roomNoCombo.get() not in freeRooms:
                self.roomNoCombo.delete(0, 'end')
                self.roomComboText.set('Please Select a Room')

    def freeBands(self, bandList, event=None, ):
        if self.dateOfEventEntry.get() != '':
            db = da.DBAccess()
            bookedBands = db.getBookedBands(self.dateOfEventValue.get(), 'party')
            freeBands = []
            for band in bandList:
                if band not in bookedBands or 'No band selected':
                    freeBands.append(band)
            self.bandOptions = freeBands
            self.bandName.configure(values=self.bandOptions)
            if self.bandName.get() not in freeBands:
                self.bandName.delete(0, 'end')
                self.bandSelected.set('Please Select a Band')
                self.band_options()

    def clear(self):
        clear(self.master)
        self.roomComboText.set('Please select a Room')
        self.dateOfEventValue.set('')
        self.bandSelected.set('Please select a Band')


class CreateWedding(CreateParty):
    def __init__(self, master):
        super().__init__(master)

        # overriding super room number options
        self.roomNumbers = CONST.WEDDING_ROOMS
        self.roomNoCombo.configure(values=self.roomNumbers)

        for ti in self.dateOfEventValue.trace_vinfo():
            self.dateOfEventValue.trace_vdelete(*ti)

        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeBands(list(CONST.BANDS.keys())))
        self.dateOfEventValue.trace('w', lambda name, index, mode: self.freeRooms(CONST.WEDDING_ROOMS))

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
        if not validation.EntriesNotEmpty(self.master):
            dialogs.not_completed(self.master)
        elif not self.band_selected():
            dialogs.not_completed(self.master, 'Band must be selected')
        elif not self.guests_entered():
            dialogs.not_completed(self.master, 'Number of guests must be greater than 0')
        elif not self.number_room_entered():
            dialogs.not_completed(self.master, 'Number of Rooms reserved must be 0 or greater')
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
            self.master.destroy()

    def number_room_entered(self):
        if 0 <= int(self.noOfRoomsEntry.get()) <= 200:
            return True
        return False

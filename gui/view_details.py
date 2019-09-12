from tkinter import *


class BaseViewDetail:
    """class is used a base class for the other view details classes"""
    def __init__(self, master, event):
        self.master = master
        self.event = event

        # window configure
        self.master.title('View Details')

        # setting text formatting vars and padding vars
        self.textHeading = 'Helvetica 18 bold'
        self.textNormal = 'Helvetica 12'
        self.paddingX = 5
        self.paddingY = 5

        # labels for form
        # heading label is given text value by child classes
        self.Heading = Label(self.master, text='heading', font=self.textHeading)

        # Number of Guests labels
        self.noGuestsTitle = Label(self.master, text='Number of Guests:', font=self.textNormal)
        self.noGuestsInfo = Label(self.master, text=event.noGuests, font=self.textNormal)

        # Name of Contact Labels
        self.nameContactTitle = Label(self.master, text='Name of Contact:', font=self.textNormal)
        self.nameContactInfo = Label(self.master, text=event.nameofContact, font=self.textNormal)

        # Address Labels
        self.addressTitle = Label(self.master, text='Full Address of Contact:', font=self.textNormal)
        self.addressInfo = Label(self.master, text=event.address, font=self.textNormal)

        # Contact Number Labels
        self.contactNumberTitle = Label(self.master, text='Contact Number:', font=self.textNormal)
        self.contactNumberInfo = Label(self.master, text=event.contactNo, font=self.textNormal)

        # Event Room Number Label
        self.roomNumberTitle = Label(self.master, text='Event Room Number:', font=self.textNormal)
        self.roomNumberInfo = Label(self.master, text=event.eventRoomNo, font=self.textNormal)

        # Date of Booking Labels
        self.dateOfBookingTitle = Label(self.master, text='Date of Booking:', font=self.textNormal)
        self.dateOfBookingInfo = Label(self.master, text=event.dateOfBooking, font=self.textNormal)

        # Date of Event Labels
        self.dateOfEventTitle = Label(self.master, text='Date of Event', font=self.textNormal)
        self.dateOfEventInfo = Label(self.master, text=event.dateOfEvent, font=self.textNormal)

        # cost per head labels
        self.costPerHeadTitle = Label(self.master, text='Cost Per Head:', font=self.textNormal)
        self.costPerHeadInfo = Label(self.master, text=event.costPerhead, font=self.textNormal)

        # buttons
        # these buttons are user on each child class and should be placed at the bottom
        self.buttonBack = Button(self.master, text='Back', font=self.textNormal, bg='white')
        self.buttonEdit = Button(self.master, text='Edit', font=self.textNormal, bg='red')
        self.buttonInvoice = Button(self.master, text='Invoice', font=self.textNormal, bg='blue')

        # placing widgets on grid layout
        # placing heading title
        self.Heading.grid(row=0, column=0, columnspan=3, sticky=NSEW, padx=self.paddingX, pady=self.paddingY)

        # placing Title and Info labels for each of the Event details
        self.noGuestsTitle.grid(row=1, column=1, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.noGuestsInfo.grid(row=1, column=2, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.nameContactTitle.grid(row=2, column=1, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.nameContactInfo.grid(row=2, column=2, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.addressTitle.grid(row=3, column=1, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.addressInfo.grid(row=3, column=2, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.contactNumberTitle.grid(row=4, column=1, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.contactNumberInfo.grid(row=4, column=2, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.roomNumberTitle.grid(row=5, column=1, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.roomNumberInfo.grid(row=5, column=2, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.dateOfBookingTitle.grid(row=6, column=1, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.dateOfBookingInfo.grid(row=6, column=2, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.dateOfEventTitle.grid(row=7, column=1, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.dateOfEventInfo.grid(row=7, column=2, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.costPerHeadTitle.grid(row=100, column=1, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.costPerHeadInfo.grid(row=100, column=2, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.buttonBack.grid(row=101, column=0, sticky=NSEW, padx=self.paddingX, pady=self.paddingY)
        self.buttonEdit.grid(row=101, column=1, sticky=NSEW, padx=self.paddingX, pady=self.paddingY)
        self.buttonInvoice.grid(row=101, column=2, sticky=NSEW, padx=self.paddingX, pady=self.paddingY)

        # setting weight and uniform for and column in grid
        self.master.grid_columnconfigure(0, weight=0, uniform='fred')
        self.master.grid_columnconfigure(1, weight=0, uniform='fred')
        self.master.grid_columnconfigure(2, weight=0, uniform='fred')

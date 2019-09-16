from tkinter import *
from classes import *
from gui import top_level_functions as tl
from gui import update


class BaseViewDetail:
    """class is used a base class for the other view details classes"""

    def __init__(self, master, event):
        self.master = master
        self.event = event

        # window configure
        self.master.title('View Details')
        self.master.configure(background='white')
        # setting text formatting vars and padding vars
        self.textHeading = 'Helvetica 18 bold'
        self.textNormal = 'Helvetica 12'
        self.paddingX = 5
        self.paddingY = 5
        # button sizes
        self.buttonWidth = 10
        self.buttonHeight = 2
        # widget background colour
        self.widgetBG = 'white'

        # labels for form
        # heading label is given text value by child classes
        self.Heading = Label(self.master, text='heading', font=self.textHeading, bg=self.widgetBG)

        # Number of Guests labels
        self.noGuestsTitle = Label(self.master, text='Number of Guests:', font=self.textNormal, bg=self.widgetBG)
        self.noGuestsInfo = Label(self.master, text=event.noGuests, font=self.textNormal, bg=self.widgetBG)

        # Name of Contact Labels
        self.nameContactTitle = Label(self.master, text='Name of Contact:', font=self.textNormal, bg=self.widgetBG)
        self.nameContactInfo = Label(self.master, text=event.nameofContact, font=self.textNormal, bg=self.widgetBG)

        # Address Labels
        self.addressTitle = Label(self.master, text='Full Address of Contact:', font=self.textNormal, bg=self.widgetBG)
        self.addressInfo = Label(self.master, text=event.address, font=self.textNormal, bg=self.widgetBG)

        # Contact Number Labels
        self.contactNumberTitle = Label(self.master, text='Contact Number:', font=self.textNormal, bg=self.widgetBG)
        self.contactNumberInfo = Label(self.master, text=event.contactNo, font=self.textNormal, bg=self.widgetBG)

        # Event Room Number Label
        self.roomNumberTitle = Label(self.master, text='Event Room Number:', font=self.textNormal, bg=self.widgetBG)
        self.roomNumberInfo = Label(self.master, text=event.eventRoomNo, font=self.textNormal, bg=self.widgetBG)

        # Date of Booking Labels
        self.dateOfBookingTitle = Label(self.master, text='Date of Booking:', font=self.textNormal, bg=self.widgetBG)
        self.dateOfBookingInfo = Label(self.master, text=event.dateOfBooking, font=self.textNormal, bg=self.widgetBG)

        # Date of Event Labels
        self.dateOfEventTitle = Label(self.master, text='Date of Event', font=self.textNormal, bg=self.widgetBG)
        self.dateOfEventInfo = Label(self.master, text=event.dateOfEvent, font=self.textNormal, bg=self.widgetBG)

        # cost per head labels
        self.costPerHeadTitle = Label(self.master, text='Cost Per Head:', font=self.textNormal, bg=self.widgetBG)
        self.costPerHeadInfo = Label(self.master, text=event.costPerhead, font=self.textNormal, bg=self.widgetBG)

        # frame for packing buttons at bottom of form
        self.buttonFrame = Frame(self.master, bg=self.widgetBG)
        # buttons
        # these buttons are user on each child class and should be placed at the bottom
        self.buttonBack = Button(self.buttonFrame, text='Back', font=self.textNormal, bg='snow', width=self.buttonWidth
                                 , height=self.buttonHeight, command=self.master.destroy)

        self.buttonInvoice = Button(self.buttonFrame, text='Invoice', font=self.textNormal, bg='deep sky blue',
                                    width=self.buttonWidth, height=self.buttonHeight)

        # placing widgets on grid layout
        # placing heading title
        self.Heading.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=self.paddingX, pady=self.paddingY)

        # placing Title and Info labels for each of the Event details
        self.noGuestsTitle.grid(row=1, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.noGuestsInfo.grid(row=1, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.nameContactTitle.grid(row=2, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.nameContactInfo.grid(row=2, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.addressTitle.grid(row=3, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.addressInfo.grid(row=3, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.contactNumberTitle.grid(row=4, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.contactNumberInfo.grid(row=4, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.roomNumberTitle.grid(row=5, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.roomNumberInfo.grid(row=5, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.dateOfBookingTitle.grid(row=6, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.dateOfBookingInfo.grid(row=6, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.dateOfEventTitle.grid(row=7, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.dateOfEventInfo.grid(row=7, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.costPerHeadTitle.grid(row=100, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.costPerHeadInfo.grid(row=100, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.buttonFrame.grid(row=101, column=0, columnspan=2)

        self.buttonBack.pack(side=LEFT, padx=self.paddingX, pady=self.paddingY)
        self.buttonInvoice.pack(side=LEFT, padx=self.paddingX, pady=self.paddingY)


class ViewDetailsConference(BaseViewDetail):
    """Class for the view details UI for Conference Class based of the BaseViewDetails class"""

    def __init__(self, master, event):
        super().__init__(master, event)

        # overriding the default heading
        self.Heading.configure(text='View Details Conference')
        # Company Name labels
        self.companyNameTitle = Label(self.master, text='Company Name:', font=self.textNormal, bg=self.widgetBG)
        self.companyNameInfo = Label(self.master, text=self.event.companyName, font=self.textNormal, bg=self.widgetBG)

        # Number of Days Labels
        self.numberOfDaysTitle = Label(self.master, text='Number of Days:', font=self.textNormal, bg=self.widgetBG)
        self.numberOfDaysInfo = Label(self.master, text=self.event.noOfDays, font=self.textNormal, bg=self.widgetBG)

        # Projector Required Labels
        self.projectorRequiredTitle = Label(self.master, text='Projector Required:', font=self.textNormal,
                                            bg=self.widgetBG)
        self.projectorRequiredInfo = Label(self.master, text='Yes' if event.projectorRequired else 'No',
                                           font=self.textNormal, bg=self.widgetBG)

        # layout for labels
        self.companyNameTitle.grid(row=8, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.companyNameInfo.grid(row=8, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.numberOfDaysTitle.grid(row=8, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.numberOfDaysInfo.grid(row=8, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.numberOfDaysTitle.grid(row=9, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.numberOfDaysInfo.grid(row=9, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.projectorRequiredTitle.grid(row=10, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.projectorRequiredInfo.grid(row=10, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)


class ViewDetailsParty(BaseViewDetail):
    """Class for the view details UI for Party Class based of the BaseViewDetails class"""

    def __init__(self, master, event):
        super().__init__(master, event)
        # overriding default heading
        self.Heading.configure(text='View Details Party')
        # labels for Band Selected
        self.bandSelectedTitle = Label(self.master, text='Band Selected:', font=self.textNormal, bg=self.widgetBG)
        self.bandSelectedInfo = Label(self.master, text=event.bandName, font=self.textNormal, bg=self.widgetBG)

        # labels for band cost
        self.bandCostTitle = Label(self.master, text='Band Cost:', font=self.textNormal, bg=self.widgetBG)
        self.bandCostInfo = Label(self.master, text=event.bandPrice, font=self.textNormal, bg=self.widgetBG)

        # layout for labels
        self.bandSelectedTitle.grid(row=8, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.bandSelectedInfo.grid(row=8, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)
        self.bandCostTitle.grid(row=9, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.bandCostInfo.grid(row=9, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)


class ViewDetailsWedding(ViewDetailsParty):
    """Class for the view details UI for Wedding Class based of the ViewDetailsParty class"""

    def __init__(self, master, event):
        super().__init__(master, event)
        # overriding the default heading
        self.Heading.configure(text='View Details Wedding')
        # labels for Number of Bed rooms Reserved
        self.NumberRoomsTitle = Label(self.master, text='Number of Rooms\nReserved:', font=self.textNormal,
                                      bg=self.widgetBG)
        self.NumberRoomsInfo = Label(self.master, text=event.noBedroomsReserved, font=self.textNormal, bg=self.widgetBG)
        # layout for labels
        self.NumberRoomsTitle.grid(row=10, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.NumberRoomsInfo.grid(row=10, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

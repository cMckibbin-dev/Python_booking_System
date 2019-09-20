from tkinter import *
import money_convert as mc
from gui import tkinter_styling as style
from invoice_templates import invoice_generator as ig


def CostBreakDownUI(master, booking):
    """function creates the UI for the cost breakdown section on the invoice Section of the window"""
    # widgets for invoice form
    CostBreakHeading = Label(master, text='Cost Break Down', font=style.textHeading, bg=style.widgetBG)
    totalExVATLabel = Label(master, text='Total ex VAT:', font=style.textNormal, bg=style.widgetBG)
    totalExVATInfo = Label(master, text=mc.pound_string(booking.subTotal()), font=style.textNormal, bg=style.widgetBG)

    VATTotalLabel = Label(master, text='VAT:', font=style.textNormal, bg=style.widgetBG)
    VATTotalInfo = Label(master, text=mc.pound_string(booking.VAT()), font=style.textNormal, bg=style.widgetBG)

    TotalLabel = Label(master, text='Total:', font=style.textNormal, bg=style.widgetBG)
    TotalInfo = Label(master, text=mc.pound_string(booking.total()), font=style.textNormal, bg=style.widgetBG)

    # grid layout for widgets
    CostBreakHeading.grid(row=20, column=0, columnspan=2, sticky=NSEW, padx=style.paddingX, pady=style.paddingY)

    totalExVATLabel.grid(row=21, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
    totalExVATInfo.grid(row=21, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

    VATTotalLabel.grid(row=22, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
    VATTotalInfo.grid(row=22, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

    TotalLabel.grid(row=23, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
    TotalInfo.grid(row=23, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)


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
        style.paddingX = 5
        style.paddingY = 5
        # button sizes
        style.buttonWidth = 10
        style.buttonHeight = 2
        # widget background colour
        style.widgetBG = 'white'

        # labels for form
        # heading label is given text value by child classes
        self.Heading = Label(self.master, text='heading', font=self.textHeading, bg=style.widgetBG)

        # Number of Guests labels
        self.noGuestsTitle = Label(self.master, text='Number of Guests:', font=self.textNormal, bg=style.widgetBG)
        self.noGuestsInfo = Label(self.master, text=event.noGuests, font=self.textNormal, bg=style.widgetBG)

        # Name of Contact Labels
        self.nameContactTitle = Label(self.master, text='Name of Contact:', font=self.textNormal, bg=style.widgetBG)
        self.nameContactInfo = Label(self.master, text=event.nameofContact, font=self.textNormal, bg=style.widgetBG)

        # Address Labels
        self.addressTitle = Label(self.master, text='Full Address of Contact:', font=self.textNormal, bg=style.widgetBG)
        self.addressInfo = Label(self.master, text=event.address, font=self.textNormal, bg=style.widgetBG)

        # Contact Number Labels
        self.contactNumberTitle = Label(self.master, text='Contact Number:', font=self.textNormal, bg=style.widgetBG)
        self.contactNumberInfo = Label(self.master, text=event.contactNo, font=self.textNormal, bg=style.widgetBG)

        # Event Room Number Label
        self.roomNumberTitle = Label(self.master, text='Event Room Number:', font=self.textNormal, bg=style.widgetBG)
        self.roomNumberInfo = Label(self.master, text=event.eventRoomNo, font=self.textNormal, bg=style.widgetBG)

        # Date of Booking Labels
        self.dateOfBookingTitle = Label(self.master, text='Date of Booking:', font=self.textNormal, bg=style.widgetBG)
        self.dateOfBookingInfo = Label(self.master, text=event.dateOfBooking, font=self.textNormal, bg=style.widgetBG)

        # Date of Event Labels
        self.dateOfEventTitle = Label(self.master, text='Date of Event', font=self.textNormal, bg=style.widgetBG)
        self.dateOfEventInfo = Label(self.master, text=event.dateOfEvent, font=self.textNormal, bg=style.widgetBG)

        # cost per head labels
        self.costPerHeadTitle = Label(self.master, text='Cost Per Head:', font=self.textNormal, bg=style.widgetBG)
        self.costPerHeadInfo = Label(self.master, text=mc.pound_string(event.costPerhead), font=self.textNormal,
                                     bg=style.widgetBG)

        # frame for packing buttons at bottom of form
        self.buttonFrame = Frame(self.master, bg=style.widgetBG)
        # buttons
        # these buttons are user on each child class and should be placed at the bottom
        self.buttonBack = Button(self.buttonFrame, text='Back', font=self.textNormal, bg='snow', width=style.buttonWidth
                                 , height=style.buttonHeight, command=self.master.destroy)

        self.buttonInvoice = Button(self.buttonFrame, text='Save Invoice', font=self.textNormal, bg='deep sky blue',
                                    width=style.buttonWidth, height=style.buttonHeight)

        # placing widgets on grid layout
        # placing heading title
        self.Heading.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=style.paddingX, pady=style.paddingY)

        # placing Title and Info labels for each of the Event details
        self.noGuestsTitle.grid(row=1, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.noGuestsInfo.grid(row=1, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.nameContactTitle.grid(row=2, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.nameContactInfo.grid(row=2, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.addressTitle.grid(row=3, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.addressInfo.grid(row=3, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.contactNumberTitle.grid(row=4, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.contactNumberInfo.grid(row=4, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.roomNumberTitle.grid(row=5, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.roomNumberInfo.grid(row=5, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.dateOfBookingTitle.grid(row=6, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.dateOfBookingInfo.grid(row=6, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.dateOfEventTitle.grid(row=7, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.dateOfEventInfo.grid(row=7, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.costPerHeadTitle.grid(row=19, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.costPerHeadInfo.grid(row=19, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        CostBreakDownUI(self.master, self.event)

        self.buttonFrame.grid(row=24, column=0, columnspan=2)

        self.buttonBack.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)
        self.buttonInvoice.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)


class ViewDetailsConference(BaseViewDetail):
    """Class for the view details UI for Conference Class based of the BaseViewDetails class"""

    def __init__(self, master, event):
        super().__init__(master, event)

        # overriding the default heading
        self.Heading.configure(text='View Details Conference')
        # Company Name labels
        self.companyNameTitle = Label(self.master, text='Company Name:', font=self.textNormal, bg=style.widgetBG)
        self.companyNameInfo = Label(self.master, text=self.event.companyName, font=self.textNormal, bg=style.widgetBG)

        # Number of Days Labels
        self.numberOfDaysTitle = Label(self.master, text='Number of Days:', font=self.textNormal, bg=style.widgetBG)
        self.numberOfDaysInfo = Label(self.master, text=self.event.noOfDays, font=self.textNormal, bg=style.widgetBG)

        # Projector Required Labels
        self.projectorRequiredTitle = Label(self.master, text='Projector Required:', font=self.textNormal,
                                            bg=style.widgetBG)
        self.projectorRequiredInfo = Label(self.master, text='Yes' if event.projectorRequired else 'No',
                                           font=self.textNormal, bg=style.widgetBG)

        self.buttonInvoice.configure(command=lambda: ig.Conference_Invoice(self.event))

        # layout for labels
        self.companyNameTitle.grid(row=8, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.companyNameInfo.grid(row=8, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.numberOfDaysTitle.grid(row=8, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.numberOfDaysInfo.grid(row=8, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.numberOfDaysTitle.grid(row=9, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.numberOfDaysInfo.grid(row=9, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

        self.projectorRequiredTitle.grid(row=10, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.projectorRequiredInfo.grid(row=10, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)


class ViewDetailsParty(BaseViewDetail):
    """Class for the view details UI for Party Class based of the BaseViewDetails class"""

    def __init__(self, master, event):
        super().__init__(master, event)
        # overriding default heading
        self.Heading.configure(text='View Details Party')
        self.buttonInvoice.configure(command=lambda: ig.party_invoice(self.event))
        # labels for Band Selected
        self.bandSelectedTitle = Label(self.master, text='Band Selected:', font=self.textNormal, bg=style.widgetBG)
        self.bandSelectedInfo = Label(self.master, text=event.bandName, font=self.textNormal, bg=style.widgetBG)

        # labels for band cost
        self.bandCostTitle = Label(self.master, text='Band Cost:', font=self.textNormal, bg=style.widgetBG)
        self.bandCostInfo = Label(self.master, text=mc.pound_string(event.bandPrice), font=self.textNormal,
                                  bg=style.widgetBG)

        # layout for labels
        self.bandSelectedTitle.grid(row=8, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.bandSelectedInfo.grid(row=8, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)
        self.bandCostTitle.grid(row=9, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.bandCostInfo.grid(row=9, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)


class ViewDetailsWedding(ViewDetailsParty):
    """Class for the view details UI for Wedding Class based of the ViewDetailsParty class"""

    def __init__(self, master, event):
        super().__init__(master, event)
        # overriding the default heading
        self.Heading.configure(text='View Details Wedding')
        self.buttonInvoice.configure(command=lambda: ig.wedding_invoice(self.event))
        # labels for Number of Bed rooms Reserved
        self.NumberRoomsTitle = Label(self.master, text='Number of Rooms\nReserved:', font=self.textNormal,
                                      bg=style.widgetBG)
        self.NumberRoomsInfo = Label(self.master, text=event.noBedroomsReserved, font=self.textNormal,
                                     bg=style.widgetBG)
        # layout for labels
        self.NumberRoomsTitle.grid(row=10, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.NumberRoomsInfo.grid(row=10, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

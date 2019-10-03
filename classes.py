import datetime


# Base class
class Event:
    """Base class and constructor that contains the details shared between all events"""

    def __init__(self, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, costPerhead,
                 dateOfBooking=None, ID=None):
        self.id = ID
        self.nameofContact = nameofContact
        self.noGuests = noGuests
        self.address = address
        self.contactNo = contactNo
        self.eventRoomNo = eventRoomNo
        self.dateOfEvent = dateOfEvent
        self.costPerhead = costPerhead
        self.dateOfBooking = datetime.datetime.now().date() if dateOfBooking is None else dateOfBooking

    def costPerHeadTotal(self):
        """Function that works out the total costs for guests using the cost per head """
        return float(self.costPerhead * self.noGuests)


# Conference class which extends event
class Conference(Event):
    """Conference class that inherits from the event base class"""

    def __init__(self, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, companyName, noOfDays,
                 projectorRequired, dateofBooking=None, costPerhead=None, ID=None):
        super().__init__(noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, costPerhead,
                         dateofBooking, ID)  # initializes the shared attributes from the base class

        # initializes the unique attributes for conference
        self.companyName = companyName
        self.noOfDays = noOfDays
        self.projectorRequired = projectorRequired
        self.costPerhead = 20 if costPerhead is None else costPerhead

    def total(self):
        """Works out the total cost including VAT"""
        return float(self.subTotal() + self.VAT())

    def subTotal(self):
        """Works out subtotal excluding Vat"""
        return float(self.noGuests * self.costPerhead) * self.noOfDays

    def VAT(self):
        """works out VAT"""
        return float(self.subTotal() / 5)

    def PricePerDay(self):
        """Works out the cost per day"""
        return float(self.noGuests * self.costPerhead)


# Party class which extends event
class Party(Event):
    """Party class that inherits from the event base class"""
    def __init__(self, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, bandName,
                 bandPrice, dateofBooking=None, costPerhead=None, ID=None):
        super().__init__(noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, costPerhead,
                         dateofBooking, ID)  # initializes the shared attributes from the base class

        # initializes the unique attributes for party
        self.bandName = bandName
        self.bandPrice = bandPrice
        self.costPerhead = 15 if costPerhead is None else costPerhead

    def total(self):
        """Works out the total cost including VAT"""
        return self.subTotal() + self.VAT()

    def subTotal(self):
        """Works out subtotal excluding Vat"""
        return (self.costPerhead * self.noGuests) + self.bandPrice

    def VAT(self):
        """works out VAT"""
        return self.subTotal() / 5


# Wedding class which extends party
class Wedding(Party):
    """Party class that inherits from the party class, this also inherits its functions"""
    def __init__(self, bandName, bandPrice, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent,
                 noBedroomsReserved, dateOfBooking=None, costPerhead=None, ID=None):
        super().__init__(noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, bandName, bandPrice,
                         dateOfBooking, costPerhead, ID)  # initializes the shared attributes from the party class

        # initializes the unique attributes for wedding
        self.noBedroomsReserved = noBedroomsReserved
        self.costPerhead = 30 if costPerhead is None else costPerhead



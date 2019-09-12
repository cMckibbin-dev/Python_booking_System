import datetime


class Event:
    def __init__(self, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, costPerhead,
                 dateOfBooking=None):
        self.nameofContact = nameofContact
        self.noGuests = noGuests
        self.address = address
        self.contactNo = contactNo
        self.eventRoomNo = eventRoomNo
        self.dateOfEvent = dateOfEvent
        self.costPerhead = costPerhead
        self.dateOfBooking = datetime.datetime.now() if dateOfBooking is None else dateOfBooking

    def total(self):
        subtotal = self.noGuests * self.costPerhead
        vat = subtotal / 5
        return subtotal + vat


class Conference(Event):
    def __init__(self, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, companyName, noOfDays,
                 projectorRequired, dateofBooking=None, costPerhead=None):
        super().__init__(noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, dateofBooking, costPerhead)
        self.companyName = companyName
        self.noOfDays = noOfDays
        self.projectorRequired = projectorRequired
        self.costPerhead = 20 if costPerhead is None else costPerhead

    def total(self):
        subtotal = self.noGuests * self.costPerhead
        vat = subtotal / 5
        return subtotal + vat


class Party(Event):
    def __init__(self, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, bandName,
                bandPrice, dateofBooking=None, costPerhead=None):
        super().__init__(noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, dateofBooking, costPerhead)
        self.bandName = bandName
        self.bandPrice = bandPrice
        self.costPerhead = 15 if costPerhead is None else costPerhead

    def total(self):
        subtotal = (self.costPerhead * self.noGuests) + self.bandPrice
        vat = subtotal / 5
        return subtotal + vat


class Wedding(Party):
    def __init__(self, bandName, bandPrice, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent,
                 noBedroomsReserved, dateOfBooking = None, costPerhead=None):
        super().__init__(noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, bandName,
                         bandPrice, dateOfBooking, costPerhead)
        self.noBedroomsReserved = noBedroomsReserved
        self.costPerhead = 30 if costPerhead is None else costPerhead

    def total(self):
        subtotal = (self.costPerhead * self.noGuests) + self.bandPrice
        vat = subtotal / 5
        return subtotal + vat

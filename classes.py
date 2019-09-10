import datetime


class Event:
    def __init__(self, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, costPerhead):
        self.nameofContact = nameofContact
        self.noGuests = noGuests
        self.address = address
        self.contactNo = contactNo
        self.eventRoomNo = eventRoomNo
        self.dateOfEvent = dateOfEvent
        self.costPerhead = costPerhead
        self.dateOfBooking = datetime.datetime.now()

    def total(self):
        subtotal = self.noGuests * self.costPerhead
        vat = subtotal / 5
        return subtotal + vat


class Conference(Event):
    def __init__(self, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, companyName, noOfDays,
                 projectorRequired):
        super().__init__(noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, costPerhead=0)
        self.companyName = companyName
        self.noOfDays = noOfDays
        self.projectorRequired = projectorRequired
        self.costPerhead = 20

    def total(self):
        subtotal = self.noGuests * self.costPerhead
        vat = subtotal / 5
        return subtotal + vat


class Party(Event):
    def __int__(self, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, costPerhead, bandName,
                bandPrice):
        super().__init__(noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent, costPerhead)
        self.bandName = bandName
        self.bandPrice = bandPrice

    def total(self):
        subtotal = (self.costPerhead * self.noGuests) + self.bandPrice
        vat = subtotal / 5
        return subtotal + vat


class Wedding(Party):
    def __init__(self, bandName, bandPrice, noGuests, nameofContact, address, contactNo, eventRoomNo, dateOfEvent,
                 costPerhead, noBedroomsReserved):
        super().__init__(self, bandName, bandPrice, noGuests, nameofContact, address, contactNo, eventRoomNo,
                         dateOfEvent, costPerhead)
        self.noBedroomsReserved = noBedroomsReserved

    def total(self):
        subtotal = (self.costPerhead * self.noGuests) + self.bandPrice
        vat = subtotal / 5
        return subtotal + vat

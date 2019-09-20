from mailmerge import MailMerge
from tkinter.filedialog import asksaveasfile
from datetime import datetime
import money_convert as mc


def File_Dialog():
    """function to display file dialog that allows user to save Invoice as docx file type"""
    path = asksaveasfile(defaultextension=".docx", filetypes=[("document file", "*.docx")])
    return path


def Conference_Invoice(Conference):
    ConferenceTemplatePath = "invoice_templates\\Conference_template.docx"
    doc = MailMerge(ConferenceTemplatePath)
    doc.merge(
        dateCreated='{:%Y-%m-%d}'.format(datetime.now().today()),
        companyName=str(Conference.companyName),
        name=str(Conference.nameofContact),
        address=str(Conference.address),
        contactNumber=str(Conference.contactNo),
        dateOfBooking=Conference.dateOfBooking.strftime('%Y-%m-%d'),
        dateOfEvent=Conference.dateOfEvent.strftime('%Y-%m-%d'),
        numberOfDays=str(Conference.noOfDays),
        projectorRequired='Yes' if Conference.projectorRequired else 'No',
        roomNumber=str(Conference.eventRoomNo),
        numberOfGuests=str(Conference.noGuests),
        costPerHead=mc.pound_string(Conference.costPerhead),
        priceForAllDays=mc.pound_string(Conference.subTotal()),
        subTotal=mc.pound_string(Conference.subTotal()),
        VAT=mc.pound_string(Conference.VAT()),
        total=mc.pound_string(Conference.total())
    )
    path = File_Dialog()
    if path is not None:
        doc.write(path.name)


def party_invoice(party):
    PartyTemplatePath = "invoice_templates\\Party_template.docx"
    doc = MailMerge(PartyTemplatePath)
    doc.merge(
        name=party.nameofContact,
        address=party.address,
        contactNumber=party.contactNo,
        dateCreated='{:%Y-%m-%d}'.format(datetime.now().today()),
        dateOfBooking=party.dateOfBooking.strftime('%Y-%m-%d'),
        dateOfEvent=party.dateOfEvent.strftime('%Y-%m-%d'),
        bandName=party.bandName,
        bandPrice=mc.pound_string(party.bandPrice),
        roomNumber=party.eventRoomNo,
        costPerHead=mc.pound_string(party.costPerhead),
        numberOfGuests=str(party.noGuests),
        costPerHeadTotal=mc.pound_string(party.costPerHeadTotal()),
        subTotal=mc.pound_string(party.subTotal()),
        VAT=mc.pound_string(party.VAT()),
        total=mc.pound_string(party.total())
    )
    path = File_Dialog()
    if path is not None:
        doc.write(path.name)


def wedding_invoice(wedding):
    PartyTemplatePath = "invoice_templates\\Wedding_template.docx"
    doc = MailMerge(PartyTemplatePath)
    print(doc.get_merge_fields())
    doc.merge(
        name=wedding.nameofContact,
        address=wedding.address,
        contactNumber=wedding.contactNo,
        dateCreated='{:%Y-%m-%d}'.format(datetime.now().today()),
        dateOfBooking=wedding.dateOfBooking.strftime('%Y-%m-%d'),
        dateOfEvent=wedding.dateOfEvent.strftime('%Y-%m-%d'),
        bandName=wedding.bandName,
        bandPrice=mc.pound_string(wedding.bandPrice),
        roomNumber=wedding.eventRoomNo,
        roomsReserved=str(wedding.noBedroomsReserved),
        costPerHead=mc.pound_string(wedding.costPerhead),
        numberOfGuests=str(wedding.noGuests),
        costPerHeadTotal=mc.pound_string(wedding.costPerHeadTotal()),
        subTotal=mc.pound_string(wedding.subTotal()),
        VAT=mc.pound_string(wedding.VAT()),
        total=mc.pound_string(wedding.total())
    )
    path = File_Dialog()
    if path is not None:
        doc.write(path.name)

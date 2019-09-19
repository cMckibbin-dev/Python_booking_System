from mailmerge import MailMerge
from tkinter.filedialog import asksaveasfile
from datetime import datetime


def File_Dialog():
    """function to display file dialog that allows user to save Invoice as docx file type"""
    path = asksaveasfile(defaultextension=".docx", filetypes=[("document file", "*.docx")])
    return path.name


def Conference_Invoice(Conference):
    ConferenceTemplatePath = "invoice_templates\\Conference_template.docx"
    doc = MailMerge(ConferenceTemplatePath)

    doc.merge(
        dateCreated=datetime.now().date(),
        companyName=Conference.companyName,
        name=Conference.nameofContact,
        address=Conference.address,
        contactNumber=Conference.contactNo,
        dateOFBooking=Conference.dateOfBooking,
        dateOFEvent=Conference.dateOfEvent,
        numberOfDays=Conference.noOfDays,
        projectorRequired='Yes' if Conference.projectorRequired else 'No',
        roomNumnber=Conference.eventRoomNo,
        numberOfGuests=Conference.noGuests,
        costPerHead=Conference.costPerhead,
        PriceForAllDays=Conference.subTotal(),
        subTotal=Conference.subTotal(),
        VAT=Conference.VAT(),
        total=Conference.total()
    )
    doc.write(File_Dialog())

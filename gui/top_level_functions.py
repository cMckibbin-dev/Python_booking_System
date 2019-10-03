from tkinter import *
from classes import *
from gui import view_details as vD
from gui import update
from gui import CalendarDialog


def calendar_popup(event, master, date_string, startDate=None, minDate=None):
    """function to display calendar dialog and changes value of StringVar to the selected value"""
    c = CalendarDialog.CalendarDialog(master, startDate, minDate)
    # if master is root or Toplevel then it grab_set of the program once dialog closes
    if type(master) == Tk or type(master) == Toplevel:
        master.grab_set()

    if c.result:
        date_string.set(c.result)


def _view_details(event):
    """function to return the correct view details class for the instance of the event"""
    if isinstance(event, Conference):
        return vD.ViewDetailsConference
    elif isinstance(event, Wedding):
        return vD.ViewDetailsWedding
    elif isinstance(event, Party):
        return vD.ViewDetailsParty


def _update_form(event):
    """function returns correct update UI class for given event"""
    if isinstance(event, Conference):
        return update.UpdateConferenceUI
    elif isinstance(event, Wedding):
        return update.UpdateWeddingUI
    elif isinstance(event, Party):
        return update.UpdatePartyUI
    else:
        print('error')


def view_details_popup(booking, parent):
    """function creates a top level pop up for the view details form of a event"""
    top = Toplevel()
    top.title('View Details')
    form = _view_details(booking)
    form(top, booking)
    top.grab_set()
    top.focus_force()
    top.wait_window()
    top.destroy()
    parent.focus_force()


def update_popup(parent, booking):
    """This function allows us to create a toplevel window for the edit window that grabs focus of the application
     while in use, this mean view all bookings will still run in the background as the main root"""
    top = Toplevel()
    top.title('Update Booking')
    form = _update_form(booking)
    form(top, booking)
    top.grab_set()
    top.focus_force()
    top.wait_window()
    top.destroy()
    parent.focus_force()

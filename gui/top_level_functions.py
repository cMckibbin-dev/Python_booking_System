from tkinter import *
import ttkcalendar


def date_top_level(event, entry):
    """function to call calender widget and insert selected value into entry box"""
    top = Toplevel()
    top.title('Selected Date')
    # calender widget
    calendar = ttkcalendar.Calendar(top)
    top.grab_set()
    top.wait_window()
    print(calendar.getselection())
    entry.delete(0, 'end')
    entry.insert(0, calendar.getselection())
    top.destroy()

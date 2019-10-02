import tkinter.simpledialog as simple
import tkcalendar
from datetime import datetime


class CalendarDialog(simple.Dialog):
    """Dialog for a calendar popup that will allow user to input a date"""

    def __init__(self, master, startDate=None, minDate=None):
        self.master = master
        self.startDate = None
        if isinstance(startDate, str):
            self.startDate = datetime.strptime(startDate, '%Y-%m-%d').date()
        elif isinstance(startDate, datetime):
            self.startDate = startDate
        else:
            self.startDate = datetime.now().date()

        if minDate is not None and minDate:
            self.minDate = minDate
        elif minDate is False and minDate is not None:
            self.minDate = None
        else:
            self.minDate = datetime.now().date()
        super().__init__(self.master, title='Calender')

    def body(self, master):
        self.calendar = tkcalendar.Calendar(master, mindate=self.minDate, year=self.startDate.year,
                                            month=self.startDate.month, day=self.startDate.day)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection_get()

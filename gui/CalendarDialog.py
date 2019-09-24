import tkinter.simpledialog as simple
import tkcalendar
from datetime import datetime
from tkinter import StringVar


class CalendarDialog(simple.Dialog):
    """Dialog for a calendar popup that will allow user to input a date"""

    def __init__(self, master, startDate=None):
        self.master = master
        self.startDate = None
        if isinstance(startDate, str):
            self.startDate = datetime.strptime(startDate, '%Y-%m-%d').date()
        elif isinstance(startDate, datetime):
            self.startDate = startDate
        elif startDate is None:
            self.startDate = datetime.now().date()
        super().__init__(self.master, title='Calender')

    def body(self, master):
        self.calendar = tkcalendar.Calendar(master, mindate=datetime.now(), year=self.startDate.year,
                                            month=self.startDate.month, day=self.startDate.day)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection_get()

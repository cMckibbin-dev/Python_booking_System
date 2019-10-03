import datetime
from tkinter import *
from gui import top_level_functions as tlf, dialogs
from Data_Access.data_access import DBAccess
import money_convert as mc
from gui import main_menu
from gui import tkinter_styling as style
import validation


class ViewIncome:
    """ViewIncome contains the UI elements and methods needed for the view income window"""
    def __init__(self, master):
        self.master = master

        # configure window
        self.master.resizable(0, 0)
        self.master.iconbitmap(str(style.logo))
        self.master.title('Total Income')
        self.master.configure(bg=style.windowBG)
        self.master.protocol('WM_DELETE_WINDOW', self.backToMainMenu)

        # widgets for window
        self.heading = Label(self.master, text='View Total Income', font=style.textHeading, bg=style.widgetBG)

        # widgets for search options
        # frame for event type search options
        self.eventTypeFrame = Frame(self.master, bg=style.widgetBG)
        # variables for check buttons for event type selection
        self.weddingCheck = BooleanVar()
        self.partyCheck = BooleanVar()
        self.conferenceCheck = BooleanVar()
        self.eventTypeLabel = Label(self.eventTypeFrame, text='Event Type:', font=style.textNormal, bg=style.widgetBG)
        self.weddingCheckBox = Checkbutton(self.eventTypeFrame, text='Weddings', font=style.textNormal,
                                           bg=style.widgetBG, variable=self.weddingCheck)
        self.partyCheckBox = Checkbutton(self.eventTypeFrame, text='Parties', font=style.textNormal, bg=style.widgetBG,
                                         variable=self.partyCheck)
        self.conferenceCheckBox = Checkbutton(self.eventTypeFrame, text='Conferences', font=style.textNormal,
                                              bg=style.widgetBG, variable=self.conferenceCheck)

        # frame for date search options
        self.dateFrame = Frame(self.master, bg=style.widgetBG)
        # Start date labels and date picker
        self.dateFromLabel = Label(self.dateFrame, text='Date From:', font=style.textNormal, bg=style.widgetBG)
        self.dateFromValue = StringVar()
        self.dateFromDatePick = Entry(self.dateFrame, font=style.textNormal, state='readonly', bg=style.widgetBG,
                                      textvariable=self.dateFromValue)
        self.dateFromDatePick.bind('<Button-1>', lambda e: tlf.calendar_popup(e, self.master, self.dateFromValue,
                                                                              minDate=False))  # calls date picker
        # End date labels and date picker
        self.dateToLabel = Label(self.dateFrame, text='Date To:', font=style.textNormal, bg=style.widgetBG)
        self.dateToValue = StringVar()
        self.dateToDatePick = Entry(self.dateFrame, font=style.textNormal, state='readonly', bg=style.widgetBG,
                                    textvariable=self.dateToValue)
        self.dateToDatePick.bind('<Button-1>', lambda e: self.check_from_date(e))  # checks start date entered first

        # widgets for displaying total income of events

        self.subHeading = Label(self.master, font=style.textHeading, text='Details', bg=style.widgetBG)
        self.totalIncomeLabel = Label(self.master, font=style.textNormal, text='Total Income From Events:',
                                      bg=style.widgetBG)
        self.totalIncomeInfo = Label(self.master, font=style.textNormal, bg=style.widgetBG)

        # frame and buttons for window
        self.buttonFrame = Frame(self.master, bg=style.widgetBG)
        self.buttonBack = Button(self.buttonFrame, text='Back', width=style.buttonWidth, height=style.buttonHeight,
                                 command=self.backToMainMenu, bg=style.buttonColour1)
        self.buttonSearch = Button(self.buttonFrame, text='Search', width=style.buttonWidth, height=style.buttonHeight,
                                   command=self.search_Total, bg=style.buttonColour2)

        # placing widgets in grid layout
        self.heading.grid(row=0, column=0, columnspan=7, padx=style.paddingX, pady=(10, 25))

        # placing event type widgets
        self.eventTypeFrame.grid(row=1, column=0, columnspan=4)
        self.eventTypeLabel.grid(row=1, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.weddingCheckBox.grid(row=1, column=1, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.partyCheckBox.grid(row=1, column=2, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.conferenceCheckBox.grid(row=1, column=3, sticky=E, padx=style.paddingX, pady=style.paddingY)

        # placing date widgets
        self.dateFrame.grid(row=2, column=0, columnspan=4)
        self.dateFromLabel.grid(row=2, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.dateFromDatePick.grid(row=2, column=1, sticky=E, padx=style.paddingX, pady=style.paddingY)
        self.dateToLabel.grid(row=2, column=3, sticky=W, padx=style.paddingX, pady=style.paddingY)
        self.dateToDatePick.grid(row=2, column=4, sticky=W, padx=style.paddingX, pady=style.paddingY)


        # placing heading for results
        self.subHeading.grid(row=4, column=0, sticky=NSEW, columnspan=4, padx=style.paddingX, pady=(10, 10))
        # placing labels and info for for result
        self.totalIncomeLabel.grid(row=5, column=0, sticky=E, padx=(25, 25), pady=(10, 25))
        self.totalIncomeInfo.grid(row=5, column=1, sticky=W, padx=(25, 25), pady=(10, 25))

        # placing buttons
        self.buttonFrame.grid(row=6, columnspan=4)
        self.buttonBack.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)
        self.buttonSearch.pack(side=LEFT, padx=style.paddingX, pady=style.paddingY)

    def checkbox_checked(self):
        """function to check if checkboxes in view income have at least 1 checked before searching"""
        if self.weddingCheck.get() is False and self.partyCheck.get() is False and self.conferenceCheck.get() is False:
            return False
        else:
            return True

    def search_Total(self):
        """function to get the total income of bookings made between two dates"""
        # checks entries are not empty and at least one check box is selected
        if validation.EntriesNotEmpty(self.master) and self.checkbox_checked():
            db = DBAccess()
            selectedTables = []  # Gets data from the database from all 3 tables
            if self.conferenceCheck.get():
                selectedTables.append('Conference')
            if self.partyCheck.get():
                selectedTables.append('party')
            if self.weddingCheck.get():
                selectedTables.append('Wedding')

            # passes search criteria to a data access function to get results
            results = db.bookings_between_dates(selectedTables, self.dateFromDatePick.get(), self.dateToDatePick.get())
            total = 0
            for result in results:
                total += result.total()  # Adds the results together

            self.totalIncomeInfo['text'] = mc.pound_string(total)  # converts to pound sterling
        else:
            dialogs.no_search_criteria(self.master)  # Returns warning to user if no search criteria entered

    def backToMainMenu(self):
        """method to close current root and create new root and opens main menu on it"""
        self.master.destroy()
        root = Tk()
        main_menu.MainMenuUI(root)
        root.mainloop()

    def check_from_date(self, event):
        """method to ensure that user has entered a start date before they have entered an end date"""
        if self.dateFromValue.get() == "":
            dialogs.enter_from_date(self.master)
        else:
            tlf.calendar_popup(None, self.master, self.dateToValue,
                               minDate=datetime.datetime.strptime
                               (self.dateFromValue.get(), '%Y-%m-%d')
                               .date())

from tkinter import *
import tkinter.ttk as ttk


class ViewIncome:
    def __init__(self, master):
        self.master = master
        # configure window
        self.master.title('Total Income')
        self.master.configure(background='white')

        # style variables for widgets
        self.textHeading = 'Helvetica 18 bold'
        self.textNormal = 'Helvetica 12'
        self.paddingX = 5
        self.paddingY = 5
        # button sizes
        self.buttonWidth = 10
        self.buttonHeight = 2
        # widget background colour
        self.widgetBG = 'white'

        # widgets for window
        self.heading = Label(self.master, text='View Total Income', font=self.textHeading, bg=self.widgetBG)

        # widgets for search options
        self.eventTypeLabel = Label(self.master, text='Event Type:', font=self.textNormal, bg=self.widgetBG)
        self.eventTypeCombo = ttk.Combobox(self.master, font=self.textNormal, values=['Conference',
                                                                                                        'Wedding',
                                                                                                        'Party'],
                                           state='readonly')

        self.dateFromLabel = Label(self.master, text='Date From:', font=self.textNormal, bg=self.widgetBG)
        self.dateFromDatePick = Entry(self.master, font=self.textNormal, state='readonly', bg=self.widgetBG)

        self.dateToLabel = Label(self.master, text='Date To:', font=self.textNormal, bg=self.widgetBG)
        self.dateToDatePick = Entry(self.master, font=self.textNormal, state='readonly', bg=self.widgetBG)

        # widgets for displaying total income of events

        self.subHeading = Label(self.master, font=self.textHeading, text='Details', bg=self.widgetBG)

        self.totalIncomeLabel = Label(self.master, font=self.textNormal, text='Total Income From Events:',
                                      bg=self.widgetBG)
        self.totalIncomeInfo = Label(self.master, font=self.textNormal, bg=self.widgetBG)

        # frame and buttons for window
        self.buttonFrame = Frame(self.master, bg=self.widgetBG)
        self.buttonBack = Button(self.buttonFrame, text='Back', width=self.buttonWidth, height=self.buttonHeight)
        self.buttonSearch = Button(self.buttonFrame, text='Search', width=self.buttonWidth, height=self.buttonHeight)

        # placing widgets in grid layout
        self.heading.grid(row=0, column=0, columnspan=4, padx=self.paddingX, pady=self.paddingY)

        self.eventTypeLabel.grid(row=1, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.eventTypeCombo.grid(row=1, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.dateFromLabel.grid(row=2, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.dateFromDatePick.grid(row=2, column=1, sticky=E, padx=self.paddingX, pady=self.paddingY)

        self.dateToLabel.grid(row=2, column=3, sticky=W, padx=self.paddingX, pady=self.paddingY)
        self.dateToDatePick.grid(row=2, column=4, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.subHeading.grid(row=4, column=0, sticky=NSEW, columnspan=2, padx=self.paddingX, pady=self.paddingY)

        self.totalIncomeLabel.grid(row=5, column=0, sticky=E, padx=self.paddingX, pady=self.paddingY)
        self.totalIncomeInfo.grid(row=5, column=1, sticky=W, padx=self.paddingX, pady=self.paddingY)

        self.buttonFrame.grid(row=6, columnspan=4)
        self.buttonBack.pack(side=LEFT, padx=self.paddingX, pady=self.paddingY)
        self.buttonSearch.pack(side=LEFT, padx=self.paddingX, pady=self.paddingY)

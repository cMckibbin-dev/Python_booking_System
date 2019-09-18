from tkinter import *
import tkinter.ttk as ttk
import gui.top_level_functions as tlf


class ViewTotalIncomeUI:

    def __init__(self, root):
        self.root = root
        self.root.geometry("900x350")
        self.options = [
            "Please select event type",
            "Conference",
            "Party",
            "Wedding"
        ]

        self.variable = StringVar(self.root)
        self.variable.set(self.options[0])  # default value

        root.title("View Total Income")
        self.root.configure(background='white')

        self.label = Label(self.root, text="View Total Income (Per Event Type)", font="Ariel, 16", height=2,
                           anchor='center', width=40)

        self.eventTypeLbl = Label(self.root, text="Select Event Type:", font="Ariel, 12", anchor='e', width=20)
        self.eventType = OptionMenu(self.root, self.variable, *self.options, command="")

        self.dateFrame = Frame(self.root)
        self.fromLbl = Label(self.dateFrame, text="From: ", font="Ariel, 12", anchor='e', width=20)
        self.fromEntry = Entry(self.dateFrame, state='readonly')
        self.fromEntry.bind('<Button-1>', lambda event: tlf.date_top_level(event, self.fromEntry))

        self.toLbl = Label(self.dateFrame, text="Date of Event:", font="Ariel, 12", anchor='e', width=20)
        self.toEntry = Entry(self.dateFrame)
        self.toEntry.bind('<Button-1>', lambda event: tlf.date_top_level(event, self.toEntry))
        self.f1 = Frame(self.root)
        self.backBtn = Button(self.f1, text="Back", width=10, height=2)
        self.searchBtn = Button(self.f1, text="Search", width=10, height=2)
        self.subHeadingLbl = Label(self.root, text="Details", font="Ariel, 16", height=2)
        self.totalIncomeLbl = Label(self.root, text="Total income from Events: ", font="Ariel, 16", height=2)
        self.totalIncomeValueLbl = Label(self.root, text="£0000", font="Ariel, 16", height=2)

        self.label.grid(row=0, column=0, columnspan=5, pady=(10, 20), padx=(120, 0), sticky=NSEW)
        self.eventType.grid(row=2, column=3, sticky=NSEW, pady=(0, 25), padx=(0, 20))
        self.eventTypeLbl.grid(row=2, column=2, pady=(0, 25))
        self.dateFrame.grid(row=3, column=1, columnspan=3)
        self.fromLbl.pack(side="left")
        self.fromEntry.pack(side="left")
        self.toLbl.pack(side="left")
        self.toEntry.pack(side="left")
        self.subHeadingLbl.grid(row=4, column=2, columnspan=2)
        self.totalIncomeLbl.grid(row=5, column=2)
        self.totalIncomeValueLbl.grid(row=5, column=3)
        self.f1.grid(row=14, columnspan=2, column=2, pady=(40, 40))
        # The buttons are packed into the frame and they have a "highlightbackground" field so they will work on a Mac.
        # "highlightbackground" is not needed for windows.
        self.backBtn.pack(side="left", padx=(0, 5))
        self.backBtn.config(bg='snow', highlightbackground='snow', state=DISABLED)
        self.searchBtn.pack(side="left", padx=(5, 0))
        self.searchBtn.config(bg='SteelBlue1', highlightbackground='SteelBlue1', fg='white')

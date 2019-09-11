from tkinter import *
import tkinter.ttk as ttk


class IndexUI:
    def __init__(self, master):
        # variables
        self.buttonActive = False

        # window configure
        self.master = master
        self.master.title('View Bookings')

        # setting text formatting vars
        self.textHeading = 'Helvetica 18 bold'
        self.textNormal = 'Helvetica 12'
        self.textTreeHeading = 'Helvetica 14 bold'

        # window Title Label
        self.titleLabel = Label(master, text='View Bookings', font=self.textHeading)

        # combo boxes for form search options
        self.comboEventType = ttk.Combobox(master, values=['All Types', 'Conference', 'Party', 'Wedding'],
                                           font=self.textNormal, state='readonly')
        self.comboEventType.current(1)

        # Future dates only checkbox
        self.futureDateCheckBox = Checkbutton(self.master, text="Future Dates only", font=self.textNormal)
        # buttons for form
        self.buttonSearch = Button(master, text='Search', font=self.textNormal)

        # These buttons only become active when options selected in tree view
        self.buttonBack = Button(master, text='Back', font=self.textNormal)
        self.buttonViewDetails = Button(master, text='View Details', font=self.textNormal, state=DISABLED)
        self.buttonEdit = Button(master, text='Edit', font=self.textNormal, state=DISABLED)

        # tree view for form where bookings are displayed
        self.tree = ttk.Treeview(master, columns=('Name of Contact', 'No.Guests', 'Room Number', 'Type of Event',
                                                  'Date of Event'))
        self.tree.heading('#1', text='Name of Contact')
        self.tree.heading('#2', text='No.Guests')
        self.tree.heading('#3', text='Room Number')
        self.tree.heading('#4', text='Type of Event')
        self.tree.heading('#5', text='Date of Event')
        self.tree['show'] = 'headings'
        self.tree.bind('<Button-1>', self.active_buttons)

        # total events label
        self.EventTotal = Label(self.master, text='Number of Events:', font=self.textNormal)
        self.TotalLabel = Label(self.master, text='0', font=self.textNormal)

        # setting grid layout for window
        # title of form
        self.titleLabel.grid(column=0, sticky=NSEW, columnspan=3, padx=10, pady=10)

        # layout for search options
        self.futureDateCheckBox.grid(row=1, column=0, sticky=NSEW, padx=10, pady=10)
        self.comboEventType.grid(row=1, column=1, sticky=NSEW, padx=10, pady=10)
        self.buttonSearch.grid(row=2, column=1, sticky=E, padx=10, pady=10)

        # layout for Tree view
        self.tree.grid(row=3, columnspan=3, sticky=NSEW, padx=10, pady=10)

        # total labels
        self.EventTotal.grid(row=4, column=0, sticky=E, padx=10, pady=10)
        self.TotalLabel.grid(row=4, column=1, sticky=W, padx=10, pady=10)

        # option buttons at bottom of window
        self.buttonBack.grid(row=5, column=0, sticky=NSEW, columnspan=1, padx=10, pady=10)
        self.buttonViewDetails.grid(row=5, column=1, sticky=NSEW, columnspan=1, padx=10, pady=10)
        self.buttonEdit.grid(row=5, column=2, sticky=NSEW, columnspan=1, padx=10, pady=10)

        # setting weight and uniform for and column in grid
        self.master.grid_columnconfigure(0, weight=0, uniform='fred')
        self.master.grid_columnconfigure(1, weight=0, uniform='fred')
        self.master.grid_columnconfigure(2, weight=0, uniform='fred')

        self.TotalLabel['text'] = self.total_treeview()

    def total_treeview(self):
        itemCount = len(self.tree.get_children())
        return itemCount

    def active_buttons(self, event):
        if not self.buttonActive:
            item = self.tree.focus()
            if item:
                self.buttonEdit['state'] = "normal"
                self.buttonViewDetails['state'] = "normal"
                self.buttonActive = True
            else:
                print('Select option')

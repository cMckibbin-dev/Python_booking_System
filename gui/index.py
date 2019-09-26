from tkinter import *
import tkinter.ttk as ttk
from Data_Access import data_access as dBA
from classes import *
from gui import main_menu
from gui.top_level_functions import view_details_popup, update_popup
from gui import tkinter_styling as style


def get_event_type(event):
    """function returns a string representing the type of the event"""
    if isinstance(event, Conference):
        return 'Conference'
    elif isinstance(event, Wedding):
        return 'Wedding'
    elif isinstance(event, Party):
        return 'Party'


def get_selected_index(tree):
    item = tree.focus()
    if item:
        return tree.get_children().index(item)


class IndexUI:
    def __init__(self, master):
        # variables
        self.buttonActive = False
        self.dbAccess = dBA.DBAccess()
        self.events = self.getdata()
        self.focusOut = False

        # window configure
        self.master = master
        self.master.title('View Bookings')
        self.master.config(background=style.windowBG)
        self.master.resizable(0, 0)
        self.master.bind('<FocusIn>', self.refresh_onfocus)
        self.master.protocol('WM_DELETE_WINDOW', self.back_to_main_menu)

        # setting text formatting vars


        # window Title Label
        self.titleLabel = Label(master, text='View Bookings', bg=style.widgetBG, font=style.textHeading)

        # combo boxes for form search options
        self.comboEventType = ttk.Combobox(master, values=['All Types', 'Conference', 'Party', 'Wedding'],
                                           font=style.textNormal, state='readonly')
        self.comboEventType.current(0)

        # Future dates only checkbox
        self.isChecked = BooleanVar()
        self.futureDateCheckBox = Checkbutton(self.master, text="Future Dates only", bg=style.widgetBG, font=style.textNormal,
                                              var=self.isChecked)
        # buttons for form
        self.buttonSearch = Button(master, text='Search', font=style.textNormal)
        self.buttonSearch.bind('<Button-1>', self.updateEvents)

        # These buttons only become active when options selected in tree view
        # frame for buttons
        self.buttonFrame = Frame(self.master , bg=style.widgetBG)
        self.buttonBack = Button(self.buttonFrame, text='Back', font=style.textNormal, bg="snow", height= 2 , width = 10, command=self.back_to_main_menu)
        self.buttonViewDetails = Button(self.buttonFrame, text='View Details', font=style.textNormal, state=DISABLED, bg=style.buttonColour1,
                                         height= 2 , width = 10, command=lambda: self.open_view_details())
        self.buttonEdit = Button(self.buttonFrame, text='Edit', font=style.textNormal, state=DISABLED, bg=style.buttonColour2, height= 2 , width = 10, command=self.open_edit)

        # tree view for form where bookings are displayed
        self.tree = ttk.Treeview(master, columns=('Name of Contact', 'No.Guests', 'Room Number', 'Type of Event',
                                                  'Date of Event'))
        self.tree.heading('#1', text='Name of Contact')
        self.tree.heading('#2', text='No.Guests')
        self.tree.heading('#3', text='Room Number')
        self.tree.heading('#4', text='Type of Event')
        self.tree.heading('#5', text='Date of Event')
        self.tree['show'] = 'headings'
        self.tree.bind('<ButtonRelease-1>', self.active_buttons)

        # total events label
        self.EventTotal = Label(self.master, text='Number of Events:', bg=style.widgetBG, font=style.textNormal)
        self.TotalLabel = Label(self.master, text='0', bg=style.widgetBG, font=style.textNormal)

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
        self.buttonFrame.grid(row=5, column=0, columnspan=3)
        self.buttonBack.grid(row=5, column=0, sticky=NSEW, columnspan=1, padx=10, pady=10)
        self.buttonViewDetails.grid(row=5, column=1, sticky=NSEW, columnspan=1, padx=10, pady=10)
        self.buttonEdit.grid(row=5, column=2, sticky=NSEW, columnspan=1, padx=10, pady=10)

        self.TotalLabel['text'] = len(self.events)
        self.refresh_eventlist()

    # function to active buttons
    def active_buttons(self, event):
        if not self.buttonActive:
            item = self.tree.focus()
            if item:
                self.buttonEdit['state'] = "normal"
                self.buttonViewDetails['state'] = "normal"
                self.buttonActive = True
            else:
                print('Select option')

    def deactive_buttons(self):
        if self.buttonActive:
            self.buttonEdit['state'] = "disable"
            self.buttonViewDetails['state'] = "disable"
            self.buttonActive = False

    def insert_to_tree(self, data):
        """Insert data in to tree view"""
        self.tree.insert('', 'end', values=(data.nameofContact, data.noGuests, data.eventRoomNo,
                                            get_event_type(data), data.dateOfEvent))

    def refresh_eventlist(self):
        self.TotalLabel['text'] = len(self.events)
        self.tree.delete(*self.tree.get_children())
        for event in self.events:
            self.insert_to_tree(event)

    def getdata(self, eventType='All Types', future=False):
        future = future
        if eventType == "All Types":
            return self.dbAccess.all_records(future)
        elif eventType == "Party":
            return self.dbAccess.all_party(future)
        elif eventType == "Conference":
            return self.dbAccess.all_conferences(future)
        elif eventType == 'Wedding':
            return self.dbAccess.all_weddings(future)

    def updateEvents(self, event):
        self.events = self.getdata(self.comboEventType.get(), self.isChecked.get())
        self.refresh_eventlist()
        self.deactive_buttons()

    def refresh_onfocus(self, event):
        """function ran when window gains focus"""
        if self.focusOut:
            self.events = self.getdata(self.comboEventType.get(), self.isChecked.get())
            self.refresh_eventlist()
            self.focusOut = False
            print('focus')
            self.deactive_buttons()

    def open_view_details(self):
        view_details_popup(self.events[get_selected_index(self.tree)], self.master)

    def open_edit(self):
        self.focusOut = True
        update_popup(self.master, self.events[get_selected_index(self.tree)])

    def back_to_main_menu(self):
        """method close index window and opens a new window to display the main menu"""
        self.master.destroy()
        root = Tk()
        main_menu.MainMenuUI(root)
        root.mainloop()

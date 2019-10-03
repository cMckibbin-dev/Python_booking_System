from tkinter import *
from gui import create_booking
from gui import index, view_income
from gui import tkinter_styling as style


def load_index(parent_root):
    """Function to load the view all bookings form"""
    parent_root.destroy()  # destroys old root
    root = Tk()  # creates a new one for view all bookings
    ui = index.IndexUI(root)
    root.mainloop()


class MainMenuUI:

    def __init__(self, root):
        """main menu GUI"""
        self.root = root
        self.root.title("Main Menu")
        self.root.resizable(0, 0)
        self.root.iconbitmap(str(style.logo))
        self.root.config(background=style.windowBG)

        # Widget creation

        # Title
        self.label = Label(self.root, text="Main Menu", font=style.textHeading, bg=style.widgetBG, height=2)

        # Buttons
        self.createNewBookingBtn = Button(self.root, text="Create New Booking", font=style.textNormal, width=20,
                                          height=3, command=self.load_create, bg=style.buttonColour1)
        self.ViewAllBookingsBtn = Button(self.root, text="View All Bookings", font=style.textNormal, width=20, height=3,
                                         command=lambda: load_index(self.root), bg=style.buttonColour2)
        self.ViewTotalIncomeBtn = Button(self.root, text="View Total Income", font=style.textNormal, width=20, height=3,
                                         command=self.load_income, bg=style.buttonColour2)
        self.ExitBtn = Button(self.root, text="Exit", font=style.textNormal, width=20, height=3,
                              command=self.root.destroy, bg=style.buttonColour1)

        # Widget positioning
        self.label.grid(row=0, column=0, columnspan=5, pady=(10, 20))
        self.createNewBookingBtn.grid(row=3, column=1, padx=(20, 5))
        self.ViewAllBookingsBtn.grid(row=3, column=2, padx=(0, 20))
        self.ViewTotalIncomeBtn.grid(row=4, column=1, padx=(20, 5), pady=(5, 30))
        self.ExitBtn.grid(row=4, column=2, padx=(0, 20), pady=(5, 30))


    def load_income(self):
        """function to load the view total income form"""
        self.root.destroy()  # destroys old root
        root = Tk()  # creates a new one for total income
        view_income.ViewIncome(root)
        root.mainloop()


    def load_create(self):
        """function to load the create form"""
        self.root.destroy()  # destroys old root
        root = Tk()  # creates a new one for create
        create_booking.CreateMenu(root)
        root.mainloop()





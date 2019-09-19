from tkinter import *
from gui import index, view_total_income, create
import tkinter.ttk as ttk


def load_index(parent_root):
    parent_root.destroy()
    root = Tk()
    ui = index.IndexUI(root)
    root.mainloop()


class MainMenuUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")

        # Widget creation
        self.label = Label(self.root, text="Main Menu", font="Ariel, 16", height=2)

        self.createNewBookingBtn = Button(self.root, text="Create New Booking", font="Ariel, 12", width=20, height=3,
                                          command=self.load_create)
        self.ViewAllBookingsBtn = Button(self.root, text="View All Bookings", font="Ariel, 12", width=20, height=3,
                                         command=lambda: load_index(self.root))
        self.ViewTotalIncomeBtn = Button(self.root, text="View Total Income", font="Ariel, 12", width=20, height=3,
                                         command=self.load_income)
        self.ExitBtn = Button(self.root, text="Exit", font="Ariel, 12", width=20, height=3, command=self.root.destroy)

        # Widget positioning
        self.label.grid(row=0, column=0, columnspan=5, pady=(10, 20))
        self.createNewBookingBtn.grid(row=3, column=1, padx=(20, 5))
        self.ViewAllBookingsBtn.grid(row=3, column=2, padx=(0, 20))
        self.ViewTotalIncomeBtn.grid(row=4, column=1, padx=(20, 5), pady=(5, 30))
        self.ExitBtn.grid(row=4, column=2, padx=(0, 20), pady=(5, 30))

    # function to load the view total income form
    def load_income(self):
        self.root.destroy()
        root = Tk()
        view_total_income.ViewTotalIncomeUI(root)
        root.mainloop()

    # function to load the create form
    def load_create(self):
        self.root.destroy()
        root = Tk()
        create.CreateUI(root)
        root.mainloop()


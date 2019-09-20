from tkinter import *
from gui import create
from gui import index, view_income
from gui import tkinter_styling as style


def load_index(parent_root):
    parent_root.destroy()
    root = Tk()
    ui = index.IndexUI(root)
    root.mainloop()


class MainMenuUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.config(background="#C1FFEA")

        # Widget creation
        self.label = Label(self.root, text="Main Menu", font=style.textHeading, bg="#C1FFEA", height=2)

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

    # function to load the view total income form
    def load_income(self):
        self.root.destroy()
        root = Tk()
        view_income.ViewIncome(root)
        root.mainloop()

    # function to load the create form
    def load_create(self):
        self.root.destroy()
        root = Tk()
        create.CreateUI(root)
        root.mainloop()


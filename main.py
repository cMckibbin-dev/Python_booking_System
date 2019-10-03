"""the main module is the entry point of the program and calls the main menu"""
from gui import main_menu
from tkinter import Tk

root = Tk()
ui = main_menu.MainMenuUI(root)
root.mainloop()

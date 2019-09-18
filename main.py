from gui import main_menu
from gui import index, update, create, main_menu
from tkinter import *
import money_convert

root = Tk()
ui = main_menu.MainMenuUI(root)

value = float(10000/100)
money_convert.pound_string(value)
root.mainloop()

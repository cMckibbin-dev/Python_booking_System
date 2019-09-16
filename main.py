from gui import index
from gui import view_details
from gui import index, update, create
from gui import index, update, create, main_menu
from tkinter import *
from Data_Access import data_access as da

root = Tk()
ui = main_menu.MainMenuUI(root)
# ui = index.IndexUI(root)
root.mainloop()

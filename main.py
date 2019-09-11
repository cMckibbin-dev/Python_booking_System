from gui import index
from tkinter import *
from Data_Access import data_access as da

root = Tk()
ui = index.IndexUI(root)
da.DBAccess()
root.mainloop()

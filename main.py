from gui import index
from gui import view_details
from gui import index, update, create
from tkinter import *
from Data_Access import data_access as da

root = Tk()
# data = da.DBAccess()
# event = data.all_weddings()
# ui = view_details.ViewDetailsWedding(root, event[0])
# # ui = update.UpdateConferenceUI(root, eventtype='wedding')
ui = index.IndexUI(root)

root.mainloop()

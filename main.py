from gui import index, update, create
from tkinter import *
from Data_Access import data_access as da

root = Tk()
# ui = update.UpdateConferenceUI(root, eventtype='wedding')
# ui = create.CreateUI(root)
ui = index.IndexUI(root)
da.DBAccess()

root.mainloop()

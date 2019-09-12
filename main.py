from gui import index
from gui import view_details
from tkinter import *
from Data_Access import data_access as da

root = Tk()
data = da.DBAccess()
event = data.all_conferences()
ui = view_details.BaseViewDetail(root,event[0])

root.mainloop()

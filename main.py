from gui import index, update, create
from tkinter import *

root = Tk()
# ui = update.UpdateConferenceUI(root, eventtype='wedding')
ui = create.CreateUI(root)
root.mainloop()

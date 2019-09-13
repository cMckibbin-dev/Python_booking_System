from gui import index, update, create, main_menu, view_total_income
from tkinter import *
from Data_Access import data_access as da

root = Tk()
# ui = main_menu.MainMenuUI(root)
# ui = update.UpdateConferenceUI(root, eventtype='wedding')
ui = create.CreateUI(root)
# ui = index.IndexUI(root)
# ui = view_total_income.ViewTotalIncomeUI(root)
da.DBAccess()

root.mainloop()

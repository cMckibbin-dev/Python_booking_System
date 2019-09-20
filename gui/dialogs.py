from tkinter import messagebox

# updated dialog message box
def updated():
 messagebox.showinfo("Successful", "These details have been changed!")

# not saved dialog message box
def not_saved():
    messagebox.showinfo("Aborted", "Action canceled, no details have been saved!")

# saved dialog message box
def saved():
    messagebox.showinfo("Successful", "These details have been successfully saved!")

def deleted():
    messagebox.showinfo("Successful", "These details have been successfully deleted!")
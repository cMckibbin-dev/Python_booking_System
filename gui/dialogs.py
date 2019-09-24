from tkinter import messagebox


# updated dialog message box
def updated(parent):
    messagebox.showinfo("Successful", "These details have been changed!", parent=parent)


# not saved dialog message box
def not_saved(parent):
    messagebox.showinfo("Aborted", "Action canceled, no details have been saved!", parent=parent)


# saved dialog message box
def saved(parent):
    messagebox.showinfo("Successful", "These details have been successfully saved!", parent=parent)


def deleted(parent):
    messagebox.showinfo("Successful", "These details have been successfully deleted!", parent=parent)


def not_completed(parent, extra_info=''):
    messagebox.showerror('Error', 'Please ensure no inputs have been left empty and are completed with correct '
                                  'information.\n{}'.format(extra_info),
                         parent=parent)

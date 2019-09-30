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


# saved dialog message box
def saved_invoice():
    messagebox.showinfo("Successful", "This invoice has been successfully saved!\nYou can view this in Microsoft Word.")


def deleted(parent):
    messagebox.showinfo("Successful", "These details have been successfully deleted!", parent=parent)


def not_completed(parent, extra_info=''):
    messagebox.showerror('Error', 'Please ensure no inputs have been left empty and are completed with correct '
                                  'information.\n{}'.format(extra_info),
                         parent=parent)


def no_search_criteria(parent):
    messagebox.showerror("Error", "No search criteria! \n\nPlease make sure you have selected an event type and "
                                  "entered a date range. ", parent=parent)


def enter_from_date(parent):
    messagebox.showerror("Error", "You have not selected a start date!", parent=parent)


def save_file_error(extra_info=''):
    messagebox.showerror('Error', 'Error occurred while trying to save file\n{}'.format(extra_info))


def limit_reached(extra_info):
    messagebox.showerror('Error', 'The Character of {} limit has been reached'.format(extra_info))


def number_limit_reached(extra_info):
    messagebox.showerror('Error', 'The limit of {} has been reached'.format(extra_info))

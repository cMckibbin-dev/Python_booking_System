from tkinter import messagebox



def updated(parent):
    """dialog to advise user that booking was updated"""
    messagebox.showinfo("Successful", "These details have been changed!", parent=parent)


# not saved dialog message box
def not_saved(parent):
    """dialog to advise user that booking was not saved"""
    messagebox.showinfo("Aborted", "Action canceled, no details have been saved!", parent=parent)


# saved dialog message box
def saved(parent):
    """dialog to advise user that booking was saved"""
    messagebox.showinfo("Successful", "These details have been successfully saved!", parent=parent)


# saved dialog message box
def saved_invoice():
    """dialog to advise user that an invoice was created and saved"""
    messagebox.showinfo("Successful", "This invoice has been successfully saved!\n\nYou can view this in Microsoft Word.")


def deleted(parent):
    """dialog to advise user that booking was deleted"""
    messagebox.showinfo("Successful", "These details have been successfully deleted!", parent=parent)


def not_completed(parent, extra_info=''):
    """dialog to advise user that this booking cant be saved due to empty fields or invalid data"""
    messagebox.showerror('Error', 'Please ensure no inputs have been left empty and are completed with correct '
                                  'information.\n\n{}'.format(extra_info),
                         parent=parent)


def no_search_criteria(parent):
    """dialog to advise user that they need to enter a search criteria first"""
    messagebox.showerror("Error", "No search criteria! \n\nPlease make sure you have selected an event type and "
                                  "entered a date range. ", parent=parent)


def enter_from_date(parent):
    """dialog to advise user that they must select a start date before an end date"""
    messagebox.showerror("Error", "You have not selected a start date!", parent=parent)


def save_file_error(extra_info=''):
    """dialog to advise user that invoice could not be saved"""
    # Extra info will be passed through based on what failed
    messagebox.showerror('Error', 'Error occurred while trying to save file\n\n{}'.format(extra_info))


def limit_reached(extra_info, parent=None):
    """dialog to advise user that they have entered too many characters"""
    messagebox.showerror('Error', 'The Character limit of {} has been reached'.format(extra_info), parent=parent)


def number_limit_reached(extra_info, parent=None):
    """dialog to advise user if they have gone over the allowed value"""
    messagebox.showerror('Error', 'The limit of {} has been reached'.format(extra_info), parent=parent)

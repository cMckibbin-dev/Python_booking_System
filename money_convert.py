import locale

locale.setlocale(locale.LC_ALL, '')


def pound_string(value):
    """function will convert a value into a string of pounds and pence containing a £ sign"""
    total = locale.currency(value, grouping=True)
    return total

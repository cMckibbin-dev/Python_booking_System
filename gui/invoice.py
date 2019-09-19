from gui.view_details import *


def CostBreakDownUI(master, booking):
    # widgets for invoice form
    CostBreakHeading = Label(master, text='Cost Break Down', font=style.textHeading, bg=style.widgetBG)
    totalExVATLabel = Label(master, text='Total ex VAT:', font=style.textNormal, bg=style.widgetBG)
    totalExVATInfo = Label(master, text=mc.pound_string(booking.subTotal()), font=style.textNormal, bg=style.widgetBG)

    VATTotalLabel = Label(master, text='VAT:', font=style.textNormal, bg=style.widgetBG)
    VATTotalInfo = Label(master, text=mc.pound_string(booking.VAT()), font=style.textNormal, bg=style.widgetBG)

    TotalLabel = Label(master, text='Total:', font=style.textNormal, bg=style.widgetBG)
    TotalInfo = Label(master, text=mc.pound_string(booking.total()), font=style.textNormal, bg=style.widgetBG)

    # grid layout for widgets
    CostBreakHeading.grid(row=20, column=0, columnspan=2, sticky=NSEW, padx=style.paddingX, pady=style.paddingY)

    totalExVATLabel.grid(row=21, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
    totalExVATInfo.grid(row=21, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

    VATTotalLabel.grid(row=22, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
    VATTotalInfo.grid(row=22, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)

    TotalLabel.grid(row=23, column=0, sticky=E, padx=style.paddingX, pady=style.paddingY)
    TotalInfo.grid(row=23, column=1, sticky=W, padx=style.paddingX, pady=style.paddingY)


class InvoiceConference(ViewDetailsConference):
    def __init__(self, master, booking):
        super().__init__(master, booking)

        # configure window
        self.master.title('Invoice Conference')
        # overriding parent class InvoiceButton to be save button
        self.buttonInvoice.configure(text='Save')
        # overriding parent heading
        self.Heading.configure(text='Invoice for Conference')
        # setting cost break down UI on to window
        CostBreakDownUI(self.master, booking)
        # moving buttons to bottom of window
        self.buttonFrame.grid(row=24, column=0, columnspan=2)


class InvoiceParty(ViewDetailsParty):
    def __init__(self, master, booking):
        super().__init__(master, booking)
        # configure window
        self.master.title('Invoice Party')
        # overriding parent class InvoiceButton to be save button
        self.buttonInvoice.configure(text='Save')
        # overriding parent heading
        self.Heading.configure(text='Invoice for Party')
        # setting cost break down UI on to window
        CostBreakDownUI(self.master, booking)
        # moving buttons to bottom of window
        self.buttonFrame.grid(row=24, column=0, columnspan=2)


class InvoiceWedding(ViewDetailsWedding):
    def __init__(self, master, booking):
        super().__init__(master, booking)
        # configure window
        self.master.title('Invoice Wedding')
        # overriding parent class InvoiceButton to be save button
        self.buttonInvoice.configure(text='Save')
        # overriding parent heading
        self.Heading.configure(text='Invoice for Wedding')
        # setting cost break down UI on to window
        CostBreakDownUI(self.master, booking)
        # moving buttons to bottom of window
        self.buttonFrame.grid(row=24, column=0, columnspan=2)



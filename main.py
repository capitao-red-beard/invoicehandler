from datetime import date as d
from typing import Set
from uuid import uuid1


class Invoice:
    def __init__(self, date: d, total:float):
        self.date = date
        self.reference_number: uuid1 = uuid1()

        if not self.valid_invoice_amount(total):
            raise InvalidInvoiceValueError
        else:
            self.total = total

    @staticmethod
    def valid_invoice_amount(value: float) -> bool:
        return True if 0.0 < value < 200000000.00 else False


class InvoiceStats:
    MAX_INVOICE_SET_SIZE = 20000000 # Twenty Million

    def __init__(self, total: float, invoice_set: Set[Invoice]):
        self.total = total
        self.invoice_set = invoice_set

    def add_invoices(self, invoice_set: Set[Invoice]) -> None:
        pass

    def add_invoice(self, invoice: Invoice) -> None:
        if len(list(self.invoice_set)) > self.MAX_INVOICE_SET_SIZE:
            raise InvalidInvoiceSetError
        else:
            self.invoice_set.add(invoice)


    def clear(self):
        self.invoice_set.clear()

    def get_median(self):
        pass

    def get_mean(self):
        pass

    @staticmethod
    def valid_invoice_set(invoice_list: Set[Invoice]) -> bool:
        return True if len(invoice_list) <= 20000000 else False


class InvalidInvoiceValueError(Exception):
    message = '\nException: InvalidInvoiceError:' \
              '\nYour invoice is invalid.' \
              '\nInvoices may only have a total between 0.0 and 200000000.00.'

class InvalidInvoiceSetError(Exception):
    message = '\nException: InvalidInvoiceSetError:' \
              '\nYour invoice set is invalid.' \
              '\nAn invoice set may only contain up to 20000000 items.'

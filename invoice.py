# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.pyson import If, Eval

__all__ = ['Invoice']


class Invoice:
    __metaclass__ = PoolMeta
    __name__ = 'account.invoice'

    @classmethod
    def __setup__(cls):
        super(Invoice, cls).__setup__()
        cls.accounting_date.states['required'] = Eval('state').in_(
                If(Eval('type') == 'in',
                    ['validated', 'posted', 'paid'],
                    ['posted', 'paid']))

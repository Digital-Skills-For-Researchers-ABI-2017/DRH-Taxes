#!/usr/bin/env python
from drhtaxes.individual import Tax
from drhtaxes.admission import admission
from drhtaxes.corporate import COR
from drhtaxes.output import tax_compare


def main():
    """
    This function brings together calculated income tax and
    calculated corporate tax reports a comparison
    """
    
    print('Application DRH Taxes')
    income, losses = admission()
    in_tax = Tax()
    indi_calc_tax = in_tax.calc_tax(income)
    cor_tax = COR()
    corp_calc_tax = cor_tax.corp(income,losses)

    msg = tax_compare(corp_calc_tax,indi_calc_tax)

    print(msg)
   
if __name__ == '__main__':
    main()



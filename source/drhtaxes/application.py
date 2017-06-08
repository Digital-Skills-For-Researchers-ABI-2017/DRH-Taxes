#!/usr/bin/env python
from drhtaxes.individual import Tax
def main():
    print('Application DRH Taxes')
    income = 5
    in_tax = Tax()
    indi_calc_tax = in_tax.calc_tax(income)
    print(indi_calc_tax)

if __name__ == '__main__':
    main()


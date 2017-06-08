def tax_compare(corp,tax):
    '''
    Define the function tax_compare that uses corp and tax as inputs, it compares them by computing the difference between the two actual taxes and returns the amount of money saved, as well as a statement of recommendation''

    difftax is a numerical variable that stores the absolute value of the difference between corporate and individual taxes
    '''

    difftax = abs(corp-tax);

    '''
    The nested IF statements below compare the values of corporate and individual taxes, returning the amount of money saved, as well as a statement of recommendation
    '''

    if (corp == tax):
        result = 'Choose either filing a income tax return as a corporate or as an individual'
    elif (corp > tax):
        result = 'Individual tax rate is the best method as the taxable income would be reduced by NZD %d' %difftax
    elif (corp < tax):
        result = 'Corporate tax rate is the best method as the taxable income would be reduced by NZD %d' % difftax 
    return result
    

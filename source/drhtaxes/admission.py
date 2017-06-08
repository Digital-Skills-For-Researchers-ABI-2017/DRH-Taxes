import sys

def tax_input_checker(typed_input):
    """
    Returns true if the input string cannot be converted to a float, and false if otherwise
    """
    try:
        f = float(typed_input)
    except ValueError:
        return False
    return True

def admission():
    """
    Recieves two inputs from the command line and makes sure they can be passed as floats to the individual and corporate modules
    """
    
    if len(sys.argv) == 3:
        
        income = sys.argv[1]


        if tax_input_checker(income) == False:
            exit("Error Code: HUGH")

        losses = sys.argv[2]
        
        if tax_input_checker(losses) == False:
            exit("Error Code: JELLYBEAN")

                
        return income, losses
    else:
        exit("Error Code: PANDA")

    



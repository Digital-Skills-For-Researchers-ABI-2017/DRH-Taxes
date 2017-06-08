# DRH-Taxes
# Tax calculation for the Democratic Republic of Hughland [1]

Aim: To determine the amount in paid taxes is when filing income taxes as an individual or as a coorporation under the tax laws of the Democratic Republic of Hughland (DRH) [2]

## Project description
This software allows clients to compare how much income taxes should be paid whether one is filing as an individual or as a corporation. 
Under the current tax laws of of the DRH, taxes are calculated as follows:

### When filing as an indivudual
- 0%, for under $10,000
- 17% for the bracket between $10,000-$30,000
- 28% for the bracket between $30,000-70,000
- 35% for all income above $70,000

### When filing as a corporation
- 20% applied to the total income
- If income is above $80,000, then incurred losses can be subtracted from income

## Running the programme using the test data

### Installation

Use pip to install the application::

  pip install git+https://github.com/Digital-Skills-For-Researchers-ABI-2017/DRH-Taxes.git

### Running

Once installed the application can be run by typing::

  drhtaxes <income> <losses>

### Expected output
### Corporate tax calculation
- Tax ($): integer or decimal when filing as a corporate 

## Implementation and architecture

<center><img src=images/DRH-taxes-top-level-flowchart.png width=400 height=400 /></center>

### Input
A float or integer value to represent the income as the first argument.  A float or integer value to represent the losses as the second argument.

### Calculate tax as individual
### Calculate tax as corporation
- Write a script to calculate corporate tax
- Run unit test
- Push and pull request to respository
- Amend according to feedback

### Output
Define the function tax_compare that uses corporate and individual tax as inputs , computes difference. The code returns two items: amount saved in dollars and a string which is statement of recommendation.

The final output is a statement printed to the screen that describes which tax avenue is best suited for the given inputs.

## Quality control

We have testing in place to make sure the code is functioning as expected.

## Prerequisites

Python and pip available from the command line.

### Operating System

Windows, OS X, and GNU/Linux.

### Programming Language
- Python

### Additional System Requirements

### Dependencies

## Input data requirements
### Corporate tax calculation
- Income ($): integer or decimal
- Incurred loss ($): interger or decimal

## Limitations

## Error Codes

### Error Code: HUGH
This error code means that your typed input in the first command line argument cannot be converted into a float value, likely due to the presence of non-numeric characters, or multiple floating points.

### Error Code: JELLYBEAN
This error code means that your typed input in the second command line argument cannot be converted into a float value, likely due to the presence of non-numeric characters, or multiple floating points.

### Error Code: PANDA
This error code means you have supplied an incorrect number of input arguments, there should only be two, income, followed by losses.

## List of contributors

## Licencing

## Acknowledgements

## Funding statement

## Competing interests

## References






[1] *The republic does not exist. (Hugh, however, does)*

[2] *Don't google it. As I said, it does not exist.*

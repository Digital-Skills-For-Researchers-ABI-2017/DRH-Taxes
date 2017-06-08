class COR(object):
	""" Tax calculation for the Democratic Republic of
	Hughland when filing as a corporation """

	def corp(self,income,incurred_loss):
		""" The input will be the income and incurred losses The
		output will be the tax """

		if income < 80000:
			tax = (income*0.2) #If income is below $80,000, 20% applied to the total income
	
		elif income >= 80000:
			tax = (income - incurred_loss)*0.2 #If income is above $80,000, then incurred losses can be subtracted from income
		return tax
		

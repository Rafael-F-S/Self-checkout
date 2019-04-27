from checkoutregister import CheckoutRegister


print("*************************************************************")
print("******************** Product List****************************")
print(" 1 : Milk")
print(" 2 : Tomato")
print(" 3 : Chocolate")
print(" 4 : Bread")
print(" 5 : Biscuit")
print(" 6 : Facewash\n")

class Main:
	check = CheckoutRegister()
	def __init__(self):
		pass
	check.scan_new_item()
#Program start
main = Main()

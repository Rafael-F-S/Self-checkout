from product import Product


class CheckoutRegister:
	# Constructor
	def __init__(self):
		self.items_purchased = [] 		# List of purchased items by customer 
		self.total = 0					# total of the amount amt_payed by customer
		self.change = 0					# Change need to be given to the customer

	# Scan item function
	def scan_new_item(self):
		barcode = input('Type the barcode: ')
		product_list = {'1': ['Milk', 2, 'L'], '2': ['Tomato', 3, 'Kg'], '3': ['Chocolate',  2, 'unit'], '4': ['Bread', 3, 'unit'], '5': ['Biscuit', 5, 'unit'], '6': ['Facewash', 4, 'unit']}
		if barcode in product_list:
			product = Product(product_list[barcode])
			print(" {} ---------------- ${}/{}.".format(product.name, product.price, product.unit))
			quantity = int(input("How many of this product you want? \n"))

			self.total = self.total + (product.price * quantity)
			self.items_purchased.append([barcode, product.name, product.price, product.unit, quantity])
		else:
			print("Error: Barcode does not exist in our database")
		
		self.another_product_scan()

	# Ask for permission to scan another item
	def another_product_scan(self):
		scan_another_product = input(" Do you want to scan another product y/n: ").upper()
		if scan_another_product == 'Y':
			self.scan_new_item()
		elif scan_another_product == 'N':
			self.accept_payment()
		else:
			print("Enter valid Character")
			self.another_product_scan()

	# Accept payment method
	def accept_payment(self):
		self.bag_items()
		print("Payment Due: $", self.total)
		amt_payed = float(input("Amount to pay: $"))
		amt_payed = self.get_float(amt_payed)

		if amt_payed > self.total:
			print("change : $", (amt_payed - self.total))
			self.change = amt_payed - self.total

		elif amt_payed < self.total:
			print("Amount Due: $", (self.total - amt_payed))
			self.total = self.total - amt_payed
			self.accept_payment()
		else:
			print("Payment Done!")

		print("/ / / / / / / / Final Receipt \ \ \ \ \ \ \ \  ")

		self.print_receipt()
		
		print("Thank you for Shopping at Fed Uni")
		self.new_customer()

	# Get floating values of payment
	def get_float(self, value):
		try:
			if value >= 0:
				val = float(value)
				return value
			else:
				print("We don't accept negative money!")
				self.accept_payment()
		except ValueError:
			print("Enter a valid number")
			accept_payment()

	# Getting List of bagged items
	def bag_items(self):
		# Input for bagged and non-bagged items
		bag_weight = 5.0
		current_bag_items = []
		current_bag_weight = 0
		items_exceeded = []

		for product in self.items_purchased:
			# print(product[4])
			bag_weight = bag_weight - current_bag_weight
			if product[4] <= bag_weight:
				current_bag_weight = current_bag_weight + product[4]
			else: 
				self.items_purchased.remove(product)
			current_bag_items.append(product)

	# Get receipt after shopping
	def print_receipt(self):
		print("Name          Quantity         Price")
		for item in self.items_purchased:
			print("{}           {}                 {}".format(item[1], item[4], str(item[4]*item[2])))

		print("Total Amount Due: $", self.total)
		print("Amount Received: $",(self.total + self.change))
		print("Change Given: $", self.change)

	def new_customer(self):
		next_custom = input("Press for (N)ext Customer or (Q)uit? ").upper()
		if next_custom == 'N':
			self.total = 0
			self.change = 0
			self.items_purchased = []
			self.scan_new_item()
		elif next_custom == 'Q':
			exit()
		else:
			print("invalid Character!")
			self.new_customer()


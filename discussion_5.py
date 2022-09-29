from cgi import print_arguments
from sys import addaudithook
import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence [i] == 'a':
			total += 1
	return (total)


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
	

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self, item):
		max_stock = item[0]
		for i in item:
			if i.stock > max_stock.stock:
				

	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price = self.items [0]
		for price in self.items:
			if price > max_price:
				max_price = price
		print (max_price)




# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		ware = Warehouse()

		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("this is a test"), 1)
		self.assertEqual(count_a("aaa"), 3)

	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):

		shop = Warehouse()

		shop.add_item (self.item1)

		check = False

		if self.item1 in shop.items:
			check = True
	
		self.assertTrue(check)



	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):

		shop = Warehouse()

		shop.add_item(self.item1)
		shop.add_item(self.item2)
		shop.add_item(self.item3)
		shop.add_item(self.item4)

		most = shop.get_max_stock(shop.items)
		
		self.assertEqual(most, self.item3)
	


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):

		shop = Warehouse()

		max
		pass
		

def main():
	test_ware = Warehouse()
	
	unittest.main()
	unittest

if __name__ == "__main__":
	main()
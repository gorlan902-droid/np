class WishList :
	_name : str
	_items : list

	def __init__(self, name = "", items = None):
		self._name = name

		if items is None
			self._items = []
		else
			self._items = items

	def setName(self, name):
		self._name = name

	def getItems(self):
        return self._items

	def addItem(self, item):
		self._items.append(item)

	def calcTotalPrice(self):
		total = 0.0

		for item in self._items:
			if hasattr(item, 'getPrice'):
				total+=item.getPrice()

		return total
class Item :
	
	_title : str = ""
	_link : str = ""
	_price : float = 0.0
	_photo : str = ""

	def __init__(self, _title = "", _link = "", _price = 0.0, photoUrl = "https://example.com/default.jpg"):
		self._title = _title
		self._link = _link
		self._price = (float)_price
		self._photo = photoUrl

	def getTitle(self):
		return self._title

	def getPrice(self):
		return self._price

	def getLink(self):
		return self._link
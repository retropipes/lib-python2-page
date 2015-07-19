class Page(object):
		
	def __init__(self, experience=False):
		self.__coeff = []
		self.__power = []
		self.__exp = bool(experience)
	
	def addCoefficient(self, value):
		self.__coeff.append(value)
		self.__power.append(len(self.__coeff))
		
	def addCoefficientAndPower(self, value, powerValue):
		self.__coeff.append(value)
		self.__power.append(powerValue)
		
	def getCoefficient(self, power):
		return self.__coeff[self.__power[power]]
	
	def getCoefficientCount(self):
		return len(self.__coeff)
		
	def getPower(self, which):
		return self.__power[which]
		
	def getPowerCount(self):
		return len(self.__power)
		
	def isExperience(self):
		return self.__exp
		
	def removeCoefficient(self):
		self.__coeff.pop(len(self.__coeff) - 1)
		self.__power.pop(len(self.__power) - 1)
		
	def removeCoefficientAndPower(self):
		self.removeCoefficient()
	
	def setCoefficient(self, power, value):
		self.__coeff[self.__power[power]] = value
		
	def setExperience(self, value):
		self.__exp = bool(value)
		
	def setPower(self, which, value):
		self.__power[which] = value

	def evaluate(self, paramValue):
		result = 0
		counter = 0
		for c in self.__coeff:
			result = result + c * paramValue ** self.__power[counter]
			counter = counter + 1
			if self.__exp:
				result = result - c
		return result
		
	def integerEvaluate(self, paramValue):
		result = 0
		counter = 0
		for c in self.__coeff:
			result = long(result + c * paramValue ** self.__power[counter])
			counter = counter + 1
			if self.__exp:
				result = long(result - c)
		return result
		
	def evaluateToList(self, start, end, increment=1):
		result = []
		counter = start
		while counter <= end:
			result.append(self.evaluate(counter))
			counter = counter + increment
		return result
		
	def integerEvaluateToList(self, start, end, increment=1):
		result = []
		counter = long(start)
		finish = long(end)
		while counter <= finish:
			result.append(self.integerEvaluate(counter))
			counter = counter + long(increment)
		return result
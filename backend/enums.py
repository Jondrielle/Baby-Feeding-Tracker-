from enum import Enum 

class FeedingMethod(str, Enum):
	breast = "breastfeeding"
	bottle = "bottle"
	food = "food"

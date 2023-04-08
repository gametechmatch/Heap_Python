#################################################################
# HeapNodeIndexData.py
#################################################################
# Author: gametechmatch
# Date: 4/2/2023
#################################################################
# This class contains static methods to find information based
# on a given node in a heap
#################################################################
# This class uses math from Mersenne numbers / the gaussian
# binomial coefficient [n, 1] for q = 2
#################################################################
from HeapLevelData import *
from math import *

class HeapNodeIndexData:

	# This method returns the level number based on the lowest
	# possible index for the unknown level
	@staticmethod
	def getLevelFromMinIndexInLevel(minNodeIndex):
		level = ((log2(minNodeIndex+1)) + 1)
		return level

	# This method returns the level number based on the highest
	# possible index for the unknown level
	@staticmethod
	def getLevelFromHighestIndexInLevel(maxNodeIndex):
		level = (log2(maxNodeIndex+2))
		return level

	# This method returns the level that a given node's index would fall in
	@staticmethod
	def getLevelFromNodeIndex(nodeIndex):
		# Mersenne numbers / the gaussian binomial coefficient
		# [n, 1] for q = 2
		level = floor(HeapNodeIndexData.getLevelFromMinIndexInLevel(nodeIndex))
		return level

	# This method returns true if a node's index is the highest possible index
	# for its level (otherwise returns false)
	@staticmethod
	def NodeInHighestIndex(nodeIndex):
		level = HeapNodeIndexData.getLevelFromNodeIndex(nodeIndex)
		highestIndex = HeapLevelData.getMaxIndexInHeapLevel(level)

		# If node's index is the max index for the level, return true
		if nodeIndex == highestIndex:
			return True

		# Else return false
		return False

	# This method returns true if a node's index is the lowest possible index
	# for its level (otherwise returns false)
	@staticmethod
	def NodeInLowestIndex(nodeIndex):
		level = HeapNodeIndexData.getLevelFromNodeIndex(nodeIndex)
		minIndex = HeapLevelData.getMinIndexInHeapLevel(level)

		# If node's index is the min index for the level, return true
		if nodeIndex == minIndex:
			return True

		# else return false
		return False

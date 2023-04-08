#################################################################
# HeapLevelData.py
#################################################################
# Author:  gametechmatch
# Date: 4/2/2023
#################################################################
# This class contains static methods to find information based
# on a given level of a heap
#################################################################
class HeapLevelData:
	@staticmethod
	def getMinNodesInHeapByLevel(level):
		heapMinNodes = (2**(level - 1))
		return heapMinNodes

	@staticmethod
	def getTotalNodesOnLevel(level):
		totalNodesOnLevel = (2**(level - 1))
		return totalNodesOnLevel

	@staticmethod
	def getMaxNodesInHeapByLevel(level):
		heapMaxNodes = ((2**level) - 1)
		return heapMaxNodes

	@staticmethod
	def getMinIndexInHeapLevel(level):
		minIndexInHeapLevel = ((2**(level-1))-1)
		return minIndexInHeapLevel

	@staticmethod
	def getMaxIndexInHeapLevel(level):
		maxIndexInHeapLevel = ((2**level) - 2)
		return maxIndexInHeapLevel

#################################################################
# Heap.py
#################################################################
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# Additional methods:
# .__levels_loop_deepest_lefts()
# .levels_loops()
# .__levels()
# .levels()
#################################################################
# Author of additional methods: gametechmatch
# Date: 4/2/2023
#################################################################
# This file exectues a Heap. Each heap is stored as a list &
# each node (key, value) is stored as a tuple
#################################################################
from HeapLevelData import *
from HeapNodeIndexData import *

# This class implements a heap
#################################################################
class Heap(object):

   # This constructor initializes an empty heap
   #################################################################
   def __init__(self, size=2):
      self._array = [None] * size # Heap stored as list
      self._totalItems = 0
      self._totalLevels = 0

   # This method tests if the heap is empty
   #################################################################
   def isEmpty(self): return self._totalItems == 0

   # This method returns true if the heap's total items matches the
   # length of the list storing the heap
   #################################################################
   def isFull(self): return self._totalItems == len(self._array)

   # This method returns the total items being stored
   #################################################################
   def __len__(self): return self._totalItems

   # This method returns the item with the maximum value
   #################################################################
   def peek(self): return None if self.isEmpty() else self._array[0]

   # This method returns the heap tree index of input node's parent
   #################################################################
   def parent(self, indexOfInputNode):
      indexOfParentNode = (indexOfInputNode - 1) // 2
      return indexOfParentNode

   # This method returns the index of the left child in heap tree
   #################################################################
   def leftChild(self, indexOfInputNode):
      #print("----------------------------------------------------")
      #print(f"left child method")
      #print(f" indexOfInputNode: {indexOfInputNode}")
      #print(f" indexOfLeftChild: {indexOfInputNode * 2 + 1}")
      #print("----------------------------------------------------")
      indexOfLeftChild = indexOfInputNode * 2 + 1
      return indexOfLeftChild

   # This method returns the index of the right child in heap tree
   #################################################################
   def rightChild(self, indexOfInputNode):
      indexOfRightChild = (indexOfInputNode * 2) + 2
      return indexOfRightChild

   # This method inserts a new item in a heap
   #################################################################
   def insert(self, item):
      # If insertion would go beyond array then expand heap array
      if self.isFull():
         self._growHeap()

      # Store item at end of array, increase total, & sift last
      # item up. (totalItems = last index + 1)
      self._array[self._totalItems] = item
      self._totalItems += 1
      self._siftUp(self._totalItems - 1)

   # This method grows the array for the heap
   #################################################################
   def _growHeap(self):
      # Store the current array & double the object's array attribute
      currentArray = self._array
      self._array = [None] * max(1, 2 * len(self._array))

      # Loop over all current items & copy them to the new array
      for i in range(self._totalItems):
         self._array[i] = currentArray[i]

   # This method removes the top item of the heap and returns it
   #################################################################
   def remove(self):
      # If the heap is empty, raise heap underflow error
      if self.isEmpty():
         raise Exception("Heap underflow")

      # Store the top item & decrease the item count
      root = self._array[0]
      self._totalItems -= 1

      # Move the last to the root
      self._array[0] = self._array[self._totalItems]

      # Clear for garbage collection
      self._array[self._totalItems] = None

      # Move last item down into position & return the top item
      self._siftDown(0)
      return root

   # This method sifts item i up toward the root to preserve heap
   # condition, recursively.
   #################################################################
   def _siftUp_rec(self, i):
      # The root node, i = 0, cannot go higher, so done
      if i <= 0:
         return

      # If parent's value is less than that of item i, swap the items &
      # continue to sift up at parent
      parentIndex = self.parent(i)
      if (self._array[parentIndex][0] < self._array[i][0]):
         self._swap(parentIndex, i)
         self._siftUp(parentIndex)

   # This method sifts item i up toward root to preserve the heap
   # condition
   #################################################################
   def _siftUp(self, i):

      # The root node, i = 0, cannot go higher, so done.
      if i <= 0:
         return

      # Store item at cell i and store item's value
      item = self._array[i]
      itemValue = item[1]


      # While i is below the root
      while 0 < i:

         parentIndex = self.parent(i)

         # if parent's value is less than that of
         # item i, copy parent to i and continue up the tree
         if (self._array[parentIndex][1] < itemValue):
            self._array[i] = self._array[parentIndex]
            i = parentIndex

         # If parent's value is greater or equal to the item value,
         # then we have found where item i belongs
         else:
            break

      # Move item i into final position
      self._array[i] = item

   # This method sifts item i down to preserve the heap condition
   #################################################################
   def _siftDown_rec(self, i):

      # Find the child indices and see if they are in the heap
      left, right = self.leftChild(i), self.rightChild(i)
      if left < len(self):

         # If both children are present, compare their values and
         # use the largest
         if right < len(self):
            maxi = right if (self._array[left][1] <
                             self._array[right][1]) else left

         # Else no right child, so max child is on the left
         else:
            maxi = left

         # If item i's value is less than max child's value, then swap
         # item i with max child and continue ._siftdown()
         if (self._array[i][1] < self._array[maxi][1]):
            self._swap(i, maxi)
            self._siftDown(maxi)

   # This method sifts the item i down to preserve the heap condition
   #################################################################
   def _siftDown(self, i):

      firstleafIndex = len(self) // 2

      # If item i is at or below leaf level, it cannot be moved down
      if i >= firstleafIndex:
         return

      item = self._array[i]
      itemValue = item[1]

      # While i above leaf level
      while i < firstleafIndex:

         # Find children & assume left child has larger value
         left, right = self.leftChild(i), self.rightChild(i)
         maxi = left

         # If both children are present, and left child has smaller value
         # then use right child
         if (right < len(self) and self._array[left][1] <
             self._array[right][1]):
            maxi = right

         # If item i's value is less than max child's value, then move max
         # child up
         if (itemValue < self._array[maxi][1]):
            self._array[i] = self._array[maxi]
            i = maxi

         # If item i's value is greater than or equal to larger child,
         # then found position
         else:
            break

      # Move item to its final position
      self._array[i] = item

   # This method swaps item i and item j in the heap array
   #################################################################
   def _swap(self, i, j):
      self._array[i], self._array[j] = self._array[j], self._array[i]

   # This method returns the heap in string format
   #################################################################
   def __str__(self):
      returnedInfo = '<'

      # Start at height 0, which has a width of 1 node (the root)
      heightInLevels = 0
      levelWidthInNodes = 1

      # Loop over all height levels
      while levelWidthInNodes <= len(self):

         # After first height row is added, separate other rows with a comma + space
         if len(returnedInfo) > 1:
            returnedInfo += ', '

         # Add row height plus values joined by commas
         returnedInfo += str(heightInLevels) + ': (' + ', '.join([str(self._array[j][1])
             for j in range(levelWidthInNodes - 1,
                            min(len(self), levelWidthInNodes - 1 + levelWidthInNodes))]) + ')'

         # Go to next height level, where the width doubles
         heightInLevels += 1
         levelWidthInNodes += levelWidthInNodes

      # Close with right bracket and return
      return returnedInfo + '>'

   # This method is a generator that traverses & yields all heap items
   #################################################################
   def traverse(self):
      for currentItemIndex in range(len(self)):
         yield self._array[currentItemIndex]

   # This method prints the heap tree with the root on the left of
   # the screen & indents by a few spaces for each level starting
   # with indent at node i.
   #################################################################
   def print(self, indentBy=4, currentIndentString='', heapIndex=0):

      # If item i is not in the tree, don't print it & return
      # to the prior iteration of the print method
      if heapIndex >= len(self):
         return

      # Calculate the indent for the next iteration
      nextIndentString = currentIndentString + ' ' * indentBy

      # Try to recursively go through the print method to travel
      # to the next farthest right node (of current node) & print it
      self.print(indentBy, nextIndentString, self.rightChild(heapIndex))

      # Print the next node within bounds
      print(currentIndentString, self._array[heapIndex])

      # Use calculation for left child node to go back and find next
      # node to print
      self.print(indentBy, nextIndentString, self.leftChild(heapIndex))

   # This method returns the total levels in the heap
   #################################################################
   def levels(self):
      # if heap is empty, return 0
      if self._totalItems == 0:
         return 0

      return (self.__levels())

   # This method is the private helper method that returns the total
   # levels in the heap to the levels_loop method
   #################################################################
   def __levels(self):
      lastNodeIndex = (self._totalItems - 1)
      self._totalLevels = HeapNodeIndexData.getLevelFromNodeIndex(lastNodeIndex)
      return self._totalLevels

   # This method returns the total levels in the heap with the
   # recursive .__levels_loop_deepest_left() private method
   #################################################################
   def levels_loop(self):
      # if heap is empty, return 0
      self._totalLevels = 0
      if self._totalItems == 0:
         return 0

      # Get total levels from recursive private method & return
      # the updated value
      self.__levels_loop_deepest_left()
      return self._totalLevels


   # This method is the private recursive helper method that returns
   # the total levels in the heap after finding the deepest left level
   #################################################################
   def __levels_loop_deepest_left(self, heapIndex=0, totalLevels=0):
      # increment up total levels
      totalLevels += 1

      # If item at heap index is not in the heap, we went 1 level too
      # deep. Set self._totalLevels = totalLevels - 1 & return to
      # each prior iteration until exiting out to the calling method
      if heapIndex >= len(self):
         self._totalLevels = (totalLevels - 1)
         return

      # Keep recursively exiting the method
      self.__levels_loop_deepest_left(self.leftChild(heapIndex), totalLevels)

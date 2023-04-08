#################################################################
# HeapClient.py
#################################################################
# Author: gametechmatch
# Date: 4/2/2023
#################################################################
# This file creates heaps, tests different operations on them,
# and displays the total levels calculated in two different ways
#################################################################

from Heap import *
from random import *

def main():
   # Create heap
   myHeap = Heap()

   print("===================================== 0 ITEMS ====================================")
   # Create empty list to test heap
   listOfValues = []
   testHeap(myHeap, listOfValues)

   print("===================================== 33 ITEMS ====================================")
   # Create list of 33 values to test heap
   for i in range(33):
      listOfValues.append(randint(200, 600))
   testHeap(myHeap, listOfValues)

   print("================================ RANDOM TOTAL ITEMS ===============================")
   # Create additional lists of random lengths to test Heap class
   totalTestsCompleted = 0
   while totalTestsCompleted < 5:

      # Clear & refill list
      listOfValues.clear()
      for i in range(randint(0, 33)):
         listOfValues.append(randint(200, 600))

      # retest Heap class
      testHeap(myHeap, listOfValues)

      # increment total tests
      totalTestsCompleted += 1

   print("===================================== 1 ITEM ====================================")
   listOfValues = [100]
   testHeap(myHeap, listOfValues)

   print("===================================== 2 ITEMS ====================================")
   listOfValues = [100, 50]
   testHeap(myHeap, listOfValues)

   print("===================================== 3 ITEMS ====================================")
   listOfValues = [100, 50, 500]
   testHeap(myHeap, listOfValues)

   print("===================================== 4 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600]
   testHeap(myHeap, listOfValues)

   print("===================================== 5 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400]
   testHeap(myHeap, listOfValues)

   print("===================================== 6 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400, 450]
   testHeap(myHeap, listOfValues)

   print("===================================== 7 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400, 450, 75]
   testHeap(myHeap, listOfValues)

   print("===================================== 8 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400, 450, 75, 44]
   testHeap(myHeap, listOfValues)

   print("===================================== 9 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400, 450, 75, 44, 90]
   testHeap(myHeap, listOfValues)

   print("===================================== 10 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400, 450, 75, 44, 90, 92]
   testHeap(myHeap, listOfValues)

   print("===================================== 11 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400, 450, 75, 44, 90, 92, 94]
   testHeap(myHeap, listOfValues)

   print("===================================== 12 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400, 450, 75, 44, 90, 92, 94, 22]
   testHeap(myHeap, listOfValues)

   print("===================================== 13 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400, 450, 75, 44, 90, 92, 94, 22, 700]
   testHeap(myHeap, listOfValues)

   print("===================================== 14 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400, 450, 75, 44, 90, 92, 94, 22, 700, 1]
   testHeap(myHeap, listOfValues)

   print("===================================== 15 ITEMS ====================================")
   listOfValues = [100, 50, 500, 600, 400, 450, 75, 44, 90, 92, 94, 22, 700, 1, 645]
   testHeap(myHeap, listOfValues)

# This function tests the Heap class by inserting values, printing
# heap, printing total levels in heap, and removing items from heap
#################################################################
def testHeap(myHeap, values):

   # Insert values into heap
   print("####################### INSERTING ITEMS IN HEAP ##################")
   print(". . . ")
   for key, value in enumerate(values):
      myHeap.insert((key, value))

   # print heap
   print("####################### FINAL RESULT AFTER INSERTING VALUES ##################")
   myHeap.print()

   # print total levels in heap
   print("####################### PRINT TOTAL LEVELS IN HEAP ##################")
   print(f"Total Levels In Heap (using math): {myHeap.levels()}")
   print(f"Total Levels In Heap (using recursion): {myHeap.levels_loop()}\n")

   # Remove items in heap
   print("####################### REMOVING ITEMS IN HEAP ##################")
   for i in range(len(myHeap)):
      print('Removing item #', i + 1, 'returns', myHeap.remove())
      print('Remaining heap:', myHeap)

   # Display what heap has after removing all items
   print()
   print('After removing all items the heap contains:', myHeap)

# execute main function
if __name__ == '__main__':
	main()

class ListOperations:
    def __init__(self):
        self.list1 = []
        for iter in range(int(input("Enter number of elements of first list: "))):
            self.list1.append(int(input("Enter element: ")))
        print(self.list1)

        self.list2 = []
        for iter in range(int(input("Enter number of elements of second list: "))):
            self.list2.append(int(input("Enter element: ")))
        print(self.list2)
    def findLargest(self):
        largestElem = 0
        listindex = None
        for iter in range(len(self.list1)):
            if self.list1[iter] > largestElem:
                largestElem = self.list1[iter]
                listindex = 1
        
        for iter in range(len(self.list2)):
            if self.list1[iter] > largestElem:
                largestElem = self.list2[iter]
                listindex = 2
        print(f"Largest element among both lists is {largestElem} belonging to list {listindex}")
    def largestAndSmallestInEach(self):
        largestIn1 = max(self.list1)
        smallestIn1 = min(self.list1)
        print(f"The largest element in {self.list1} is {largestIn1} and the smallest element is {smallestIn1}")

        largestIn2 = max(self.list2)
        smallestIn2 = min(self.list2)
        print(f"The largest element in {self.list2} is {largestIn2} and the smallest element is {smallestIn2}")
    def Combine(self):
        finalList = self.list1 + self.list2
        print(f"The combined list of {self.list1} and {self.list2} is {finalList}")

obj1 = ListOperations()
obj1.findLargest()
obj1.largestAndSmallestInEach()
obj1.Combine()
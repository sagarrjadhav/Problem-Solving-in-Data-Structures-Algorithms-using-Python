#!/usr/bin/env python
""" Source for module Searching """

class Searching:
    """ Source for class Searching """
    def __init__(self):
        """ Source for method __init__ """

    @classmethod
    def main1(cls, args):
        first = [1, 3, 5, 7, 9, 25, 30]
        s = Searching()
        print s.linearSearchSorted(first, 7, 8)

    def linearSearchUnsorted(self, arr, size, value):
        i = 0
        while i < size:
            if value == arr[i]:
                return True
            i += 1
        return False

    def linearSearchSorted(self, arr, size, value):
        i = 0
        while i < size:
            if value == arr[i]:
                return True
            elif value < arr[i]:
                return False
            i += 1
        return False
    
    @classmethod
    def main2(cls, args):
        first = [1, 3, 5, 7, 9, 25, 30]
        s = Searching()
        print s.BinarySearchRecursive(first, 3)      
        
    #  Binary Search Algorithm - Iterative Way
    def Binarysearch(self, arr, size, value):
        low = 0
        high = size - 1
        
        while low <= high:
            mid = low + (high - low) / 2
            #  To avoid the overflow
            if arr[mid] == value:
                return True
            elif arr[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def BinarySearchRecursive(self, arr, value):
        return self.BinarySearchRecursiveUtil(arr, 0, len(arr) - 1, value)

    #  Binary Search Algorithm - Recursive Way
    def BinarySearchRecursiveUtil(self, arr, low, high, value):
        if low > high:
            return False
        mid = low + (high - low) / 2
        #  To avoid the overflow
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            return self.BinarySearchRecursiveUtil(arr, mid + 1, high, value)
        else:
            return self.BinarySearchRecursiveUtil(arr, low, mid - 1, value)

    @classmethod
    def main3(cls, args):
        first = [1, 3, 5, 3, 9, 1, 30]
        s = Searching()
        s.printRepeating(first)
        s.printRepeating2(first)
        s.printRepeating3(first)
        s.printRepeating4(first, 50)


    def printRepeating(self, arr):
        size = len(arr)
        i = 0
        print " Repeating elements :: ",
        while i < size:
            j = i + 1
            while j < size:
                if arr[i] == arr[j]:
                    print arr[i],
                j += 1
            i += 1

    def printRepeating2(self, arr):
        size = len(arr)
        i = 0
        arr.sort()
        print " Repeating elements are :: ",
        while i < size:
            if arr[i] == arr[i - 1]:
                print arr[i],
            i += 1

    def printRepeating3(self, arr):
        size = len(arr)
        hs = set()
        i = 0
        print " Repeating elements are ::",
        while i < size:
            if arr[i] in hs:
                print arr[i],
            else:
                hs.add(arr[i])
            i += 1

    def printRepeating4(self, arr, valrange):
        size = len(arr)
        count = [0] * valrange
        i = 0
        print " Repeating elements are :: ",
        while i < size:
            if count[arr[i]] == 1:
                print arr[i],
            else:
                count[arr[i]] += 1
            i += 1
    
    @classmethod
    def main4(cls, args):
        first = [1, 30, 5, 13, 9, 31, 5]
        s = Searching()
        print s.getMax(first)
        print s.getMax2(first)
        print s.getMax3(first, 50)

    
    def getMax(self, arr):
        size = len(arr)
        maxval = arr[0]
        count = 1
        maxCount = 1
        i = 0
        while i < size:
            j = i + 1
            count = 1
            while j < size:
                if arr[i] == arr[j]:
                    count += 1
                j += 1
            if count > maxCount:
                maxval = arr[i]
                maxCount = count
            i += 1
        return maxval

    def getMax2(self, arr):
        size = len(arr)
        maximum = arr[0]
        maxCount = 1
        curr = arr[0]
        currCount = 1
        arr.sort()
        i = 0
        while i < size:
            if arr[i] == arr[i - 1]:
                currCount += 1
            else:
                currCount = 1
                curr = arr[i]
            if currCount > maxCount:
                maxCount = currCount
                maximum = curr
            i += 1
        return maximum

    def getMax3(self, arr, valuerange):
        size = len(arr)
        maximum = arr[0]
        maxCount = 1
        count = [0] * valuerange
        i = int()
        while i < size:
            count[arr[i]] += 1
            if count[arr[i]] > maxCount:
                maxCount = count[arr[i]]
                maximum = arr[i]
            i += 1
        return maximum

    @classmethod
    def main5(cls, args):
        first = [1, 5, 5, 13, 5, 31, 5]
        s = Searching()
        print s.getMajority(first)
        print s.getMajority2(first)
        print s.getMajority3(first)

    def getMajority(self, arr):
        size = len(arr)
        maximum = 0
        count = 0
        maxCount = 0
        i = 0
        while i < size:
            j = i + 1
            while j < size:
                if arr[i] == arr[j]:
                    count += 1
                j += 1
            if count > maxCount:
                maximum = arr[i]
                maxCount = count
            i += 1
        if maxCount > size / 2:
            return maximum
        else:
            return sys.maxint # can also raised exception.

    def getMajority2(self, arr):
        size = len(arr)
        majIndex = size / 2
        i = 0      
        arr.sort()
        candidate = arr[majIndex]
        count = 1
        while i < size:
            if arr[i] == candidate:
                count += 1
            i += 1
        if count > size / 2:
            return arr[majIndex]
        else:
            return sys.maxint # can also raised exception.

    def getMajority3(self, arr):
        size = len(arr)
        majIndex = 0
        count = 1
        i = 1
        while i < size:
            if arr[majIndex] == arr[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                majIndex = i
                count = 1
            i += 1
        candidate = arr[majIndex]
        count = 0
        i = 0
        while i < size:
            if arr[i] == candidate:
                count += 1
            i += 1
        if count > size / 2:
            return arr[majIndex]
        else:
            return sys.maxint  # can also raised exception.

    @classmethod
    def main6(cls, args):
        first = [1, 5, 4, 3, 2, 7, 8, 9, 10]
        s = Searching()
        # print s.findMissingNumber(first, 9)
        print s.findMissingNumber3(first, 9)
            
    def findMissingNumber(self, arr, upperRange):
        size = len(arr)
        i = 1
        found = 0
        while i <= upperRange:
            found = 0
            j = 0
            while j < size:
                if arr[j] == i:
                    found = 1
                    break
                j += 1
            if found == 0:
                return i
            i += 1
        return sys.maxint

    def findMissingNumber2(self, arr, upperRange):
        size = len(arr)
        i = 1
        xorSum = 0
        while i <= upperRange:
            xorSum ^= i
            i += 1
        i = 0
        while i < size:
            xorSum ^= arr[i]
            i += 1
        return xorSum

    def findMissingNumber3(self, arr, upperRange):
        size = len(arr)
        mSet = set()
        i = 0
        while i < size:
            mSet.add(arr[i])
            i += 1
        i = 1
        while i <= upperRange:
            if (i in mSet) == False:
                return i
            i += 1
        return sys.maxint



    @classmethod
    def main7(cls, args):
        first = [1, 5, 4, 3, 2, 7, 8, 9, 6]
        s = Searching()
        print s.FindPair(first, 8)
        print s.FindPair2(first, 8)
        print s.FindPair3(first, 8)
            

    def FindPair(self, arr, value):
        size = len(arr)
        i = 0
        while i < size:
            j = i + 1
            while j < size:
                if (arr[i] + arr[j]) == value:
                    print "The pair is::", arr[i], "&" , arr[j]
                    return True
                j += 1
            i += 1
        return False

    def FindPair2(self, arr, value):
        size = len(arr)
        first = 0
        second = size - 1
        arr.sort()
        while first < second:
            curr = arr[first] + arr[second]
            if curr == value:
                print "The pair is::", arr[first], "&", arr[second]
                return True
            elif curr < value:
                first += 1
            else:
                second -= 1
        return False

    def FindPair3(self, arr, value):
        size = len(arr)
        hs = set()
        i = int()
        while i < size:
            if (value - arr[i]) in hs:
                print "The pair is::", arr[i] , "&" , (value - arr[i])
                return True
            hs.add(arr[i])
            i += 1
        return False


    @classmethod
    def main8(cls, args):
        first = [1, 5, -10, 3, 2, -6, 8, 9, 6]
        s = Searching()
        print s.minabsSumPair2(first)
        print s.minabsSumPair(first)
        # print s.minabsSumPair(first)

    def minabsSumPair(self, arr):
        size = len(arr)
        if size < 2:
            print "Invalid Input"
            return
        minFirst = 0
        minSecond = 1
        i = 0
        minSum = abs(arr[0] + arr[1])
        while i < size - 1:
            j = i + 1
            while j < size:
                currsum = abs(arr[i] + arr[j])
                if currsum < minSum:
                    minSum = currsum
                    minFirst = i
                    minSecond = j
                j += 1
            i += 1
        print " The two elements with minimum sum are : ", arr[minFirst], "&", arr[minSecond]

    def minabsSumPair2(self, arr):
        size = len(arr)
        if size < 2:
            print "Invalid Input"
            return
        arr.sort()
        minFirst = 0
        minSecond = size - 1
        minSum = abs(arr[minFirst] + arr[minSecond])        
        l = 0
        r = size - 1
        while l < r:
            currsum = (arr[l] + arr[r])
            if abs(currsum) < minSum:
                minSum = currsum
                minFirst = l
                minSecond = r
            if currsum < 0:
                l += 1
            elif currsum > 0:
                r -= 1
            else:
                break
        print " The two elements with minimum sum are : ", arr[minFirst], "&" , arr[minSecond]


    @classmethod
    def main9(cls, args):
        first = [1, 5, 10, 13, 20, 30, 8, 7, 6]
        s = Searching()
        print s.SearchBotinicArrayMax(first)
        print s.SearchBitonicArray(first, 32)
        # print s.minabsSumPair(first)

    def SearchBotinicArrayMax(self, arr):
        size = len(arr)
        start = 0
        end = size - 1
        mid = (start + end) / 2
        maximaFound = 0
        if size < 3:
            print "error"
            return 0
        while start <= end:
            mid = (start + end) / 2
            if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
                maximaFound = 1
                break
            elif arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
                start = mid + 1
            elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]:
                end = mid - 1
            else:
                break
        if maximaFound == 0:
            print "error"
            return sys.maxint
        return arr[mid]

    def SearchBitonicArray(self, arr, key):
        size = len(arr)
        maxval = self.FindMaxBitonicIndex(arr, size)
        k = self.BinarySearch(arr, 0, maxval, key, True)
        if k == True:
            return True
        else:
            return self.BinarySearch(arr, maxval + 1, size - 1, key, False)

    def FindMaxBitonicIndex(self, arr, size):
        start = 0
        end = size - 1
        if size < 3:
            print "error"
            return -1
        while start <= end:
            mid = (start + end) / 2
            if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
                return mid
            elif arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
                start = mid + 1
            elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]:
                end = mid - 1
            else:
                break
        print "error"
        return -1

    def BinarySearch(self, arr, start, end, key, isInc):
        if end < start:
            return False
        mid = (start + end) / 2
        if key == arr[mid]:
            return True
        if isInc != False and key < arr[mid] or isInc == False and key > arr[mid]:
            return self.BinarySearch(arr, start, mid - 1, key, isInc)
        else:
            return self.BinarySearch(arr, mid + 1, end, key, isInc)

    @classmethod
    def main10(cls, args):
        first = [1, 5, 10, 13, 20, 30, 8, 7, 6]
        s = Searching()
        print s.findKeyCount(first, 6)
        print s.findKeyCount2(first, 6)
        # print s.minabsSumPair(first)

    def findKeyCount(self, arr, key):
        size = len(arr)
        i = 0
        count = 0
        while i < size:
            if arr[i] == key:
                count += 1
            i += 1
        return count

    def findKeyCount2(self, arr, key):
        size = len(arr)
        firstIndex = self.findFirstIndex(arr, 0, size - 1, key)
        lastIndex = self.findLastIndex(arr, 0, size - 1, key)
        return (lastIndex - firstIndex + 1)

    @classmethod
    def main11(cls, args):
        first = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
        s = Searching()
        print s.findKeyCount(first, 6)
        print s.findKeyCount2(first, 6)
        # print s.minabsSumPair(first)

    def findFirstIndex(self, arr, start, end, key):
        if end < start:
            return -1
        mid = (start + end) / 2
        if key == arr[mid] and (mid == start or arr[mid - 1] != key):
            return mid
        if key <= arr[mid]:
            return self.findFirstIndex(arr, start, mid - 1, key)
        else:
            return self.findFirstIndex(arr, mid + 1, end, key)

    def findLastIndex(self, arr, start, end, key):
        if end < start:
            return -1
        mid = (start + end) / 2
        if key == arr[mid] and (mid == end or arr[mid + 1] != key):
            return mid
        if key < arr[mid]:
            return self.findLastIndex(arr, start, mid - 1, key)
        else:
            return self.findLastIndex(arr, mid + 1, end, key)

    @classmethod
    def main12(cls, args):
        first = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
        s = Searching()
        print s.seperateEvenAndOdd(first)
        # print s.findKeyCount2(first, 6)
        # print s.minabsSumPair(first)


    def swap(self, arr, first, second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp

    def seperateEvenAndOdd(self, arr):
        size = len(arr)
        left = 0
        right = size - 1
        while left < right:
            if arr[left] % 2 == 0:
                left += 1
            elif arr[right] % 2 == 1:
                right -= 1
            else:
                self.swap(arr, left, right)
                left += 1
                right -= 1
        return arr

    @classmethod
    def main(cls, args):
        first = [10, 150, 6, 67, 61, 16, 86, 6, 67, 78, 150, -3, 28, 143 ]
        s = Searching()
        print s.maxProfit(first)
        # print s.findKeyCount2(first, 6)
        # print s.minabsSumPair(first)

    def maxProfit(self, stocks):
        size = len(stocks)
        buy = 0
        sell = 0
        curMin = 0
        currProfit = 0
        maxProfit = 0
        i = 0
        while i < size:
            if stocks[i] < stocks[curMin]:
                curMin = i
            currProfit = stocks[i] - stocks[curMin]
            if currProfit > maxProfit:
                buy = curMin
                sell = i
                maxProfit = currProfit
            i += 1
        print "Purchase day is - ", buy , " at price " , stocks[buy]
        print "Sell day is - " , sell , " at price " , stocks[sell]

    @classmethod
    def main14(cls, args):
        # first = [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]
        first = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
        second = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
        s = Searching()
        print s.findMedian(first, second)
        # print s.findKeyCount2(first, 6)
        # print s.minabsSumPair(first)

    def getMedian(self, arr):
        size = len(arr)
        arr.sort()
        return arr[size / 2]

    def findMedian(self, arrFirst, arrSecond):
        sizeFirst = len(arrFirst)
        sizeSecond = len(arrSecond)
        medianIndex = ((sizeFirst + sizeSecond) + (sizeFirst + sizeSecond) % 2) / 2
        i = 0
        j = 0
        count = 0
        while count < medianIndex - 1:
            if i < sizeFirst - 1 and arrFirst[i] < arrSecond[j]:
                i += 1
            else:
                j += 1
            count += 1
        if arrFirst[i] < arrSecond[j]:
            return arrFirst[i]
        else:
            return arrSecond[j]

    @classmethod
    def min(cls, a, b):
        return b if a > b else a

    @classmethod
    def max(cls, a, b):
        return b if a < b else a

    @classmethod
    def main15(cls, args):
        # first = [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]
        # first = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]
        # second = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]
        first = "000000001111"
        s = Searching()
        print s.BinarySearch01(first)
        # print s.findKeyCount2(first, 6)
        # print s.minabsSumPair(first)

    def BinarySearch01(self, arr):
        size = len(arr)
        if size == 1 and arr[0] == '1':
            return 0
        return self.BinarySearch01Util(arr, 0, size - 1)

    def BinarySearch01Util(self, arr, start, end):
        if end < start:
            return -1
        mid = (start + end) / 2
        if '1' == arr[mid] and '0' == arr[mid - 1]:
            return mid
        if '0' == arr[mid]:
            return self.BinarySearch01Util(arr, mid + 1, end)
        else:
            return self.BinarySearch01Util(arr, start, mid - 1)

    @classmethod
    def main16(cls, args):
        # first = [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]
        #
        first = [34, 56, 77, 1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
        # second = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]
        
        s = Searching()
        print s.BinarySearchRotateArray(first, 20)
        # print s.findKeyCount2(first, 6)
        # print s.minabsSumPair(first)

    def BinarySearchRotateArray(self, arr, key):
        size = len(arr)
        return self.BinarySearchRotateArrayUtil(arr, 0, size - 1, key)
 
    def BinarySearchRotateArrayUtil(self, arr, start, end, key):
        if end < start:
            return False
        mid = (start + end) / 2
        if key == arr[mid]:
            return True
        if arr[mid] > arr[start]:
            if arr[start] <= key and key < arr[mid]:
                return self.BinarySearchRotateArrayUtil(arr, start, mid - 1, key)
            else:
                return self.BinarySearchRotateArrayUtil(arr, mid + 1, end, key)
        else:
            if arr[mid] < key and key <= arr[end]:
                return self.BinarySearchRotateArrayUtil(arr, mid + 1, end, key)
            else:
                return self.BinarySearchRotateArrayUtil(arr, start, mid - 1, key)

    
    @classmethod
    def main17(cls, args):
        # first = [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]
        #
        first = [34, 56, 77, 1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 34, 20, 30 ]
        # second = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]    
        s = Searching()
        print s.FirstRepeated(first)
        # print s.findKeyCount2(first, 6)
        # print s.minabsSumPair(first)

    def FirstRepeated(self, arr):
        size = len(arr)
        i = 0
        while i < size:
            j = i + 1
            while j < size:
                if arr[i] == arr[j]:
                    return arr[i]
                j += 1
            i += 1
        return sys.maxint  # can raise exception.

    @classmethod
    def main18(cls, args):
        
        
        # [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]
        #
        # first = [34, 56, 77, 1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 34, 20, 30 ]
        # second = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]    
        s = Searching()
        print s.transformArrayAB1("aaaabbbb")

    def transformArrayAB1(self, strval):
        arr = list(strval)
        size = len(arr)
        N = size / 2
        i = 1
        while i < N:
            j = 0
            while j < i:
                self.swap(arr, N - i + 2 * j, N - i + 2 * j + 1)
                j += 1
            i += 1
        return "".join(arr)

    @classmethod
    def main19(cls, args):
        s = Searching()
        print s.checkPermutation2("aaaabbbb", "bbaaaabb")

    def checkPermutation(self, str1, str2):
        array1 = list(str1)
        array2 = list(str2)
        
        size1 = len(array1)
        size2 = len(array2)
        if size1 != size2:
            return False
        array1.sort()
        array2.sort()
        i = 0
        while i < size1:
            if array1[i] != array2[i]:
                return False
            i += 1
        return True

    def checkPermutation2(self, array1, array2):
        size1 = len(array1)
        size2 = len(array2)        
        if size1 != size2:
            return False
        al = []
        i = 0
        while i < size1:
            al.append(array1[i])
            i += 1
        i = 0
        while i < size2:
            if al.count(array2[i]) == 0:
                return False
            al.remove(array2[i])
            i += 1
        return True

    @classmethod
    def main20(cls, args):
        s = Searching()
        first = [1, 7, 6, 4, 8, 3, 8, 2, 6, 9]
        print s.removeDuplicates(first)

    def removeDuplicates(self, array):
        size = len(array)
        j = 0
        i = int()
        if size == 0:
            return 0
        array.sort()
        while i < size:
            if array[i] != array[j]:
                j += 1
                array[j] = array[i]
            i += 1
        array[j:size - 1] = []
        return array

    def FindElementIn2DArray(self, arr, r, c, value):
        row = 0
        column = c - 1
        while row < r and column >= 0:
            if arr[row][column] == value:
                return True
            elif arr[row][column] > value:
                column -= 1
            else:
                row += 1
        return False


if __name__ == '__main__':
    import sys
    Searching.main(sys.argv)


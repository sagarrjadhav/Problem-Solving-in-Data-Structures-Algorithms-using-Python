#!/usr/bin/env python
""" Source for module Introduction """
from ctypes.test.test_simplesubclasses import MyInt
class Introduction(object):
    """ Source for class Introduction """
    
    @classmethod
    def main(cls, args):
        i = 1
        cls.increment(i)
        print i
        var = MyInt()
        var.value = 1
        cls.increment2(var)
        print var.value
    
    @classmethod
    def increment(cls, var):
        var += 1

    class MyInt(object):
        value = 0

    @classmethod
    def increment2(cls, value):
        value.value += 1

    @classmethod
    def swap(cls, arr, x, y):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp


    @classmethod
    def permutation(cls, arr, i, length):
        if length == i:
            print arr
            return
        j = i
        while j < length:
            cls.swap(arr, i, j)
            cls.permutation(arr, i + 1, length)
            cls.swap(arr, i, j)
            j += 1



    @classmethod
    def main4444(cls, args):
        arr = [None] * 5
        i = 0
        while i < 5:
            arr[i] = i
            i += 1
        cls.permutation(arr, 0, 5)

    @classmethod
    def GCD(cls, m, n):
        if m < n:
            return (cls.GCD(n, m))
        if m % n == 0:
            return (n)
        return (cls.GCD(n, m % n))

    @classmethod
    def main555(cls, args):
        print cls.GCD(5, 2)

    @classmethod
    def towerOfHanoi(cls, num, src, dst, temp):
        """ Source for method towerOfHanoi """
        if num < 1:
            return
        cls.towerOfHanoi(num - 1, src, temp, dst)
        print "Move " , num , " disk  from peg " , src , " to peg " , dst
        cls.towerOfHanoi(num - 1, temp, dst, src)

    @classmethod
    def main1111(cls, args):
        num = 4
        print "The sequence of moves involved in the Tower of Hanoi are :"
        cls.towerOfHanoi(num, 'A', 'C', 'B')

    @classmethod
    def function2(cls):
        print "fun2 line 1"

    @classmethod
    def function1(cls):
        print "fun1 line 1"
        cls.function2()
        print "fun1 line 2"

    @classmethod
    def main96(cls, args):
        print "main line 1"
        cls.function1()
        print "main line 2"

    @classmethod
    def maxSubArraySum(cls, arr):
        size = len(arr)
        maxSoFar = 0
        maxEndingHere = 0
        i = 0
        while i < size:
            maxEndingHere = maxEndingHere + arr[i]
            if maxEndingHere < 0:
                maxEndingHere = 0
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
            i += 1
        return maxSoFar


    @classmethod
    def main975(cls, args):
        arr = [1, -2, 3, 4, -4, 6, -4, 8, 2]
        print cls.maxSubArraySum(arr)

    

    @classmethod
    def variableExample(cls):
        var1 = 100
        var2 = 200
        var3 = var1 + var2
        print "Adding" , var1 , "and" , var2 , "will give" , var3

    @classmethod
    def arrayExample(cls):
        arr = [0] * 10
        i = 0
        while i < 10:
            arr[i] = i
            i += 1
        return arr
        cls.printArray1(arr, 10)

    @classmethod
    def printArray1(cls, arr):
        count = len(arr)
        i = 0
        while i < count:
            print arr[i],
            i += 1

    @classmethod
    def main100(cls, args):
        cls.twoDArrayExample()


    @classmethod
    def twoDArrayExample(cls):
        first = 4
        second = 4
        arr = [[0 for x in range(first)] for y in range(second) ]      
        count = 0
        i = 0
        while i < first:
            j = 0
            while j < second:
                arr[i][j] = count
                count += 1
                j += 1
            i += 1
        cls.print2DArray(arr, first, second)

    @classmethod
    def print2DArray(cls, arr, row, col):
        i = 0
        while i < row:
            j = 0
            while j < col:
                print arr[i][j],
                j += 1
            i += 1

    @classmethod
    def main99(cls, args):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print cls.SumArray(arr)


    @classmethod
    def SumArray(cls, arr):
        size = len(arr)
        total = 0
        index = 0
        while index < size:
            total = total + arr[index]
            index += 1
        return total

    @classmethod
    def SequentialSearch(cls, arr, value):
        size = len(arr)
        i = 0
        while i < size:
            if value == arr[i]:
                return True
            i += 1
        return False

    @classmethod
    def BinarySearch(cls, arr, value):
        size = len(arr)
        low = 0
        high = size - 1
        while low <= high:
            mid = low + (high - low) / 2
            if arr[mid] == value:
                return True
            else:
                if arr[mid] < value:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

    @classmethod
    def main98(cls, args):

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print cls.BinarySearch(arr, 6)


    @classmethod
    def rotateArray(cls, arr, k):
 
        n = len(arr)
        cls.reverseArray(arr, 0, k - 1)
        cls.reverseArray(arr, k, n - 1)
        cls.reverseArray(arr, 0, n - 1)

    @classmethod
    def reverseArray(cls, arr, start, end):
        i = start
        j = end
        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1

    @classmethod
    def reverseArray_0(cls, a):
        start = 0
        end = len(a)
        i = start
        j = end
        while i < j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i += 1
            j -= 1
    
    @classmethod
    def main97(cls, args):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cls.rotateArray(arr, 3)
        print arr

    
    
    class coord(object):
        x = int()
        y = int()

    def main2(self):
        point = self.coord()
        point.x = 10
        point.y = 10
        print "X axis coord value is  " + point.x
        print "Y axis coord value is  " + point.y


    class student(object):
        rollNo = int()
        firstName = str()
        lastName = str()

    def main3(self):
        stud = self.student()
        refStud = stud
        refStud.rollNo = 1
        refStud.firstName = "john"
        refStud.lastName = "smith"
        print "Roll No:   Student Name:  " + refStud.rollNo + refStud.firstName + refStud.lastName


    def main4(self):
        x = 10
        y = 20
        result = sum(x, y)
        print "Sum is : " + result


    def sum(self, num1, num2):
        result = num1 + num2
        return result

    @classmethod
    def factorial(cls, i):
        if i <= 1:
            return 1
        return i * cls.factorial(i - 1)

    @classmethod
    def main95(cls, args):
        print cls.factorial(5)


    @classmethod
    def printInt(cls, number):
        conversion = "0123456789"
        digit = number % 10
        number = number / 10
        temp = ""
        if number != 0:
            temp += cls.printInt(number)
        temp += conversion[digit]
        return temp

    @classmethod
    def main3232(cls, args):
        print cls.printInt2(50, 2)
        
    @classmethod
    def printInt2(cls, number, base):
        conversion = "0123456789ABCDEF"
        digit = number % base
        number = number / base
        temp = ""
        if number != 0:
            temp += cls.printInt2(number, base)
        temp += conversion[digit]
        return temp

    @classmethod
    def fibonacci(cls, n):
        if n <= 1:
            return n
        return cls.fibonacci(n - 1) + cls.fibonacci(n - 2)

    @classmethod
    def main7777(cls, args):
        print cls.fibonacci(6)

    @classmethod
    def BinarySearchRecursive(cls, arr, low, high, value):
        mid = low + (high - low) / 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            return cls.BinarySearchRecursive(arr, mid + 1, high, value)
        else:
            return cls.BinarySearchRecursive(arr, low, mid - 1, value)


    @classmethod
    def main3213(cls, args):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print cls.BinarySearch(arr, 6)
        print cls.BinarySearch(arr, 16)

        
if __name__ == '__main__':
    import sys
    Introduction.main(sys.argv)


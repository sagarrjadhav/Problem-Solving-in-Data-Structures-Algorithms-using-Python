#!/usr/bin/env python
class BubbleSort(object):
    def __init__(self, array):
        self.arr = array
        self.sort2()

    def less(self, value1, value2):
        return value1 < value2

    def more(self, value1, value2):
        return value1 > value2

    def sort(self):
        size = len(self.arr)
        i = 0
        while i < (size - 1):
            j = 0
            while j < size - i - 1:
                if self.more(self.arr[j], self.arr[j + 1]):
                    #  Swapping 
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j + 1]
                    self.arr[j + 1] = temp
                j += 1
            i += 1

    def sort2(self):
        size = len(self.arr)
        swapped = 1
        i = 0
        while i < (size - 1) and swapped == 1:
            swapped = 0
            j = 0
            while j < size - i - 1:
                if self.more(self.arr[j], self.arr[j + 1]):
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j + 1]
                    self.arr[j + 1] = temp
                    swapped = 1
                j += 1
            i += 1

class BubbleSortDemo:
    @classmethod
    def main(cls, args):
        array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
        BubbleSort(array)
        print array

if __name__ == '__main__':
    import sys
    BubbleSortDemo.main(sys.argv)
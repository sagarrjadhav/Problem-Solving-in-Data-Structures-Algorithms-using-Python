#!/usr/bin/env python
""" generated source for module InsertionSort """

class InsertionSort(object):
    def __init__(self, array):
        self.arr = array
        self.sort()

    def more(self, value1, value2):
        return value1 > value2

    def sort(self):
        size = len(self.arr)
        i = 1
        while i < size:
            temp = self.arr[i]
            j = i;
            while j > 0 and self.more(self.arr[j - 1], temp):
                self.arr[j] = self.arr[j - 1]
                j -= 1
            self.arr[j] = temp
            i += 1

class InsertionSortDemo(object):
    @classmethod
    def main(cls, args):
        array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
        InsertionSort(array)
        print array


if __name__ == '__main__':
    import sys
    InsertionSortDemo.main(sys.argv)

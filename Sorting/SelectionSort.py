#!/usr/bin/env python
class SelectionSort(object):
    def __init__(self, array):
        self.arr = array
        self.sort()

    def sort(self):
        # back array
        size = len(self.arr)
        i = 0
        while i < size - 1:
            maxIndex = 0
            j = 1
            while j < size - 1 - i:
                if self.arr[j] > self.arr[maxIndex]:
                    maxIndex = j
                j += 1
            temp = self.arr[size - 1 - i]
            self.arr[size - 1 - i] = self.arr[maxIndex]
            self.arr[maxIndex] = temp
            i += 1

    def sort2(self):
        # front array
        size = len(self.arr)
        i = 0
        while i < size - 1:
            minIndex = i
            j = i + 1
            while j < size:
                if self.arr[j] < self.arr[minIndex]:
                    minIndex = j
                j += 1
            temp = self.arr[i]
            self.arr[i] = self.arr[minIndex]
            self.arr[minIndex] = temp
            i += 1

class SelectionSortDemo(object):
    @classmethod
    def main(cls, args):
        array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
        SelectionSort(array)
        print array
       
if __name__ == '__main__':
    import sys
    SelectionSortDemo.main(sys.argv)


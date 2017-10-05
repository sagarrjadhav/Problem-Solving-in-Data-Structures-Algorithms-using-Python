#!/usr/bin/env python
class QuickSort(object):
    def __init__(self, array):
        self.arr = array
        size = len(self.arr)
        self.Sort(self.arr, 0, size - 1)

    def Sort(self, arr, lower, upper):
        if upper <= lower:
            return
        pivot = arr[lower]
        start = lower
        stop = upper
        while lower < upper:
            while arr[lower] <= pivot and lower < upper:
                lower += 1
            while arr[upper] > pivot and lower <= upper:
                upper -= 1
            if lower < upper:
                self.swap(arr, upper, lower)
        self.swap(arr, upper, start)
        # upper is the pivot position
        self.Sort(arr, start, upper - 1)
        # pivot -1 is the upper for left sub array.
        self.Sort(arr, upper + 1, stop)
        #  pivot + 1 is the lower for right sub array.
        
    def swap(self, arr, first, second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp

class QuickSortDemo(object):
    @classmethod
    def main(cls, args):
        array = [3, 4, 2, 1, 6, 5, 7, 8, 1, 1]
        QuickSort(array)
        print array

if __name__ == '__main__':
    import sys
    QuickSortDemo.main(sys.argv)


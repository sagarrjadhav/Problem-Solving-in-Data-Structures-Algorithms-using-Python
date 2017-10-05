#!/usr/bin/env python
class QuickSelect(object):
    def Select(self, array, k):
        self.arr = array
        size = len(self.arr)
        self.SelectUtil(self.arr, 0, size-1, k)
        return self.arr[k-1]

    def SelectUtil(self, arr, lower, upper, k):
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
        self.swap(arr, upper, start)    # upper is the pivot position
        
        if k < upper: 
            # pivot -1 is the upper for left sub array.
            self.SelectUtil(arr, start, upper - 1, k)
        
        if k > upper:
            #  pivot + 1 is the lower for right sub array.
            self.SelectUtil(arr, upper + 1, stop, k)   
              
    def swap(self, arr, first, second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp
        
        
class QuickSelectDemo(object):
    @classmethod
    def main(cls, args):
        array = [3, 4, 2, 1, 6, 5, 7, 8, 10, 9]
        value = QuickSelect().Select(array, 5)
        print "value at index 5 is : " , value,

if __name__ == '__main__':
    import sys
    QuickSelectDemo.main(sys.argv)
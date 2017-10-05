#!/usr/bin/env python
class BucketSort(object):
    def __init__(self, arr, lowerRange, upperRange):
        self.array = arr
        self.range = upperRange - lowerRange
        self.lowerRange = lowerRange
        size = len(self.array)
        count = [0] * self.range
        i = 0
        while i < size:
            count[self.array[i] - self.lowerRange] += 1
            i += 1
        
        j = 0
        i = 0
        while i < self.range:
            while count[i] > 0:
                self.array[j] = i + self.lowerRange
                count[i] -= 1
                j += 1
            i += 1
                

class BucketSortDemo(object):
    @classmethod
    def main(cls, args):
        array = [23, 24, 22, 21, 26, 25, 27, 28, 21, 21]
        BucketSort(array, 20, 30)
        print array

if __name__ == '__main__':
    import sys
    BucketSortDemo.main(sys.argv)
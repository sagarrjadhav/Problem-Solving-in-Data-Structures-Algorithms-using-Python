#!/usr/bin/env python

class MergeSort(object):
    def __init__(self, array):
        self.arr = array
        size = len(self.arr)
        tempArray = [0] * size
        self.mergeSrt(self.arr, tempArray, 0, size - 1)
        
    def mergeSrt(self, arr, tempArray, lowerIndex, upperIndex):
        if lowerIndex >= upperIndex:
            return
        middleIndex = (lowerIndex + upperIndex) / 2
        self.mergeSrt(arr, tempArray, lowerIndex, middleIndex)
        self.mergeSrt(arr, tempArray, middleIndex + 1, upperIndex)
        self.merge(arr, tempArray, lowerIndex, middleIndex, upperIndex)
    
    def merge(self, arr, tempArray, lowerIndex, middleIndex, upperIndex):
        lowerStart = lowerIndex
        lowerStop = middleIndex
        upperStart = middleIndex + 1
        upperStop = upperIndex
        count = lowerIndex
        
        while lowerStart <= lowerStop and upperStart <= upperStop:
            if arr[lowerStart] < arr[upperStart]:
                tempArray[count] = arr[lowerStart]
                count += 1
                lowerStart += 1
            else:
                tempArray[count] = arr[upperStart]
                count += 1
                upperStart += 1
                
        while lowerStart <= lowerStop:
            tempArray[count] = arr[lowerStart]
            count += 1
            lowerStart += 1
            
        while upperStart <= upperStop:
            tempArray[count] = arr[upperStart]
            count += 1
            upperStart += 1
        
        i = lowerIndex
        while i <= upperIndex:
            arr[i] = tempArray[i]
            i += 1


class MergeSortDemo(object):
    @classmethod
    def main(cls, args):
        array = [3, 4, 2, 1, 6, 5, 7, 8, 1, 1]
        MergeSort(array)
        print array

if __name__ == '__main__':
    import sys
    MergeSortDemo.main(sys.argv)

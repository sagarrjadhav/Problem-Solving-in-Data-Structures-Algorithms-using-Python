#!/usr/bin/env python
from collections import Counter

class HashTableExercise(object):
    @classmethod
    def main(cls, args):
        first = "hello"
        second = "elloh"
        third = "world"
        print "isAnagram : " , cls.isAnagram(first, second)
        print "isAnagram : " , cls.isAnagram(first, third)
        print cls.removeDuplicate(first)
        print first
        arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]
        print cls.findMissing(arr, 1, 10)
        arr1 = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 1]
        cls.printRepeating(arr1)
        cls.printFirstRepeating(arr1)

    @classmethod
    def isAnagram(cls, str1, str2):
        size1 = len(str1)
        size2 = len(str2)
        if size1 != size2:
            return False
        cm = Counter()
        for ch in str1:
            cm[ch] += 1
        for ch in str2:
            if cm[ch] == 0:
                return False
            else:
                cm[ch] -= 1
        return True

    @classmethod
    def removeDuplicate(cls, exp):
        hs = set()
        retexp = ""
        for ch in exp:
            if (ch in hs) == False:
                retexp += ch
                hs.add(ch)
        return retexp

    @classmethod
    def findMissing(cls, arr, start, end):
        hs = set()
        for i in arr:
            hs.add(i)
        curr = start
        while curr <= end:
            if (curr in hs) == False:
                return curr
            curr += 1
        return sys.maxint

    @classmethod
    def printRepeating(cls, arr):
        hs = set()
        print "Repeating elements are:",
        for val in arr:
            if val in hs:
                print val,
            else:
                hs.add(val)

    @classmethod
    def printFirstRepeating(cls, arr):
        size = len(arr)
        i = 0
        hs = Counter()
        while i < size:
            hs[arr[i]] += 1
            i += 1
        i = 0
        while i < size:
            if hs.get(arr[i]) > 1:
                print "First Repeating number is : " , arr[i]
                return arr[i]
            i += 1

    def hornerHash(self, key, tableSize):
        size = len(key)
        h = 0
        i = 0
        while i < size:
            h = (32 * h + key[i]) % tableSize
            i += 1
        return h


if __name__ == '__main__':
    import sys
    HashTableExercise.main(sys.argv)

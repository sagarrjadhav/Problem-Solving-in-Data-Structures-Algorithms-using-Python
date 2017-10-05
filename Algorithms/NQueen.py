#!/usr/bin/env python

class NQueen(object):
    @classmethod
    def printArr(cls, Q, n):
        i = 0
        while i < n:
            print(Q[i])
            i += 1
        print("")

    @classmethod
    def Feasible(cls, Q, k):
        i = 0
        while i < k:
            if Q[k] == Q[i] or abs(Q[i] - Q[k]) == abs(i - k):
                return False
            i += 1
        return True

    @classmethod
    def NQueens(cls, Q, k, n):
        if k == n:
            cls.printArr(Q, n)
            return
        i = 0
        while i < n:
            Q[k] = i
            if cls.Feasible(Q, k):
                cls.NQueens(Q, k + 1, n)
            i += 1


    @classmethod
    def main(cls, args):
        Q = [0] * 8
        cls.NQueens(Q, 0, 8)
        
if __name__ == '__main__':
    import sys
    NQueen.main(sys.argv)

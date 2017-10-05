#!/usr/bin/env python

import math

class Analysis(object):

    def fun1(self, n):
        m = 0
        i = 0
        while i < n:
            m += 1
            i += 1
        return m

    def fun2(self, n):
        m = 0
        i = 0
        while i < n:
            j = 0
            while j < n:
                m += 1
                j += 1
            i += 1
        return m

    def fun3(self, n):
        m = 0
        i = 0
        while i < n:
            j = 0
            while j < i:
                m += 1
                j += 1
            i += 1
        return m

    def fun4(self, n):
        m = 0
        i = 1
        while i < n:
            m += 1
            i = i * 2
        return m

    def fun5(self, n):
        m = 0
        i = n
        while i > 0:
            m += 1
            i = i / 2
        return m

    def fun6(self, n):
        m = 0
        i = 0
        while i < n:
            j = 0
            while j < n:
                k = 0
                while k < n:
                    m += 1
                    k += 1
                j += 1
            i += 1
        return m

    def fun7(self, n):
        m = 0
        i = 0
        while i < n:
            j = 0
            while j < n:
                m += 1
                j += 1
            i += 1
        i = 0
        while i < n:
            k = 0
            while k < n:
                m += 1
                k += 1
            i += 1
        return m

    def fun8(self, n):
        m = 0
        i = 0
        while i < n:
            j = 0
            while j < math.sqrt(n):
                m += 1
                j += 1
            i += 1
        return m

    def fun9(self, n):
        m = 0
        i = n
        while i > 0:
            j = 0
            while j < i:
                m += 1
                j += 1
            i /= 2
        return m

    def fun10(self, n):
        m = 0
        i = 0
        while i < n:
            j = i
            while j > 0:
                m += 1
                j -= 1
            i += 1
        return m

    def fun11(self, n):
        m = 0
        i = 0
        while i < n:
            j = i
            while j < n:
                k = j + 1
                while k < n:
                    m += 1
                    k += 1
                j += 1
            i += 1
        return m

    def fun12(self, n):
        m = 0
        i = 0
        while i < n:
            j = 0
            while j < n:
                m += 1
                j += 1
            i += 1
        return m

    def fun13(self, n):
        m = 0
        i = 1
        while i <= n:
            j = 0
            while j <= i:
                m += 1
                j += 1
            i *= 2
        return m
    
    @classmethod
    def main(cls, args):
        analysis = Analysis()
        print "Value of M fun1():" , analysis.fun1(100)
        print "Value of M fun2():" , analysis.fun2(100)
        print "Value of M fun3():" , analysis.fun3(100)
        print "Value of M fun4():" , analysis.fun4(100)
        print "Value of M fun5():" , analysis.fun5(100)
        print "Value of M fun6():" , analysis.fun6(100)
        print "Value of M fun7():" , analysis.fun7(100)
        print "Value of M fun8():" , analysis.fun8(100)
        print "Value of M fun9():" , analysis.fun9(100)
        print "Value of M fun10():" , analysis.fun10(100)
        print "Value of M fun11():" , analysis.fun11(100)
        print "Value of M fun12():" , analysis.fun12(100)
        print "Value of M fun13():" , analysis.fun13(100)


if __name__ == '__main__':
    import sys
    Analysis.main(sys.argv)
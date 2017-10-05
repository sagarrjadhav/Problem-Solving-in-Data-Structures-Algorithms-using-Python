from collections import Set

class MyClass:
                 
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        a = set()
        a.add(5)
        a.add(5)
        a.add(4)
        a.add(2)
        a.add(5)
        print a
        print len(a)
        a.remove(4)
        print a
        a.add(8)
        print a.pop()
        print a
        print (5 in a)

if __name__ == '__main__':
    import sys
    MyClass.main(sys.argv)
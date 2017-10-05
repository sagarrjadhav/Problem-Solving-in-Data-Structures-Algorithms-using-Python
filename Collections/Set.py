class MyClass:
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        a = set()
        a.add(5)
        a.add(4)
        a.add(2)
        a.add(1)
        a.add(5)
        print a
        print (4 in a) 
        a.remove(4)
        print a    

if __name__ == '__main__':
    import sys
    MyClass.main(sys.argv)
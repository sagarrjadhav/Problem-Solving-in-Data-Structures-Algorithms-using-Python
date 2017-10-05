from collections import OrderedDict

class MyClass: 
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        a = {}
        a["apple"] = 40
        a["banana"] = 10
        a["mango"] = 20
        print a
        print a["mango"]
        print a.get("mango")
        print "apple" in a
        
        b = OrderedDict()
        b["apple"] = 40
        b["banana"] = 10
        b["mango"] = 20
        print b
        print b["mango"]
        print b.get("mango")
        print "banana" in b
        

if __name__ == '__main__':
    import sys
    MyClass.main(sys.argv)

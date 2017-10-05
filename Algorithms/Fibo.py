class Prime(object):  
    @classmethod
    def main(cls, args):
        print(cls.isPrime(50))
        print(cls.isPrime(47))
    
    @classmethod
    def isPrime(self, n):
        if( n > 1):
            answer = True
        else:
            answer = False
        i = 2
        while(i*i <= n):
            if(n%i == 0):
                answer = False
                break
            i += 1
        return answer     

if __name__ == '__main__':
    import sys
    Prime.main(sys.argv)
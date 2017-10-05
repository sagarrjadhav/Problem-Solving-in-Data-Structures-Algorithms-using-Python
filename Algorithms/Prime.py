class Fibo(object):
    
    @classmethod
    def main(cls, args):
        print(cls.fibonacci(50))
        print(cls.fibonacci2(50))

    @classmethod
    def fibonacci2(cls, n):
        if n <= 1:
            return n
        return cls.fibonacci(n - 1) + cls.fibonacci(n - 2)
    
    @classmethod
    def fibonacci(cls, n):
        first = 0
        second = 1
        if (n == 0):
            return first;
        elif (n == 1):
            return second;
        i = 2
        while(i <= n):
            temp = first + second
            first = second
            second = temp
            i += 1
        return temp
    
    def isPrime(self, n):
        if( n > 1):
            answer = True
        else:
            answer = False
        i = 2
        while(i*i <= n):
            if(n%i == 0):
                answer = True;
                break;
            i += 1
        return answer     

if __name__ == '__main__':
    import sys
    Fibo.main(sys.argv)
#!/usr/bin/env python

class Algo:
    @classmethod
    def isBalancedParenthesis(cls, expn):
        stk = []
        for ch in expn:
            if ch == '{' or ch == '[' or ch == '(':
                stk.append(ch)
            elif ch == '}':
                if stk.pop() != '{':
                    return False
            elif ch == ']':
                if stk.pop() != '[':
                    return False
            elif ch == ')':
                if stk.pop() != '(':
                    return False
        return len(stk) == 0


    @classmethod
    def main1(cls, args):
        expn = "{()}[]"
        value = Algo.isBalancedParenthesis(expn)
        print "Given Expn:" , expn
        print "Result after isParenthesisMatched:" , value

    @classmethod
    def insertAtBottom(cls, stk, value):  # !!!!!!!!! waste for python.
        if len(stk) == 0:
            stk.append(value)
        else:
            temp = stk.pop()
            cls.insertAtBottom(stk, value)
            stk.append(temp)

    @classmethod
    def reverseStack(cls, stk):  # !!!!!!!!! waste for python.
        if len(stk) == 0:
            return
        else:
            value = stk.pop
            cls.reverseStack(stk)
            cls.insertAtBottom(stk, value)

    @classmethod
    def postfixEvaluate(cls, expn):
        stk = []
        token_list = expn.split()

        for token in token_list:
            if token == '+':
                num1 = stk.pop();
                num2 = stk.pop();
                stk.append(num1 + num2)
            elif token == '-':
                num1 = stk.pop();
                num2 = stk.pop();
                stk.append(num1 - num2)
            elif token == '*':
                num1 = stk.pop();
                num2 = stk.pop();
                stk.append(num1 * num2)
            elif token == '/':
                num1 = stk.pop();
                num2 = stk.pop();
                stk.append(num1 / num2)
            else: 
                stk.append(int(token))
        return stk.pop()

    @classmethod
    def main2(cls, args):
        expn = "6 5 2 3 + 8 * + 3 + *"
        value = cls.postfixEvaluate(expn)
        print "Given Postfix Expn: " , expn
        print "Result after Evaluation: " , value

    @classmethod
    def precedence(cls, x):
        if x == '(':
            return (0)
        if x == '+' or x == '-':
            return (1)
        if x == '*' or x == '/' or x == '%':
            return (2)
        if x == '^':
            return (3)
        return (4)


    @classmethod
    def infixToPostfix(cls, expn):
        stk = []
        token_list = expn.split()
        output = ""
        for token in token_list:
            if token in '+-*/^':
                while len(stk) != 0 and cls.precedence(token) <= cls.precedence(stk[len(stk) - 1]):
                    outsrt = stk.pop()
                    output = output + " " + outsrt
                stk.append(token)
            elif token == '(':
                stk.append(token)
            elif token == ')':
                outsrt = None
                while len(stk) != 0 and outsrt != '(':
                    outsrt = stk.pop()
                    if outsrt != '(' :
                        output = output + " " + outsrt
            else :
                output = output + " " + token
            
        while len(stk) != 0:
            outsrt = stk.pop()
            output = output + " " + outsrt
        return output

    @classmethod
    def main5(cls, args):
        expn = "10 + ( ( 3 ) ) * 5 / ( 16 - 4 )"
        # value = cls.infixToPostfix(expn)
        value = cls.infixToPrefix(expn)
        print "Infix Expn: " , expn
        print "Postfix Expn: " , value

    @classmethod
    def infixToPrefix(cls, expn):
        expn = cls.reverseString(expn)
        expn = cls.replaceParanthesis(expn)
        expn = cls.infixToPostfix(expn)
        expn = cls.reverseString(expn)
        return expn

    @classmethod
    def replaceParanthesis(cls, expn):
        lower = 0
        upper = len(expn)
        newexp = ""
        while lower < upper:
            if expn[lower] == '(':
                newexp += ')'
            elif expn[lower] == ')':
                newexp += '('
            else:
                newexp += expn[lower]
            lower += 1
        return newexp

    @classmethod
    def reverseString(cls, expn):
        lower = 0
        upper = len(expn)
        newexp = ""
        while lower < upper:
            newexp += expn[upper - 1]
            upper -= 1
        return newexp

    @classmethod
    def main75(cls, args):
        expn = "10+((3))*5/(16-4)"
        value = cls.infixToPrefix(expn)
        print "Infix Expn: " , expn
        print "Prefix Expn: " , value

    @classmethod
    def StockSpanRange(cls, arr):
        SR = [0] * len(arr)
        SR[0] = 1
        i = 1
        size = len(arr)
        
        while i < size:
            SR[i] = 1
            j = i - 1
            while (j >= 0) and (arr[i] >= arr[j]):
                SR[i] += 1
                j -= 1
            i += 1
        return SR
    
    @classmethod
    def main54(cls, args):
        arr = [6, 5, 4, 3, 2, 4, 5, 7, 9]
        value = cls.StockSpanRange2(arr)
        print "StockSpanRange: " , value
 

 
    
    @classmethod
    def StockSpanRange2(self, arr):
        stk = []
        size = len(arr)
        SR = [0] * size
        stk.append(0)
        SR[0] = 1
        i = 1
        while i < size:
            while len(stk) != 0 and arr[stk[len(stk) - 1]] <= arr[i]:
                stk.pop()
            if (len(stk) == 0):
                SR[i] = i + 1  
            else:
                SR[i] = i - stk[len(stk) - 1]
            stk.append(i)
            i += 1
        return SR

    @classmethod
    def main(cls, args):
        arr = [7, 6, 5, 4, 4, 1, 6, 3, 1]
        value = cls.GetMaxArea2(arr)
        print "GetMaxArea: " , value

    @classmethod
    def GetMaxArea(cls, arr):
        size = len(arr)
        maxArea = -1
        minHeight = 0
        i = 1
        while i < size:
            minHeight = arr[i]
            j = i - 1
            while j >= 0:
                if minHeight > arr[j]:
                    minHeight = arr[j]
                currArea = minHeight * (i - j + 1)
                if maxArea < currArea:
                    maxArea = currArea
                j -= 1
            i += 1
        return maxArea

    @classmethod
    def GetMaxArea2(cls, arr):
        """ generated source for method GetMaxArea2 """
        size = len(arr)
        stk = []
        maxArea = 0
        i = 0
        while i < size:
            while (i < size) and (len(stk) == 0 or arr[stk[len(stk) - 1]] <= arr[i]):
                stk.append(i)
                i += 1
            while not len(stk) == 0 and (i == size or arr[stk[len(stk) - 1]] > arr[i]):
                top = stk[len(stk) - 1]
                stk.pop()
                topArea = arr[top] * (i if len(stk) == 0 else i - stk[len(stk) - 1] - 1)
                if maxArea < topArea:
                    maxArea = topArea
        return maxArea


if __name__ == '__main__':
    import sys
    Algo.main(sys.argv)

class Solution:
    def generateParenthesis(self,n: int, stack='',k=0):
        p = []
        if n == 0:
            return [stack+k*')']
        else:
            p += self.generateParenthesis(n-1,stack+'(',k+1)
            if k>0:
                p+=self.generateParenthesis(n, stack+')',k-1)
            return p
print(Solution.generateParenthesis(4))
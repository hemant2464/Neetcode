class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(ip,op):
            o,c=ip[0],ip[1]
            if o==0 and c==0:
                ans.append(op)
                return 
            else:
                if o>0 and o<c:
                    op1=op+'('
                    op2=op+')'
                    solve([o-1,c],op1)
                    solve([o,c-1],op2)
                elif o==c:
                    op+='('
                    solve([o-1,c],op)
                else:
                    op+=')'
                    solve([o,c-1],op)
        ans=[]
        solve([n,n],'')
        return ans
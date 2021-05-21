'''
给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。
有效的表达式需遵循以下约定：
"t"，运算结果为 True
"f"，运算结果为 False
"!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
"&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
"|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）
示例 1：
输入：expression = "!(f)"
输出：true
示例 2：
输入：expression = "|(f,t)"
输出：true
示例 3：
输入：expression = "&(t,f)"
输出：false
示例 4：
输入：expression = "|(&(t,f,t),!(t))"
输出：false
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/parsing-a-boolean-expression
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expression=expression.replace('t','True')
        expression=expression.replace('f','False')
        expression=expression.replace('!','notF')
        expression=expression.replace('&','andF')
        expression=expression.replace('|','orF')
        def notF(b):
            return not b
        def andF(*b): #*b 不定数量的参数
            result=True #当item为True的时候result才是True
            for item in b:
                result=result and item
            return result
        def orF(*b): 
            result=False #当item为True的时候result才是True
            for item in b:
                result=result or item
            return result
        return eval(expression)


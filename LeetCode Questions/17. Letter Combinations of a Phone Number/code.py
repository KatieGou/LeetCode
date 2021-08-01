from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        dic={'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8': 'tuv', '9':'wxyz'}
        combinations=list()
        for digit in digits:
            l=list(dic[digit])
            combinations.append(l)
        output=list()
        for i in product(*combinations):
            print(i)
            output.append(''.join(i))
        return output

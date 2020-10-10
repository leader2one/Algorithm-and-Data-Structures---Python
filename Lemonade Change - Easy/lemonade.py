class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        twenty = five = ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five >= 1:
                    ten += 1
                    five -= 1
                else :
                    return 0
            elif i == 20:
                twenty += 1
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else : 
                    return 0
        return 1    
from math import sqrt


class Solution:
    def isThree(self, n: int) -> bool:
        diviosrs = [1, n]
        for num in range(2, n):
            if n % num == 0:
                diviosrs += [num]
                if len(diviosrs) > 3:
                    return False
                else:
                    pass
            else:
                pass

        print(diviosrs)
        return True if len(diviosrs) == 3 else False


print(Solution().isThree(14))

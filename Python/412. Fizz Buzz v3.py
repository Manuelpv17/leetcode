# v3
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        dic = {3: "Fizz", 5: "Buzz"}
        for num in range(1, n + 1):
            fizzBuzz = ""
            for key in dic.keys():
                if num % key == 0:
                    fizzBuzz += dic[key]
            if fizzBuzz == "":
                fizzBuzz += str(num)
            result.append(fizzBuzz)
        return result

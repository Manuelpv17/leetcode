# v2
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for num in range(1, n + 1):
            fizzBuzz = ""
            if num % 3 == 0:
                fizzBuzz += "Fizz"
            if num % 5 == 0:
                fizzBuzz += "Buzz"
            if fizzBuzz == "":
                fizzBuzz += str(num)
            result.append(fizzBuzz)
        return result

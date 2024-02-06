class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        index = 0
        len_nums = len(nums)
        if nums[0] >= 0:
            index = 0
        elif nums[len_nums - 1] < 0:
            index = len_nums - 1
        else:
            for i in range(1, len_nums):
                if nums[i - 1] < 0 and nums[i] >= 0:
                    index = i
        left = index - 1
        right = index
        while True:
            if left >= 0 and ( right >= len_nums or -nums[left] < nums[right]):
                result.append(nums[left] ** 2)
                left -= 1
            elif right < len_nums:
                result.append(nums[right] ** 2)
                right += 1
            else:
                break
                
        return result
                
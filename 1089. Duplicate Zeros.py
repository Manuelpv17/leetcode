# Space O(n) - Time O(n)

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        copy = arr.copy()
        i_arr = 0
        i_copy = 0
        while i_arr < len(arr):
            if copy[i_copy] == 0:
                arr[i_arr] = 0
                if i_arr < len(arr) - 1:
                    arr[i_arr + 1] =  0
                i_arr += 2
            else:
                arr[i_arr] = copy[i_copy]
                i_arr += 1
            i_copy += 1

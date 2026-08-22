class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        tmp_n = 0
        for i in range(len(arr) - 1,-1,-1):
            tmp_n = arr[i]
            arr[i] = curr_max
            if tmp_n > curr_max:
                curr_max = tmp_n

            i -= 1
        return arr


        
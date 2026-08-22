class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        run_max = -1
        hold = -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] > run_max:
                hold = arr[i]
                arr[i] = run_max
                run_max = hold
            else:
                arr[i] = hold
        return arr

        
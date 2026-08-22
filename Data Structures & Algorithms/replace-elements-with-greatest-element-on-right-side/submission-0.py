class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        bar = max(arr)
        for i in range(len(arr)-1):
            if arr[i] >= bar:
                bar = max(arr[i+1:])
            arr[i] = bar
        arr[-1] = -1
        return arr


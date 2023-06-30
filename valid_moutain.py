class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        #check if the array is at least 3 elements if not return false
        #set increasing to true
        #from the start to the end of the array
            #if we are increasing and the current one is greater than the next
                #return false
            #if we are decreasing and we increase
                #return false
            #if we decrease
                #set increase to false

        l = len(arr)
        if l < 3 or arr[0] > arr[1]:
            return False
        inc = True
        for i in range(l -1):
            if arr[i] >= arr[i + 1]:
                inc = False
            if (not inc) and arr[i] <= arr[i + 1]:
                return False

        return  not inc

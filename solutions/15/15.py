class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the list
        nums.sort()
        # Initialize the result array
        result = []
        # Iterate the list with i
        for i in range(len(nums)):
            # If the number is larger than 0, we can break
            # since the remaining numbers are all positive.
            if nums[i] > 0:
                break
            # If the current number is equal to the previous, skip it.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Initialize the pointer j and k to the next element of i and
            # the last element, respectively.
            j = i + 1
            k = len(nums) - 1
            while j < k:
                # If the sums of the elements of the indices i, j, and k is
                # equal to 0, add the triplet into result
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    # Increament j and decrement k
                    j += 1
                    k -= 1
                    # Skip duplicated element at indices j and k
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                # If the sum is less than 0, increment j.
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                # If the sum is greater than 0, decrement k.
                else:
                    k -= 1
            # Return the result list
        return result

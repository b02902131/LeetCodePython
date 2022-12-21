public class Solution
{
    public int[] RunningSum(int[] nums)
    {
        // try-1
        // int[] outputNums = new int [nums.Length];
        // outputNums[0] = nums[0];
        // for(int i = 1; i < outputNums.Length ; i++) {
        //     outputNums[i] = outputNums[i-1] + nums[i];
        // }
        // return outputNums;
        // try-2
        for (int i = 0; i < nums.Length - 1; i++)
        {
            nums[i + 1] += nums[i];
        }
        return nums;
    }
}

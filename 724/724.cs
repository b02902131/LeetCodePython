public class Solution
{
    public int PivotIndex(int[] nums)
    {
        int sumRight = 0;
        for (int i = 1; i < nums.Length; i++)
        {
            sumRight += nums[i];
        }
        int ptr = 0;
        int sumLeft = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (sumLeft == sumRight)
            {
                return i;
            }
            sumLeft += nums[ptr];

            if (ptr < nums.Length - 1)
            {
                sumRight -= nums[ptr + 1];
            }

            ptr += 1;
        }
        return -1;
    }
}

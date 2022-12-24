public class Solution
{
    public int[] ShortestToChar(string s, char c)
    {
        int[] ans = new int[s.Length];
        int ptr1 = 0;
        int ptr2 = 0;
        int ptr3 = 0;
        while (ptr1 < s.Length)
        {
            if (s[ptr1] == c)
            {
                while (ptr2 < ptr1)
                {
                    if (s[ptr3] == c)
                    {
                        ans[ptr2] = Math.Min(ptr2 - ptr3, ptr1 - ptr2);
                    }
                    else
                    {
                        ans[ptr2] = ptr1 - ptr2;
                    }
                    ptr2++;
                }
                ptr3 = ptr1;
            }
            ptr1++;
        }
        while (ptr2 < ptr1)
        {
            ans[ptr2] = ptr2 - ptr3;
            ptr2++;
        }
        return ans;
    }
}

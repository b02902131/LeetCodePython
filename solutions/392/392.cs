public class Solution
{
    public bool IsSubsequence(string s, string t)
    {
        int sPtr = 0;
        int tPtr = 0;

        while (sPtr < s.Length && tPtr < t.Length)
        {
            if (t[tPtr] == s[sPtr])
            {
                sPtr++;
            }
            tPtr++;
        }

        return sPtr == s.Length;
    }
}

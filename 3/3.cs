public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        Dictionary<char, int> m = new Dictionary<char, int>() { };
        int i = 0;
        int j = 0;
        int ans = 0;
        for (i = 0; i < s.Length; i++)
        {
            if (m.ContainsKey(s[i]))
            {
                j = Math.Max(j, m[s[i]] + 1);
                m[s[i]] = i;
            }
            else
            {
                m[s[i]] = i;
            }
            ans = Math.Max(ans, i - j + 1);
        }
        return ans;
    }
}

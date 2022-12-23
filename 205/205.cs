public class Solution
{
    public bool IsIsomorphic(string s, string t)
    {
        if (s.Length != t.Length)
        {
            return false;
        }

        Dictionary<char, char> m = new Dictionary<char, char> { };
        Dictionary<char, char> mReversed = new Dictionary<char, char> { };

        for (int i = 0; i < s.Length; i++)
        {
            if (m.ContainsKey(s[i]))
            {
                if (m[s[i]] != t[i])
                {
                    return false;
                }
            }
            else if (mReversed.ContainsKey(t[i]))
            {
                if (mReversed[t[i]] != s[i])
                {
                    return false;
                }
            }
            else
            {
                m[s[i]] = t[i];
                mReversed[t[i]] = s[i];
            }
        }

        return true;
    }
}

public class Solution
{
    public bool CheckDistances(string s, int[] distance)
    {
        for (int i = 0; i < 26; i++)
        {
            char testChar = (char)((int)('a') + i);
            List<int> indexes = new List<int>();
            for (int j = 0; j < s.Length; j++)
            {
                if (s[j] == testChar)
                {
                    indexes.Add (j);
                }
            }
            if (indexes.Count == 0)
            {
                continue;
            }
            if (indexes.Count != 2)
            {
                return false;
            }
            if (indexes[1] - indexes[0] - 1 != distance[i])
            {
                return false;
            }
        }
        return true;
    }
}

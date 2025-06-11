/*
Leetcode 3445:You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:

subs has a size of at least k.
Character a has an odd frequency in subs.
Character b has an even frequency in subs.
Return the maximum difference.

Note that subs can contain more than 2 distinct characters.

Example 1:

Input: s = "12233", k = 4

Output: -1

Explanation:

For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.

Example 2:

Input: s = "1122211", k = 3

Output: 1

Explanation:

For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.

Example 3:

Input: s = "110", k = 3

Output: -1

Constraints:

3 <= s.length <= 3 * 104
s consists only of digits '0' to '4'.
The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
1 <= k <= s.length
*/


      class Solution {

    public int maxDifference(String s, int k) {
        int n = s.length();

        int ans = Integer.MIN_VALUE;

        for (char a = '0'; a <= '4'; ++a) {
            for (char b = '0'; b <= '4'; ++b) {
                if (a == b) {
                    continue;
                }

                int[] best = new int[4];
                Arrays.fill(best, Integer.MAX_VALUE);

                // cnt_a, cnt_b: Prefix counts for the 'right' pointer (s[0...right]).
                int cnt_a = 0, cnt_b = 0;
                // prev_a, prev_b: Prefix counts for the 'left' pointer (s[0...left]).
                int prev_a = 0, prev_b = 0;
                // 'left' tracks the end of the prefix we are recording in the 'best' array.
                int left = -1;

                // The main loop iterating through the string with the 'right' pointer.
                for (int right = 0; right < n; ++right) {
                    // Update prefix counts for the current 'right' position.
                    cnt_a += (s.charAt(right) == a) ? 1 : 0;
                    cnt_b += (s.charAt(right) == b) ? 1 : 0;

               
                    while (right - left >= k && cnt_b - prev_b >= 2) {
                        // Get the parity state for the prefix ending at 'left'.
                        int left_status = getStatus(prev_a, prev_b);

                        best[left_status] = Math.min(
                                best[left_status],
                                prev_a - prev_b
                        );

                        // Advance the left pointer and its corresponding prefix counts.
                        ++left;
                        prev_a += (s.charAt(left) == a) ? 1 : 0;
                        prev_b += (s.charAt(left) == b) ? 1 : 0;
                    }

                    int right_status = getStatus(cnt_a, cnt_b);

                    int required_status = right_status ^ 0b10;

                    if (best[required_status] != Integer.MAX_VALUE) {
              
                        ans = Math.max(
                                ans,
                                cnt_a - cnt_b - best[required_status]
                        );
                    }
                }
            }
        }
        return ans;
    }


    private int getStatus(int cnt_a, int cnt_b) {
     
        return ((cnt_a & 1) << 1) | (cnt_b & 1);
    }
}

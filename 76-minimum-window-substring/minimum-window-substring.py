class Solution:
    def minWindow(self, s, t):
        from collections import Counter

        t_count = Counter(t)
        window = {}

        have, need = 0, len(t_count)
        res = [-1, -1]
        res_len = float("inf")

        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Check if this char satisfies requirement
            if char in t_count and window[char] == t_count[char]:
                have += 1

            # Try to shrink window
            while have == need:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Remove left char
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
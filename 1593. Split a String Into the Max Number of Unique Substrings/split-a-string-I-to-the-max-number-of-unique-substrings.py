def maxUniqueSplit(s: str) -> int:
    def backtrack(start, seen):
        if start == len(s):
            return 0
        max_count = 0
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring not in seen:
                seen.add(substring)
                max_count = max(max_count, 1 + backtrack(end, seen))
                seen.remove(substring)
        return max_count

    return backtrack(0, set())
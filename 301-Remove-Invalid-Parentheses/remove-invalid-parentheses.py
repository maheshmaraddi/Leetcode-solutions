class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        open_cnt = 0
        for c in s:
            if c == '(':
                open_cnt += 1
            elif c == ')':
                open_cnt -= 1

        def revert(s):
            reverse = [''] * len(s)
            for i, c in enumerate(s):
                reverse[-i - 1] = ')' if c == '(' else ('(' if c == ')' else c)
            return ''.join(reverse)

        if open_cnt > 0:
            return [revert(res) for res in self.removeInvalidParentheses(revert(s))]

        ans = []
        removes = [[]]
        closes = []
        open_cnt = 0
        consecutive = False
        last_valid = -1
        for i, c in enumerate(s):
            if c == '(':
                open_cnt += 1
            elif c == ')':
                open_cnt -= 1
                if not consecutive:
                    closes.append(i)
                if open_cnt < 0:
                    open_cnt = 0
                    new_removes = []
                    # print(closes)
                    for re in removes:
                        lst = re[-1] if re else -1
                        idx = bisect_right(closes, lst)
                        # print(lst,idx)
                        for j in range(idx, len(closes)):
                            tmp = re[:]
                            tmp.append(closes[j])
                            new_removes.append(tmp)

                        if lst != - 1 and s[lst + 1] == ')':  # this can remove
                            re.append(lst + 1)
                            new_removes.append(re)

                    removes = new_removes
            consecutive = (c == ')')
            if open_cnt == 0: last_valid = i

        last = [""]
        if open_cnt > 0:
            last = self.removeInvalidParentheses(s[last_valid + 1:])
        for re in removes:
            tmp = list(s[:last_valid + 1])
            for i in re:
                tmp[i] = ''
            for lst in last:
                ans.append(''.join(tmp) + lst)
        return ans




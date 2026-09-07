from typing import List, Optional


class Solution:
    def encode(self, strs: List[str]) -> str:
        out = []

        for s in strs:
            out.append(f"{len(s)}:{s}")

        return "".join(out)

    def decode(self, s: str) -> List[str]:
        out = []

        idx = L = 0

        while idx < len(s):
            cur_char = s[idx]
            if cur_char == ":":
                start, end = idx + 1, idx + L + 1
                out.append(s[start:end])
                idx, L = end, 0
            else:
                L = (L * 10) + int(cur_char)
                idx += 1

        return out

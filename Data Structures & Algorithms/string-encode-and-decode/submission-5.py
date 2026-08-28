class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return None
        return "⌊".join(s for s in strs)

    def decode(self, s: str) -> List[str]:
        if s == None:
            return []
        return s.split("⌊")


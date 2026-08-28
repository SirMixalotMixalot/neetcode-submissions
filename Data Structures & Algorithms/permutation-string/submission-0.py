class Solution:   
    def checkInclusion(self, s1: str, s2: str) -> bool:
        characterIndex = lambda c: ord(c) - ord('a')
        if len(s2) < len(s1):
            return False
        s1Counter = [0 for _ in range(26)]
        for c in s1:
            s1Counter[characterIndex(c)] += 1
        slidingCounter = [0 for _ in range(26)]
        for c in s2[:len(s1)]:
            slidingCounter[characterIndex(c)] += 1 
        
        if slidingCounter == s1Counter:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            # evict left
            left = i - 1 
            slidingCounter[characterIndex(s2[left])] -= 1
            # add right
            right = i + len(s1) - 1
            slidingCounter[characterIndex(s2[right])] += 1

            # check if we found a match 
            if slidingCounter == s1Counter: # O(1) comparison
                return True
            # otherwise, continue sliding
        # no match was found
        return False

            

        
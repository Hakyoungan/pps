class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        #greed factor, cookie size sort하기
        g.sort()
        s.sort()

        content_children = 0
        cookie_index = 0

        while cookie_index < len(s) and content_children < len(g):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        return content_children
    
# Example 1
g1 = [1, 2, 3]
s1 = [1, 1]
print(Solution().findContentChildren(g1, s1)) 

# Example 2
g2 = [1, 2]
s2 = [1, 2, 3]
print(Solution().findContentChildren(g2, s2)) 
class Solution:
    def findFrequentTreeSum(self, root):
        cnt = Counter()
        def dfs(root):
            if not root:
                return 0
            sums = root.val + dfs(root.left) + dfs(root.right)
            cnt[sums] += 1
            return sums
        dfs(root)
        maxcnt = max(cnt.values())
        return [s for s, c in cnt.items() if c == maxcnt]        


      

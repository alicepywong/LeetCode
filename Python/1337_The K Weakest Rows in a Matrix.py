class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # Constraints
        if (len(mat) > 100) or (k < 1 or k > len(mat)):
            return
        for a in range(len(mat)):
            if len(mat[a]) < 2:
                return
            if (mat[a].count(0) + mat[a].count(1)) != len(mat[a]):
                return

        count = {}
        for i in range(len(mat)):
            count[i] = mat[i].count(1)

        count_sorted = sorted(count.items(), key=lambda x: x[1])

        count = []
        for j in range(0, k):
            count.append(count_sorted[j][0])

        return count

__author__ = 'karthikb'

class Solution:
    # @param s, a string
    # @return a list of lists of string
    part_dict = {}
    def minCut(self, s):
        #return self.compute_partition(s)
        i, N = 0, len(s)
        return self.dp_compute_partition(s, 0, N - i - 1)

    def compute_partition(self, s):
        N = len(s)
        if N <= 1:
            return 0
        i, j = 0, N - 1
        if s[i] == s[j]:
            return self.compute_partition(s[i+1:j])
        else:
            return min(1 + self.compute_partition(s[i+1:j+1]), 1 + self.compute_partition(s[i:j]))

    def dp_compute_partition(self, data, i, j):

        if (i, j) in self.part_dict:
            return self.part_dict[(i, j)]
        if i > j:
            self.part_dict[(i, j)] = 0
        elif data[i] == data[j]:
            self.part_dict[(i, j)] = self.dp_compute_partition(data, i + 1, j-1)
        else:
            self.part_dict[(i, j)] = min(1 + self.dp_compute_partition(data, i+1, j), 1 + self.dp_compute_partition(data,i, j-1))
        return self.part_dict[(i, j)]

    def iter_compute_partition(self, data):
        N = len(data)
        i, j = 0, N-1

sol = Solution()
print sol.minCut("bb")



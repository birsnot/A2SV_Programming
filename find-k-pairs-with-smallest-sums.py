class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = [(nums1[0] + nums2[0], 0, 0)]
        N1, N2 = len(nums1), len(nums2)
        ans = []
        for _ in range(min(k, N1*N2)):
            _, i, j = heappop(pq)
            ans.append((nums1[i], nums2[j]))
            if j == 0:
                if i + 1 < N1:
                    heappush(pq, (nums1[i + 1] + nums2[0], i + 1, 0))
            if j + 1 < N2:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
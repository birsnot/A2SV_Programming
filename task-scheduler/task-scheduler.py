class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks).most_common()
        max_fr = c[0][1]
        max_fr_count = 0
        for _, fr in c:
            if fr == max_fr:
                max_fr_count += 1
            else:
                break
        return max((n+1)*(max_fr-1) + max_fr_count, len(tasks))

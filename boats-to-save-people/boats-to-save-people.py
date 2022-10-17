class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        i = 0
        j = len(people) - 1
        while i < j:
            while i < j:
                if people[i] + people[j] <= limit:
                    count += 1
                    j -= 1
                    break
                else:
                    j -= 1
            i += 1
        print(count)
        return len(people) - count

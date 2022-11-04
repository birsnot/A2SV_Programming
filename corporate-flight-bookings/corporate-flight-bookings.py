class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        new_range = [0]*(n+2)
        for b in bookings:
            new_range[b[0]] += b[2]
            new_range[b[1]+1] -= b[2]
        ps = [0]*n
        temp = 0
        for i, r in enumerate(new_range[1:-1]):
            temp += r
            ps[i] = temp
        return ps

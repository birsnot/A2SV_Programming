class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        _routes = []
        for route in routes:
            _routes.append(set(route))
        dq = deque([source])
        visited = set([source])
        buses = -1
        while dq:
            buses += 1
            L = len(dq)
            for _ in range(L):
                pos = dq.popleft()
                if pos == target:
                    return buses
                temp = []
                for i, route in enumerate(_routes):
                    if pos in route:
                        for new_pos in route:
                            if new_pos not in visited:
                                visited.add(new_pos)
                                dq.append(new_pos)
                    else:
                        temp.append(route)
                _routes = temp
        return -1
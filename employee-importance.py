"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ids = {}
        for emp in employees:
            ids[emp.id] = emp
        def dfs(v):
            emp = ids[v]
            ret = emp.importance
            for ch in emp.subordinates:
                ret += dfs(ch)
            return ret
        return dfs(id)
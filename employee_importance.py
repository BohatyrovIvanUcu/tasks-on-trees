"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees, id):

        emp_map = {emp.id: emp for emp in employees}

        def add_all_below(emp_id):
            emp = emp_map[emp_id]
            total = emp.importance

            for sub_id in emp.subordinates:
                total += add_all_below(sub_id)

            return total

        return add_all_below(id)

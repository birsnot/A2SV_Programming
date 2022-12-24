class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = 0
        min_salary = salary[0]
        sum = -salary[0]
        
        for n in salary:
            if n < min_salary:
                sum += min_salary
                min_salary = n
            elif n > max_salary:
                sum += max_salary
                max_salary = n
            else:
                sum += n
        return sum/(len(salary)-2)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        a = sum(students)
        b = len(students) - a
        s = 0
        for i in sandwiches:
            if i:
                if a > 0:
                    s += 1
                    a -= 1
                else:
                    break
            else:
                if b > 0:
                    s += 1
                    b -= 1
                else:
                    break
        return len(students) - s
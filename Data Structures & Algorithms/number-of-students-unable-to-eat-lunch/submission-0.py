
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_mapping = Counter(students)
        student_mapping['count'] = len(students)
        for sandwich in sandwiches:
            if student_mapping[sandwich] > 0:
                student_mapping[sandwich] -= 1
                student_mapping['count'] -= 1
            else:
                break
        return student_mapping['count']



        
from domain.assignmnet_domain import assignmnetDomain
from algorithm.backtracking import backtrackingAlgorithm
from utils.data_format import formatting_data

class CSPAlgorithm:
    def __init__(self, programs, courses, instructors, rooms, curriculum) -> None:
        self.programs = programs
        self.courses = courses
        self.instructors = instructors
        self.rooms = rooms
        self.curriculum = curriculum
        self.define_domain_variable()
        self.define_algorithm()
        self.define_result()
    
    def define_domain_variable(self):
        assignmnet = assignmnetDomain(self.programs, self.courses, self.instructors, self.rooms, self.curriculum)
        self.domain_assignment = assignmnet.assignment()
        self.numBlockCourse = assignmnet.numBlockCourse()
        #print(self.domain_assignment)
        
    def define_algorithm(self):
        algo = backtrackingAlgorithm(self.domain_assignment, self.instructors, self.numBlockCourse)
        self.result = algo.backtracking_search()
        #print(self.result)
    
    def define_result(self):
        student_details = {student['_id']: student for student in self.programs}
        course_details = {course['code']: course for course in self.courses}
        teacher_details = {teacher['_id']: teacher for teacher in self.instructors}
        room_details = {room['_id']: room for room in self.rooms}
        schedule = formatting_data(self.result, student_details, course_details, teacher_details, room_details)
        #print(schedule)
        return schedule
    
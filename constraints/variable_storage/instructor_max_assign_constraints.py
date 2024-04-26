import copy

def instructor_max_assign(teacher_course, instructor, course_code):
    instructor_course_scheduler_copy = copy.deepcopy(teacher_course)
    
    if instructor not in teacher_course:
        instructor_course_scheduler_copy[instructor] = []
        
    instructor_course_scheduler_copy[instructor].append(course_code)
    
    return instructor_course_scheduler_copy
    
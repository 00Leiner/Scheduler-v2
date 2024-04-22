def check_instructor_max_assign(teacher_course, instructor):
    teacher_course_copy = teacher_course
    
    if instructor not in teacher_course_copy:
        return True
    
    if len(teacher_course_copy[instructor]) == 5:
        return False
    
    return True

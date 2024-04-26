import copy

def instructor_schedule(teacher_schedule, instructor, day1, day2, time1, time2, course_type):
    teacher_schedule_copy = copy.deepcopy(teacher_schedule)
    
    time_requirements_1 = 3 if course_type == 'Laboratory' else 2
    time_requirements_2 = 2 if course_type == 'Laboratory' else 1
    
    if instructor not in teacher_schedule_copy:
        teacher_schedule_copy[instructor] = {day1: [], day2: []}
        
    if day1 not in teacher_schedule_copy[instructor]:
        teacher_schedule_copy[instructor][day1] = []
    
    if day2 not in teacher_schedule_copy[instructor]:
        teacher_schedule_copy[instructor][day2] = []
        
    teacher_schedule_copy[instructor][day1].extend(range(time1, time1 + time_requirements_1))
    teacher_schedule_copy[instructor][day2].extend(range(time2, time2 + time_requirements_2))
        
    return teacher_schedule_copy

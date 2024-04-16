
def instructor_schedule(teacher_schedule, instructor, day1, day2, time1, time2, course_type):
    teacher_schedule_copy = teacher_schedule
    if course_type == 'Laboratory':
        time_requirements_1 = 3
        time_requirements_2 = 2
    else:
        time_requirements_1 = 2
        time_requirements_2 = 1
    
    if instructor not in teacher_schedule:
        teacher_schedule_copy[instructor] = {day1: [], day2: []}
        
    if day1 not in teacher_schedule[instructor]:
        teacher_schedule_copy[instructor][day1] = []
    
    if day2 not in teacher_schedule[instructor]:
        teacher_schedule_copy[instructor][day2] = []
        
    teacher_schedule_copy[instructor][day1].extend(range(time1, time1 + time_requirements_1))
    teacher_schedule_copy[instructor][day2].extend(range(time2, time2 + time_requirements_2))
        
    return teacher_schedule_copy
    
def check_instructor_schedule(teacher_schedule, instructor, day1, day2, time1, time2, course_type):
    time_requirements_1 = 3 if course_type == 'Laboratory' else 2
    time_requirements_2 = 2 if course_type == 'Laboratory' else 1
    
    teacher_schedule_copy = teacher_schedule
    
    if instructor in teacher_schedule_copy:
        if day1 in teacher_schedule_copy[instructor]:
            
            for ts in range(time1, time1 + time_requirements_1 + 1):
                if ts in teacher_schedule_copy[instructor][day1]:
                    # print("invalid instructor")            
                    return False
            
            if (len(teacher_schedule_copy[instructor][day1]) + time_requirements_1) > 6:
                    # print("invalid instructor")        
                    return False
                
        if day2 in teacher_schedule_copy[instructor]:
            for ts in range(time2, time2 + time_requirements_2 + 1):
                if ts in teacher_schedule_copy[instructor][day2]:
                    # print("invalid instructor")        
                    return False
                
            if (len(teacher_schedule_copy[instructor][day2]) + time_requirements_2) > 6:
                # print("invalid instructor")        
                return False
            
    # print("valid instructor")            
    return True
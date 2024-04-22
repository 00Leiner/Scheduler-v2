def check_instructor_schedule(teacher_schedule, instructor, day1, day2, time1, time2, course_type):
    if course_type == 'Laboratory':
        time_requirements_1 = 3
        time_requirements_2 = 2
    else:
        time_requirements_1 = 2
        time_requirements_2 = 1
    
    teacher_schedule_copy = teacher_schedule
    
    if instructor in teacher_schedule_copy:
        if day1 in teacher_schedule_copy[instructor]:
            if day2 in teacher_schedule_copy[instructor]:
                for ts in range(time2, (time2 + time_requirements_2)):
                    if ts in teacher_schedule_copy[instructor][day2]:
                        return False
                #if (len(teacher_schedule_copy[instructor][day2]) + time_requirements_2) > 6:
                    #return False
            #else:
                #if (len(teacher_schedule_copy[instructor]) + 1) > 5: 
                    #return False
                    
            for ts in range(time1, (time1 + time_requirements_1)):
                if ts in teacher_schedule_copy[instructor][day1]:
                    return False
            
            #if (len(teacher_schedule_copy[instructor][day1]) + time_requirements_2) > 6:
                    #return False
                
        #else:
            #if day2 not in teacher_schedule_copy[instructor]:
                #if (len(teacher_schedule_copy[instructor]) + 2) > 5:
                    #return False
            #else:
                #if (len(teacher_schedule_copy[instructor]) + 1) > 5:
                    #return False
                
    return True
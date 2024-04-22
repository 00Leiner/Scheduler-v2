import random

def forwardChecking(var, domain):
    domain_copy = set(domain)  # Create a copy of the domain
    
    (_program_id, _course_code, _course_type, _instructor, _room1, _room2, _day1, _day2, _time1, _time2) = var
    
    if _course_type == 'Laboratory':
        time_requirements_1 = 3
        time_requirements_2 = 2
    else:
        time_requirements_1 = 2
        time_requirements_2 = 1
    
    for _var in domain_copy.copy():  # Use copy of domain_copy for iteration
        (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = _var
        
        if (_program_id, _course_code) == (program_id, course_code):
            domain_copy.discard(_var)
    
    for ts in range(_time1, _time1 + time_requirements_1 + 1):
        for _var in domain_copy.copy():
            (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = _var
            
            if (_program_id, _day1, ts) == (program_id, day1, time1) or \
               (_instructor, _day1, ts) == (instructor, day1, time1):
                domain_copy.discard(_var)
                
    for ts in range(_time2, _time2 + time_requirements_2 + 1):
        for _var in domain_copy.copy():
            (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = _var
            
            if (_program_id, _day2, ts) == (program_id, day2, time2) or \
               (_instructor, _day2, ts) == (instructor, day2, time2):
                domain_copy.discard(_var)
                
    for ts in range(_time1, _time1 + time_requirements_1):
        for _var in domain_copy.copy():
            (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = _var
            
            if (_room1, _day1, ts) == (room1, day1, time1):
                domain_copy.discard(_var)
                
    for ts in range(_time2, _time2 + time_requirements_2):
        for _var in domain_copy.copy():
            (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = _var
            
            if (_room2, _day2, ts) == (room2, day2, time2):
                domain_copy.discard(_var)
    
    random.shuffle(list(domain_copy))  
             
    return domain_copy

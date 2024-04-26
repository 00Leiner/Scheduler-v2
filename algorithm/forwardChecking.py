def forwardChecking(var, domain):
    domain_copy = set()  # Create a copy of the domain
    
    (_program_id, _course_code, _course_type, _instructor, _room1, _room2, _day1, _day2, _time1, _time2) = var
    
    time_requirements_1 = 3 if _course_type == 'Laboratory' else 2
    time_requirements_2 = 2 if _course_type == 'Laboratory' else 1
    
    for _var in domain:  # Use copy of domain_copy for iteration
        (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = _var
        
        if (_program_id, _course_code) == (program_id, course_code):
            # print("remove var based on program_id and course_code")
            domain_copy.add(_var)
            continue
        
        if _time1 - 1 <= time1 <= _time1 + time_requirements_1 and \
           ((_program_id, _day1, time1) == (program_id, day1, time1) or \
            (_instructor, _day1, time1) == (instructor, day1, time1)):      
            # print("remove var based on program_id, day1, time1 and instructor, day1, time1") 
            domain_copy.add(_var)
            continue
        
        if _time2 - 1 <= time2 <= _time2 + time_requirements_2 and \
           ((_program_id, _day2, time2) == (program_id, day2, time2) or \
            (_instructor, _day2, time2) == (instructor, day2, time2)):
            # print("remove var based on program_id, day2, time2 and instructor, day2, time2") 
            domain_copy.add(_var)
            continue
        
        if _time1 <= time1 < _time1 + time_requirements_1 and \
           (_room1, _day1, time1) == (room1, day1, time1):
            # print("remove var based on room1, day1, time1") 
            domain_copy.add(_var)
            continue
        
        if _time2 <= time2 < _time2 + time_requirements_2 and \
           (_room2, _day2, time2) == (room2, day2, time2):
            # print("remove var based on room2, day2, time2") 
            domain_copy.add(_var)
            continue
            
    domain.difference_update(domain_copy)
    return domain

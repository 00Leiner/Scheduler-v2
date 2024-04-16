def room_sched(room_schedule, room1, room2, day1, day2, time1, time2, course_type):
    room_schedule_copy = room_schedule
    
    if course_type == 'Laboratory':
        time_requirements_1 = 3
        time_requirements_2 = 2
    else:
        time_requirements_1 = 2
        time_requirements_2 = 1
    
    if room1 not in room_schedule_copy:
        room_schedule_copy[room1] = {day1: []}
        
    if room2 not in room_schedule_copy:
        room_schedule_copy[room2] = {day2: []}
        
    if day1 not in room_schedule_copy[room1]:
        room_schedule_copy[room1][day1] = []
        
    if day2 not in room_schedule_copy[room2]:
        room_schedule_copy[room2][day2] = []
        
    room_schedule_copy[room1][day1].extend(range(time1, time1 + time_requirements_1))
    room_schedule_copy[room2][day2].extend(range(time2, time2 + time_requirements_2))
        
    return room_schedule_copy
    
def check_room_availability(room_schedule, room1, room2, day1, day2, time1, time2, course_type):
    room_schedule_copy = room_schedule
    
    if course_type == 'Laboratory':
        time_requirements_1 = 3
        time_requirements_2 = 2
    else:
        time_requirements_1 = 2
        time_requirements_2 = 1
    
    if room1 in room_schedule_copy:
        if day1 in room_schedule_copy[room1]:
            for ts in range(time1, time1 + time_requirements_1):
                if ts in room_schedule_copy[room1][day1]:
                    return False
    if room2 in room_schedule_copy:
        if day2 in room_schedule_copy[room2]:
            for ts in range(time2, time2 + time_requirements_2):
                if ts in room_schedule_copy[room2][day2]:
                    return False
                
    return True
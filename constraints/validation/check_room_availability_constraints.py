import copy

def check_room_availability(room_schedule, room1, room2, day1, day2, time1, time2, course_type):
    
    room_schedule_copy = copy.deepcopy(room_schedule)
    
    time_requirements_1 = 3 if course_type == 'Laboratory' else 2
    time_requirements_2 = 2 if course_type == 'Laboratory' else 1
    
    for room, day, time, time_requirements in [(room1, day1, time1, time_requirements_1), (room2, day2, time2, time_requirements_2)]:
        if room in room_schedule_copy and day in room_schedule_copy[room]:
            for ts in range(time, time + time_requirements):
                if ts in room_schedule_copy[room][day]:
                    # print("invalid room")    
                    return False
       
    # print("valid room")     
    return True

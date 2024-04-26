import copy

def blocks_sched(blocks_schedule, blocks, day1, day2, time1, time2, course_type):
    blocks_schedule_copy = copy.deepcopy(blocks_schedule)
    
    time_requirements_1 = 3 if course_type == 'Laboratory' else 2
    time_requirements_2 = 2 if course_type == 'Laboratory' else 1
    
    if blocks not in blocks_schedule_copy:
        blocks_schedule_copy[blocks] = {day1: [], day2: []}
        
    if day1 not in blocks_schedule_copy[blocks]:
        blocks_schedule_copy[blocks][day1] = []
    
    if day2 not in blocks_schedule_copy[blocks]:
        blocks_schedule_copy[blocks][day2] = []
        
    blocks_schedule_copy[blocks][day1].extend(range(time1, time1 + time_requirements_1))
    blocks_schedule_copy[blocks][day2].extend(range(time2, time2 + time_requirements_2))
        
    return blocks_schedule_copy

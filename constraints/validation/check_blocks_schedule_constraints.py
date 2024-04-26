def check_blocks_schedule(blocks_schedule, blocks, day1, day2, time1, time2, course_type):
    time_requirements_1 = 3 if course_type == 'Laboratory' else 2
    time_requirements_2 = 2 if course_type == 'Laboratory' else 1
    
    blocks_schedule_copy = blocks_schedule
    
    if blocks in blocks_schedule_copy:
        if day1 in blocks_schedule_copy[blocks]:
            for ts in range(time1, time1 + time_requirements_1 + 1):
                if ts in blocks_schedule_copy[blocks][day1]:
                    # print("invalid blocks")
                    return False
            
        if day2 in blocks_schedule_copy[blocks]:
            for ts in range(time2, time2 + time_requirements_2 + 1):
                if ts in blocks_schedule_copy[blocks][day2]:
                    # print("invalid blocks")
                    return False
    
    # print("valid blocks")
    return True
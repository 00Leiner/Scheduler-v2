import copy
from algorithm.forwardChecking import forwardChecking
from constraints.variable_storage.instructor_schedule_constraints import instructor_schedule
from constraints.validation.check_instructor_schedule_constraints import check_instructor_schedule
from constraints.validation.check_room_availability_constraints import check_room_availability
from constraints.variable_storage.room_schedule_constraints import room_sched
from constraints.validation.check_blocks_schedule_constraints import check_blocks_schedule
from constraints.variable_storage.blocks_schedule_constraints import blocks_sched

class backtrackingAlgorithm:
    def __init__(self, domain_assignment, instructors, numBlockCourse):
        self.instructors = instructors
        self.domain_assignment = domain_assignment
        self.numBlockCourse = numBlockCourse
        # print(self.numBlockCourse)
    
    def backtracking_search(self):
        result = []
        self.backtrack({}, self.domain_assignment, {}, {}, {}, result)
        return result
    
    def backtrack(self, schedule, domain, teacher_schedule, room_schedule, blocks_schedule, result):
        if len(result) == 1:
            return
        
        if len(schedule) == self.numBlockCourse:
            result.append(schedule.copy())
            return 
        
        sorted_domain = sorted(domain, key=lambda var: (var[2] != 'Laboratory', var[0]))

        for var in sorted_domain:
            (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = var
            if (program_id, course_code) not in schedule and \
                check_blocks_schedule(blocks_schedule, program_id, day1, day2, time1, time2, course_type) and \
                    check_instructor_schedule(teacher_schedule, instructor, day1, day2, time1, time2, course_type) and \
                        check_room_availability(room_schedule, room1, room2, day1, day2, time1, time2, course_type):
                            
                time_requirements_1 = 3 if course_type == 'Laboratory' else 2
                time_requirements_2 = 2 if course_type == 'Laboratory' else 1
                                    
                schedule[(program_id, course_code)] = {
                    'instructor': instructor,
                    'schedule_1':{
                        'room': room1,
                        'day': day1,
                        'time': (time1, time1 + time_requirements_1)
                        },
                    'schedule_2':{
                        'room': room2,
                        'day': day2,
                        'time': (time2, time2 + time_requirements_2)
                        }}
                                    
                update_teacher_schedule = instructor_schedule(teacher_schedule, instructor, day1, day2, time1, time2, course_type)
                              
                update_room_schedule = room_sched(room_schedule, room1, room2, day1, day2, time1, time2, course_type)
                                  
                update_blocks_schedule = blocks_sched(blocks_schedule, program_id, day1, day2, time1, time2, course_type)     
                            
                print("Blocks Schedule: ", update_blocks_schedule)
                print()
                print("Instructors Schedule: ", update_teacher_schedule)
                print()
                print("Rooms Schedule: ", update_room_schedule)
                print()
                                    
                update_domain = forwardChecking(var, domain)
                                    
                #recursion
                self.backtrack(schedule, update_domain, update_teacher_schedule, update_room_schedule, update_blocks_schedule,  result)
                
                teacher_schedule = update_teacher_schedule
                room_schedule = update_room_schedule
                blocks_schedule = update_blocks_schedule
                        

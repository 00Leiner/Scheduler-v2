from algorithm.forwardChecking import forwardChecking
from constraints.check_instructor_max_assign_schedule import check_instructor_max_assign
from constraints.instructor_max_assign_constraints import instructor_max_assign
from constraints.instructor_schedule_constraints import instructor_schedule
from constraints.check_instructor_schedule_constraints import check_instructor_schedule
from constraints.check_room_availability_constraints import check_room_availability
from constraints.room_schedule_constraints import room_sched

class backtrackingAlgorithm:
    def __init__(self, domain_assignment):
        self.domain_assignment = domain_assignment
        self.program_course = set((program_id, course_code) for program_id, course_code, _, _, _, _, _, _, _, _, in self.domain_assignment)
        
    def backtracking_search(self):
        result = []
        self.backtrack({}, self.domain_assignment, {}, {}, {}, result)
        return result
    
    def backtrack(self, schedule, domain, teacher_schedule, room_schedule, instructor_max, result):
        if len(result) == 2:
            return
        
        if len(schedule) == len(self.program_course):
            result.append(schedule.copy())
            return 
        
        if len(domain) == 0:
            return
        
        sorted_domain = sorted(domain, key=lambda var: (var[2] != 'Laboratory', var[0], var[1]))
        
        for var in sorted_domain:
            (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = var
            if (program_id, course_code) not in schedule:
                if check_room_availability(room_schedule, room1, room2, day1, day2, time1, time2, course_type):
                    if check_instructor_schedule(teacher_schedule, instructor, day1, day2, time1, time2, course_type):
                        if check_instructor_max_assign(instructor_max, instructor):
            
                            if course_type == 'Laboratory':
                                time_requirements_1 = 3
                                time_requirements_2 = 2
                            else:
                                time_requirements_1 = 2
                                time_requirements_2 = 1
                            
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
                                }
                            }
                            
                            update_instructor_max = instructor_max_assign(instructor_max, instructor, course_code)
                            # Perform forward checking
                            update_domain = forwardChecking(var, domain)
                            
                            update_teacher_schedule = instructor_schedule(teacher_schedule, instructor, day1, day2, time1, time2, course_type)
                            
                            update_room_schedule = room_sched(room_schedule, room1, room2, day1, day2, time1, time2, course_type)
                            
                            #recursion
                            self.backtrack(schedule, update_domain, update_teacher_schedule, update_room_schedule, update_instructor_max, result)
                        
                        else:
                            # Remove the invalid assignment from the domain
                            domain.discard(var)
                    else:
                        # Remove the invalid assignment from the domain
                        domain.discard(var)
                else:
                    # Remove the invalid assignment from the domain
                    domain.discard(var)
            else:
                # Remove the invalid assignment from the domain
                domain.discard(var)
class assignmnetDomain:
    def __init__(self, programs, courses, instructors, rooms, curriculum) -> None:
        self.programs = programs
        self.courses = courses
        self.instructors = instructors
        self.rooms = rooms
        self.curriculum = curriculum
        
        self.program_curriculum_data = {}
        self.program_curriculum()
        self.room_by_type = {}
        self.room_type()
    
    def numBlockCourse(self):
        return len(self.program_curriculum_data)
        
    def assignment(self):
        assign = set()
        
        for (program_id, course_code), course_type in self.program_curriculum_data.items():
            rooms_for_course = self.room_by_type.get(course_type, [])
            lecture_rooms = self.room_by_type.get('Lecture', [])
            
            for instructor in self.instructors:
                for room1 in rooms_for_course:
                    for room2 in lecture_rooms:
                        for day1 in range(1, 4):
                            for day2 in self.second_day_schedule(day1):
                                if course_type == 'Laboratory':
                                    time_requirements_1 = 3
                                    time_requirements_2 = 2
                                else:
                                    time_requirements_1 = 2
                                    time_requirements_2 = 1
                                
                                for time1 in range(7, 18 - time_requirements_1):
                                    for time2 in range(7, 18 - time_requirements_2):
                                        assignment_tuple = (program_id, course_code, course_type, instructor['_id'], room1, room2, day1, day2, time1, time2)
                                        assign.add(assignment_tuple)
        
        return assign
    
    def room_type(self):
        self.room_by_type['Laboratory'] = [room['_id'] for room in self.rooms if room['type'] == 'Laboratory']
        self.room_by_type['Lecture'] = [room['_id'] for room in self.rooms]
                
    def program_curriculum(self):
        indexed_curriculum = {}
        for curriculum in self.curriculum:
            key = (curriculum['program'], curriculum['major'], curriculum['year'], curriculum['semester'])
            indexed_curriculum.setdefault(key, []).extend(curriculum['curriculum'])

        for student in self.programs:
            student_id = student['_id']
            key = (student['program'], student['major'], student['year'], student['semester'])
            for course in indexed_curriculum.get(key, []):
                self.program_curriculum_data[(student_id, course['code'])] = course['type']
            
    def second_day_schedule(self, first_day):
        if first_day == 1:
            return [3, 4, 5]
        elif first_day == 2:
            return [4, 5]
        else:
            return [5]

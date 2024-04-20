class assignmnetDomain:
    def __init__(self, programs, courses, instructors, rooms, curriculum) -> None:
        self.programs = programs
        self.courses = courses
        self.instructors = instructors
        self.rooms = rooms
        self.curriculum = curriculum
        
        self.program_curriculum_data= {}
        self.program_curriculum()
        self.by_specialization = {}
        self.instructor_specialization()
        self.room_by_type = {}
        self.room_type()
        
    def assignment(self):
        assign = set()
        for (program_id, course_code), course_type in self.program_curriculum_data.items():
            for instructor in self.by_specialization[course_code]:
                for room1 in self.room_by_type[course_type]:
                    for room2 in self.room_by_type['Lecture']:
                        for day1 in range(1, 7):
                            day2 = self.second_day_schedule(day1)
                            
                            if course_type == 'Laboratory':
                                first_time_schedule = 3
                                second_time_schedule = 2
                            else:
                                first_time_schedule = 2
                                second_time_schedule = 1
                            
                            for time1 in range(7, (20 - first_time_schedule)):
                                for time2 in range(7, (20 - second_time_schedule)):
                                    
                                    assignment_tuple = (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2)
                                    assign.add(assignment_tuple)
        return assign
            
    def instructor_specialization(self):
        for course in self.courses:
            self.by_specialization[course['code']] = []
            for instructor in self.instructors:
                for specialized in instructor['specialized']:
                    if course['code'] == specialized['code']:
                        self.by_specialization[course['code']].append(instructor['_id'])
                        
    def room_type(self):
        self.room_by_type['Laboratory'] = []
        self.room_by_type['Lecture'] = []
        for room in self.rooms:
            if room['type'] == 'Laboratory':
                self.room_by_type['Laboratory'].append(room['_id'])
            else:
                self.room_by_type['Lecture'].append(room['_id'])
                
    def _program_course(self):
          for program in self.programs:
            for course in program['courses']:
                self.program_course[(program['_id'], course['code'])] = course['type']    
        
    def program_curriculum(self):
        for student in self.programs:
            student_id = student['_id']
            student_program = student['program']
            student_major = student['major']
            student_year = student['year']
            student_semester = student['semester']
            
            for curriculum in self.curriculum:
                _student_program = curriculum['program']
                _student_major = curriculum['major']
                _student_year = curriculum['year']
                _student_semester = curriculum['semester']
                
                if all((student_program == _student_program), 
                       (student_major == _student_major), 
                       (student_year == _student_year), 
                       (student_semester == _student_semester)):
                    
                    for course in curriculum['courses']:
                        
                        self.program_curriculum_data[(student_id, course['code'])] = course['type']   
              
    def second_day_schedule(self, first_day):
        list_of_days = list(range(1, 7))

        #2 days gap from first schedule
        first_day_index = list_of_days.index(first_day)
        second_day_index = (first_day_index + 4) % len(list_of_days)
        second_day = list_of_days[second_day_index]

        return  second_day
            
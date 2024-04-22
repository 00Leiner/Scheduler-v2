import requests
from flask import Flask, jsonify
from getData.student_data import fetch_student_data
from getData.room_data import fetch_room_data
from getData.teacher_data import fetch_teacher_data
from getData.course_data import fetch_course_data
from getData.curriculum_data import fetch_curriculum_data
from scheduler.CSPAlgorithm import CSPAlgorithm

class Scheduler:
    def __init__(self) -> None:
        self.getData()
    
    def getData(self):
        self.programs = fetch_student_data()
        self.courses = fetch_course_data()
        self.instructors = fetch_teacher_data()
        self.rooms = fetch_room_data()
        self.curriculum = fetch_curriculum_data()
        
    def CSP(self):
        csp = CSPAlgorithm(self.programs, self.courses, self.instructors, self.rooms, self.curriculum)
        result = csp.define_result()
        return result
        
app = Flask(__name__)
class Fetching:
    def __init__(self):
        self.url = 'http://192.168.176.1:3000/Schedule/create'

    def perform_post_request(self, data):
        response = requests.post(self.url, json=data)

        if response.status_code in [200, 201]:
            return response
        else:
            print(f"Error in POST request. Status code: {response.status_code}")
            print(response.text)
            return response

@app.route('/activate_csp_algorithm', methods=['POST'])
def activate_csp_algorithm():
    try:
        scheduler = Scheduler()
        result = scheduler.CSP()
        
        fetching_instance = Fetching()
        for solution in result:
            response = fetching_instance.perform_post_request(solution)
            print(response.text)
  
        return jsonify({"status": "success", "message": "CSP algorithm activated successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
  
if __name__ == "__main__":
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    scheduler = Scheduler()
    p = scheduler.CSP()
    print(p)
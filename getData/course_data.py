import requests

class Fetching:
    def __init__(self, url):
        self.url = url
    
    def perform_get_request(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            # Assuming the response content is JSON
            data = response.json()
            return data
        else:
            print(f"Error in GET request. Status code: {response.status_code}")
            print(response.text)
            return None
        
def format_data(fetched_data):
    formatted_data = []

    for room in fetched_data.get('courses', []):
        room_info = {
            '_id': room.get('_id', ''),
            'code': room.get('code', ''),
            'description': room.get('description', ''),
            'units': room.get('units', ''),
            'type': room.get('type', '')
        }

        formatted_data.append(room_info)

    return formatted_data

def fetch_course_data():
    fetch_url = 'http://192.168.1.6:3000/Courses/get'
    fetching_instance = Fetching(fetch_url)
    fetched_data = fetching_instance.perform_get_request()

    if fetched_data is not None:
        formatted_data = format_data(fetched_data)
        return formatted_data
    else:
        print('Failed to fetch data.')
        return None
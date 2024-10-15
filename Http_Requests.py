import requests

class HttpRequestsClass:

   def get_status_code(self, url):
        response = requests.get(url)  
        return response.status_code # This will return the status code like 200
    
   def get_response_time(self, url):
        response = requests.get(url)
        return response.elapsed.total_seconds()  # Return response time in seconds
 
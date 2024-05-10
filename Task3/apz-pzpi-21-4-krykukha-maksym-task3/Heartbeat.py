import random
import time
import requests
import Session
import configuration

BASE_URL = configuration.get_base_url()
MAX_RANDOM_OFFSET = 0.45
RAND_RANGE = 11
SLEEP_TIME = 1

# Function to simulate and send heartbeats for a session 
def make_heartbeats(session_id,watcher_id,driver_id):    
    heart_beats = 75    
    while True:        
        try:
            # Check if session is disabled
            if (Session.is_enabled_session(session=session_id)== "DISABLED"):                
             print(session_id, "is disabled")            
            # Simulate heartbeat fluctuation
            rand_num = MAX_RANDOM_OFFSET - (random.randint(0, RAND_RANGE) / 10)            
            heart_beats += rand_num            
            # Prepare JSON data for heartbeat
            json_data = {
                "count": heart_beats,                        
                "sessionId":session_id,                        
                "driverId":driver_id,                        
                "watcherId":watcher_id
            }
            # Send POST request to add heartbeat
            url = f"{BASE_URL}/heartbeat/add"              
            response = requests.post(url, json=json_data)                        
            print(response.json()['count'], ":",response.json()['description']," heartbeat")                    
            time.sleep(SLEEP_TIME)
        except Exception as e:
            # Handle exceptions and wait before retrying
                time.sleep(SLEEP_TIME)

from datetime import datetime
import requests
import configuration

# Base URL for the API endpoint
BASE_URL = configuration.get_base_url()
# Headers for localization
headers = {"localization": "uk",}

# Authentication data for watcher and driver
auth_data_watcher = {    
    "email":"test@gmail.com",    
    "phone":"0123456789",    
    "watcherName":"ADMIN",    
    "watcherSurname":"ADMIN",    
    "password":"ADMIN"
}
auth_data_driver = {    
    "email":"test@gmail.com",    
    "phone":"0123456789",    
    "driverName":"DRIVER",    
    "driverSurname":"DRIVER",    
    "password":"DRIVER"
}

# Function to authenticate the watcher and return the response
def authenticate_watcher() -> str:    
    url = f"{BASE_URL}/auth/watcher_login"          
    try:
        # Send POST request for watcher authentication
            response = requests.post(url, headers=headers, json=auth_data_watcher)    
    except Exception as e :
        print("Error at authentication")
    return(response)
    

# Function to authenticate the driver and return the response
def authenticate_driver(iot) -> str:    
    url = f"{BASE_URL}/auth/driver_login"      
    try:
        # Send POST request for driver authentication
            response = requests.post(url, headers=headers, json=auth_data_driver)        
    except Exception as e :
        print("Error at authentication")
    return(response)    

# Get watcher ID from authentication response
def get_watcher_id():    
    response = authenticate_watcher()    
    print("Watcher", response.json()['watcher']['id'])    
    return(response.json()['watcher']['id'])

# Get driver ID from authentication response
def get_driver_id(iot):   
    response = authenticate_driver(iot)   
    print("Driver", response.json()['driver']['id'])   
    return(response.json()['driver']['id'])

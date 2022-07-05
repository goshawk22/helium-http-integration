# Set up initial directory for putting packets
import os
if not os.path.exists('packets'):
    os.makedirs('packets')

# Import libraries
from fastapi import FastAPI, Request
import json
from datetime import datetime, date

# Create FastAPI app
app = FastAPI()

# Create post at root
@app.post("/")
async def root(info : Request):
    req_info = await info.json()
    date_today = str(date.today())
    time = datetime.now()

    date_path = 'packets/' + date_today + '/'
    if not os.path.exists(date_path):
        os.makedirs(date_path)

    dev_name = req_info['name']

    # Save packet using current time
    folder = date_path + str(dev_name)
    if not os.path.exists(folder):
        os.makedirs(folder)

    path = date_path + str(dev_name) + '/' + str(time) + '.json'
    with open(path, 'w+') as f:
        json.dump(req_info, f, indent=4)

    # Return SUCCESS
    return {
        "status" : "SUCCESS",
        "data" : req_info
    }

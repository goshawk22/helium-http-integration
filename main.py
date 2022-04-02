# Set up initial directory for putting packets
import os
if not os.path.exists('packets'):
    os.makedirs('packets')

# Import libraries
from fastapi import FastAPI, Request
import json
import datetime

# Create FastAPI app
app = FastAPI()

# Create post at root
@app.post("/")
async def root(info : Request):
    req_info = await info.json()

    # Save packet using current time
    time = datetime.datetime.now()
    path = 'packets/' + str(time) + '.json'
    with open(path, 'w+') as f:
        json.dump(req_info, f, indent=4)

    # Return SUCCESS
    return {
        "status" : "SUCCESS",
        "data" : req_info
    }
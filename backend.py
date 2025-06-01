
from fastapi import FastAPI,Request
import uvicorn 

from pydantic import BaseModel, Field
from agnet import initagent 
import uuid
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)
class Prompt(BaseModel):
    user_id: str
    prompt: str

@app.get("/")
async def read_root():
    
    return {"message": "Hello World from FastAPI and Uvicorn!"}


connected_clients = {}




@app.post("/prompt")
async def agent_run(prompt:Prompt):
    user_id = prompt.user_id
    prompt = prompt.prompt
    socket_id = connected_clients.get(user_id)
    agent,thoughts=initagent() 
    res =  agent.invoke(prompt) 
    print(type(res.get('output')))
    return {"answer":str(res.get('output')),"thoughts":thoughts.thoughts}
    



if __name__ == "__main__":
    print("Starting Uvicorn server...")
    
    uvicorn.run(
        "backend:app",  
        host="127.0.0.1",
        port=8000,
        reload=True, 
        log_level="info"
    )
   
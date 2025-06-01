from langchain.callbacks.base import BaseCallbackHandler

from socketio import AsyncServer

class ThoughtCaptureHandler(BaseCallbackHandler):
    def __init__(self):
        
        self.thoughts = []

    async def on_agent_action(self, action, **kwargs):
        thought = f"Thought: {action.log}"
        self.thoughts.append(thought)
        

    async def on_agent_finish(self, finish, **kwargs):
        final_thought = f"Final Answer: {finish.log}"
        self.thoughts.append(final_thought)
        






from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from smolagents import GradioUI

model_id = "meta-llama/Llama-3.3-70B-Instruct"
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], 
                  model=HfApiModel(model_id=model_id,),
                  additional_authorized_imports=["requests","bs4"])

# agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")

GradioUI(agent).launch()
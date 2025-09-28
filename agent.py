from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()
agent = Agent()

@app.entrypoint
def invoke(payload):
    """Agent function"""
    user_message = payload.get("prompt")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()
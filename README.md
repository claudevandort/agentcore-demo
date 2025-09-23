# AWS AgentCore
Set of composable services that allow to build and deploy agents securely and at scale

- **AgentCore Runtime** allows to deploy agents built in a variety of agentic frameworks providing isolation and scalability

- **AgentCore Memory** abstracts away memory management instrastructure, providing short-term and long-term memory that can be shared across agents and sessions.

- **Built-in tools** such as AgentCore code interpleter, and AgentCore browser

- **AgentCore Gateway** provides a way to discover an use tools, APIs, Lambda functions, and services.

- **AgentCore Observability** helps trace, debug, and monitor agents

- **AgentCore Identity** provides identity and access management for agents and tools

# Getting started
```shell
# Create python virtual environment
python -m venv venv
source venv/bin/activate
# Install dependencies
pip install bedrock-agentcore bedrock-agentcore-starter-toolkit strands-agents strands-agents-tools aws-opentelemetry-distro~=0.10.1
pip freeze > requirements.txt
```

# Resources
https://www.youtube.com/watch?v=2890bEb61qQ&t=1240s
https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
https://github.com/awslabs/amazon-bedrock-agentcore-samples
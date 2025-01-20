# Agentic AI

Agentic AI refers to artificial intelligence systems that can operate with varying degrees of autonomy to achieve specified goals. An AI Agent is typically composed of three core components:

- **Foundation Model**: A Large Language Model (LLM) or Small Language Model (SLM) that provides the core reasoning, decision-making, and orchestration capabilities. Examples include GPT-4, Claude, or smaller open-source models.

- **Memory Systems**: Components that maintain context through:
  - Short-term memory: Recent conversation history and immediate context
  - Long-term memory: Persistent knowledge storage using vector databases or other storage solutions
  
- **Tools & Integrations**: External capabilities that allow the agent to:
  - Retrieve information (web search, document querying)
  - Take actions (API calls, database operations)
  - Interact with other systems and services

## Orchestration Tools

These are libraries used to interact with the Foundation models

| Name | Team/Author | Languages | Getting Started |
|---|---|---|---|
Instructor  | Jason Liu | [Python](https://python.useinstructor.com/), [JavaScript](https://js.useinstructor.com/) | [Notebook](tools/instructor/Getting_Started.ipynb) |
Langchain    | Langchain   | [Python](https://python.langchain.com/docs/introduction/), JavaScript | |
LlamaIndex  | LlamaIndex  | Python, JavaScript | |
DSPy       | Stanford NLP | [Python](https://dspy.ai/) | |
llm  | Simon Willison | [CLI](https://llm.datasette.io/en/stable/) | |
Amazon Bedrock | Amazon | Python | |
Azure AI | Microsoft | Python | |
Vertex AI | Google | Python | |
OpenAI SDK | OpenAI | Python | |

## Agentic AI Frameworks

| Name | Company | Languages |
|---|---|---|
CrewAI |  CrewAI | Python |
LangGraph |  LangChain | [Python](https://github.com/olanigan/ai_cookbook/blob/main/tools/langgraph/Getting_Started.ipynb) |
Smolagents |  Huggingface | [Python](https://github.com/olanigan/ai_cookbook/tree/main/tools/smolagents) |
Pydantic AI | Pydantic Services | Python |
LlamaIndex Workflow | LlamaIndex | Python |
Phidata | Phidata | Python |
Bee Agent |  IBM | Python |

Amazon Bedrock Agents | Amazon | Python |
Vertex AI Agent Builder | Google | Python |

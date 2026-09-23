# Introduction to LangSmith

### Step-1: 

Set the LangSmith API Key using the following Link:


[https://smith.langchain.com/](https://smith.langchain.com/o/8f3b2123-029e-55f9-82ce-40965f0bd52a/settings/apikeys)

### Step-2: 
Set the following environment variables of your project:

```
1. GEMINI_API_KEY='your_gemini_api_key'
2. LANGSMITH_TRACING_V2=true
3. LANGSMITH_API_KEY='your_langsmith_api_key'
4. LANGSMITH_ENDPOINT='https://api.smith.langchain.com'
5. LANGSMITH_PROJECT='your_project_name'
```

### Step-3:
Run the LangChain Agent
```
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

agent = create_agent(model="google_genai:gemini-2.5-flash")


result = agent.invoke({"messages": [{"role": "user", "content": "What is ML"}]})

print(result["messages"][-1].content)
```
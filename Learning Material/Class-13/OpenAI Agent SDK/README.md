# OpenAI Agents SDK

The OpenAI Agents SDK enables you to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions. It's a production-ready upgrade of our previous experimentation for agents, Swarm. The Agents SDK has a very small set of primitives:

- Agents, which are LLMs equipped with instructions and tools
- Agents as tools / Handoffs, which allow agents to delegate to other agents for specific tasks
- Guardrails, which enable validation of agent inputs and outputs

See the [Documentation](https://openai.github.io/openai-agents-python/)

Before working on it, You must install **OpenAI Agent SDK** in your coding virtual environment.

```
uv add openai-agents
```
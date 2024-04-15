#!/usr/bin/env python
# coding: utf-8

# In[1]:
 
import os
import pandas as pd
from langchain.llms import OpenAI
from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent

# Access the OpenAI API key from the environment variable
openai_api_key = os.environ.get('OPENAI_API_KEY')

def create_agent(filename: str):
  # Create an OpenAI object using the environment variable
  llm = OpenAI(openai_api_key=openai_api_key)

  # Read the CSV file into a Pandas DataFrame.
  df = pd.read_csv(r'C:\Users\nande\Downloads\churn-dataset.csv')

  # Create a Pandas DataFrame agent.
  return create_pandas_dataframe_agent(llm, df, verbose=True)

# In[2]:


def query_agent(agent, query):
    """
    Query an agent and return the response as a string.

    Args:
        agent: The agent to query.
        query: The query to ask the agent.

    Returns:
        The response from the agent as a string.
    """

    prompt = (
        """
            For the following query, if it requires drawing a table, reply as follows:
            {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}

            If the query requires creating a bar chart, reply as follows:
            {"bar": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}

            If the query requires creating a line chart, reply as follows:
            {"line": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}

            There can only be two types of chart, "bar" and "line".

            If it is just asking a question that requires neither, reply as follows:
            {"answer": "answer"}
            Example:
            {"answer": "The title with the highest rating is 'Gilead'"}

            If you do not know the answer, reply as follows:
            {"answer": "I do not know."}

            Return all output as a string.

            All strings in "columns" list and data list, should be in double quotes,

            For example: {"columns": ["title", "ratings_count"], "data": [["Gilead", 361], ["Spider's Web", 5164]]}

            Lets think step by step.

            Below is the query.
            Query: 
            """
        + query
    )

    # Run the prompt through the agent.
    response = agent.run(prompt)

    # Convert the response to a string.
    return response.__str__()


# In[ ]:





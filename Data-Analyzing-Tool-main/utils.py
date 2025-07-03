from langchain.llms import OpenAI
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent



def query_agent(data, query):
    # Parse the CSV file and create pandas dataframe from its contents
    df = pd.read_csv(data)

    llm = OpenAI()
    
    # Create pandas dataframe agent.
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)

    return agent.run(query)

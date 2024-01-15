import os

from langchain.llms import OpenAI
import streamlit as st
from langchain.chains import SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain #executing prompt template
# Sstreamlit Framework
os.environ['OPENAI_API_KEY'] = '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'
st.title("LangChain Demo with OpenAI API")
input_text = st.text_input('Celebrity Search results')

#prompt TEmplate
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}",
)


# OPENAI LLMS

llm = OpenAI(temperature=0.8) # how much control the agent should have 

chain = LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='person')
second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="when was{person} born",
)
chain2 =  LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='dob')

parent_chain = SimpleSequentialChain(chains=[chain,chain2],verbose=True)
if input_text:
    st.write(parent_chain.run(input_text))

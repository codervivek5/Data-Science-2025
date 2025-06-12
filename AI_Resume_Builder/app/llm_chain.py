import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from langchain_community.llms import Together
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

# Choose LLM
llm_provider = os.getenv("LLM_PROVIDER", "TOGETHER")

if llm_provider.upper() == "TOGETHER":
    llm = Together(
        model="deepseek-ai/DeepSeek-V3",
        temperature=0.3,
        max_tokens=150  ,
        together_api_key=os.getenv("TOGETHER_API_KEY")
    )
elif llm_provider.upper() == "GEMINI":
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
else:
    raise ValueError("Unsupported LLM Provider")

# Prompt Template
template = PromptTemplate.from_template("""
Generate a resume for:
Name: {name}
Role: {role}
Skills: {skills}
Experience: {experience} years

Return:
- A 2-3 line professional summary
- Three bullet points for experience
""")

# 🧠 Chain
chain: Runnable = template | llm | StrOutputParser()

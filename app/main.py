from langchain_anthropic.chat_models import ChatAnthropic
import time
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from loguru import logger
from typing import Any, Union
from langchain_core.runnables.base import RunnableSequence, Runnable
from typing_extensions import TypedDict
from tqdm import tqdm
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn



app = FastAPI()



load_dotenv(dotenv_path='secrets/secrets.env')


llm = ChatAnthropic(temperature=0.1, 
                    model_name="claude-3-haiku-20240307",
                    max_tokens_to_sample=4096,
                    timeout=60,
                    streaming=True)

prompt = PromptTemplate(template='Answer question.\n{question}')
Chat = prompt | llm


def chat(input: str) -> Any:
    return Chat.invoke(input)

@app.post("/chat_async")
async def chat_async(input: str) -> Any:
    m = await Chat.ainvoke(input)
    return m.content



if __name__=='__main__':
    uvicorn.run(
        app=app,
        host='0.0.0.0',
        port=30000
    )
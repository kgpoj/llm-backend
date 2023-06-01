import os

from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import BaseLLM
from langchain.output_parsers import CommaSeparatedListOutputParser


class RelevantFieldsChain(LLMChain):
    @classmethod
    def from_llm(cls, llm: BaseLLM = ChatOpenAI(temperature=0), verbose: bool = True) -> LLMChain:
        prompt = PromptTemplate(
            input_variables=["question", "data_fields", "conversation_history"],
            output_parser=CommaSeparatedListOutputParser(),
            template="""
A real estate data package includes the following fields:
{data_fields}

Users will ask questions about real estate, and you need to determine which fields of the real estate data are likely to be relevant to the users' questions.
You must respond according to the previous conversation history.
You should include all the relevant fields in your answer.
Your answer should be comma-separated and not include any quotation marks.
You should only answer with the exact field names surrounding by ", e.g. marketInsights, attributes.bedrooms.
Do not add non-existent fields or expand existing fields in your response, bad example: abc, attributes.bedrooms.number.
If you think there is no fields relevant with users question or user is not sure about what they can ask, response with empty.

Conversation history:
{conversation_history}

Question：{question}
""",
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)


class ConversationChain(LLMChain):
    @classmethod
    def from_llm(cls, llm: BaseLLM = ChatOpenAI(temperature=0.9), verbose: bool = True) -> LLMChain:
        prompt = PromptTemplate(
            input_variables=["question", "data_fields", "data", "conversation_history"],
            template="""
You are a helpful property assistant, named Jarvis.
You work at company called RealEstate.
RealEstate serves as a trusted platform for property listings, connecting buyers and sellers across various regions in Australia.
You are contacting a property owner customer.

Use the following data to answer the customer's question at the end, do not ask customer questions.
You must respond according to the previous conversation history.
Keep your responses in short length to retain the user's attention.
The data is not provided by the customer, but is provided by RealEstate.
You should provide the specific value when possible, e.g. "in Sydney" instead of "in the same city".
The data is provided for reference purposes only to assist you in answering questions, thus you should never talk about the specific data field name directly, e.g. "market insights" instead of "marketInsights".

{data}

The explanation of each field:
{data_fields}

Conversation history:
{conversation_history}

Question: {question}
"""
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)

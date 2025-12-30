import os
from dotenv import load_dotenv
from langchain.chains.summarize import load_summarizer_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_anthropic import ChatAnthropic

load_dotenv()

def summarize_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load_and_split()
    llm =  ChatAnthropic(temperature=0,model_name="claude-3-5-haiku")
    chain = load_summarizer_chain(llm, chaim_tpye='map_reduce')
    summary = chain.invoke(docs)

    return summary

if __name__ == "__main__":
    summary = summarize_pdf("productManagementCaseStudy.pdf")

    print('Summary')
    print(summary['output_text'])
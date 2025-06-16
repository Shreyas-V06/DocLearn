from langchain_core.prompts import ChatPromptTemplate

'''STEP 5: Load Chat Prompt'''

def LoadPrompt():
    prompt= ChatPromptTemplate.from_template("""
Answer the following question based on the context mentioned below:
                                          
<context>
{context}
</context>
                                          
Question: {input}""")
    return prompt


from langchain import PromptTemplate
from langchain import LLMChain
from langchain.llms import CTransformers
from src.helper import *

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"


instruction = "Convert the following text from English to French: \n\n {text}"


SYSTEM_PROMPT = B_SYS + DEFAULT_SYSTEM_PROMPT + E_SYS
template = B_INST + SYSTEM_PROMPT + instruction + E_INST


prompt = PromptTemplate(template=template, input_variables=["text"])


llm = CTransformers(model='/Users/coschool/Desktop/Anup/project/llama-2-cpu-on-machine/model/llama-2-7b-chat.ggmlv3.q4_0.bin',
                    model_type='llama',
                    config={'max_new_tokens': 128,
                            'temperature': 0.01}
                   )

if __name__ == '__main__':
    LLM_Chain=LLMChain(prompt=prompt, llm=llm)

    print(LLM_Chain.run("How are you?"))
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage

#promptTemplates -> (recebe dicionário de saida)

# prompt_template = PromptTemplate.from_template("Gere para mim uma lista de pré atendimento sobre: {assunto}. Escreva em {lingua}")
# retorno = prompt_template.invoke({"assunto": "imobiliária", "lingua":"pt-br"})

# print(retorno)


#ChatPromptTemplate

chat_prompt_template = ChatPromptTemplate(
    ["Gere para mim um script de pré atendimento sobre: {assunto}. Escreva em {lingua}"]
)

retorno = chat_prompt_template.invoke({"assunto": "imobiliária", "lingua": "pt-br"})

print(retorno)
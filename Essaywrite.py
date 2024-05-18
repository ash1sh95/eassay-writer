import streamlit as st
from langchain.prompts import promptTemplate
from langchain.llms import cTransformers

##function to get response from LLama 2 model 

def LLamafunction(input_text,num_words,essay_style):

    ##llama model 
    llm=CTransformners(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_token':256,
                                'temperature':0.01})

    template=""" write an essay for {essay_style} job profile for a topic {input_text} with the {num_words} words"""

    prompt=PromptTemplate(input_variables=["essay_style","input_text","num_words"],template=template)


    response=llm(prompt.format(style=essay_style,text=input_text,n_words=num_words))
    print(response)
    return(response)


st.set_page_config (page_title ="Write an essay",
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate essay")

input_text=st.text_input("Enter the essay topic")

## columns for addtional fields 

col1,col2=st.columns([5,5])

with col1:
    num_words=st.text_input('Number of words')
with col2:
    essay_style=st.selectbox('writing the essay for',('Students','Professionals','Research scholar','layman'), index=0)

submit=st.button("Write")

###response viwer
if submit:
    st.write(LLamafunction(input_text,num_words,essay_style))


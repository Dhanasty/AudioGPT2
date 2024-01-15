import streamlit as st

import whisper
from audiorecorder import audiorecorder

import os 
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from gpt_qa import ask_question
from transcribe import get_text
import pickle
os.environ["OPENAI_API_KEY"] = "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"

#st.title("Audio GPT")
# wav_audio_data = st_audiorec()

# if wav_audio_data is not None:
#     st.audio(wav_audio_data, format='audio/wav')
# Open the file in read mode
content = ""
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    

st.title('Audio GPT')

audio = audiorecorder("Click to record", "Click to stop recording")
switch = False
if st.button("Reset"):
    content = ""
    with open('example.txt', 'w') as file:
        file.write(content)
if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.export().read())  

    # To save audio to a file, use pydub export method:
    audio.export("tempDir/audio.wav", format="wav")
    switch = True

    # # To get audio properties, use pydub AudioSegment properties:
    # st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")

# File uploader widget
# uploaded_file = st.file_uploader("Choose an audio file...", type=['wav', 'mp3', 'ogg'])

# if uploaded_file is not None:
#     # Display file details
#     file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
#     st.write(file_details)

#     # Create a directory if it doesn't exist
#     directory = "tempDir"
#     if not os.path.exists(directory):
#         os.makedirs(directory)

#     # Save the file to the server
#     file_path = os.path.join(directory, uploaded_file.name)
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
if(switch):
    content +=  get_text("tempDir/"+"audio.wav") 
    print(content)
    with open('example.txt', 'w', encoding='utf-8') as file:
        file.write(content)
    #text = text[0:14000]
    #print(text[0:50])
    if len(content) > 10 :
        user_input = st.text_input("Enter the question you want to ask: ")
        ans = ask_question(content,user_input)
        st.write(ans)
    else:
        st.write("No words detected")



# def ask_question(content,qa):
#     os.environ["OPENAI_API_KEY"] = "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"
#     text_splitter = CharacterTextSplitter(
#     separator="\n",
#     chunk_size=800,
#     chunk_overlap = 40,
#     length_function = len,
#     )
#     texts = text_splitter.split_text(content)
#     embeddings = OpenAIEmbeddings(openai_api_key="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")
#     document_search= FAISS.from_texts(texts,embeddings)
#     chain = load_qa_chain(OpenAI(),chain_type="stuff")
#     query = qa
#     docs = document_search.similarity_search(query)
#     ans = chain.run(input_documents = docs,question=query)
#     return ans



# if __name__ == '__main__':
#     main()

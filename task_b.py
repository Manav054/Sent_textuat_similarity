import spacy.cli 
spacy.cli.download("en_core_web_lg")
import streamlit as st
import spacy

nlp = spacy.load("en_core_web_lg")

def calculate_similarity(text1, text2) :
  sent1 = nlp(text1)
  sent2 = nlp(text2)
  value = sent1.similarity(sent2)
  return round(value, 4)

def main() :
    st.title("Semantic Similarity Tester")
    html_temp = """
    <div style = "backgroud-color : tomato ; padding : 10px">
    <h2 style = "color : white ; text-align : center ;>Streamlit Semantic Textual Similarity App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    text1 = st.text_input("Text1", "Type Here")
    text2 = st.text_input("Text2", "Type Here")
    similarity = ""
    
    if st.button("Calculate similarity") :
        similarity = calculate_similarity(text1, text2)
    st.success("Similarity is {}".format(similarity))

if "__name__" == "__main__" :
    main()

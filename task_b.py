# -*- coding: utf-8 -*-
"""Task_B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zkG5-ZSUJGJaP0_DeqW1Mrw0fEFfMj2n
"""
-m pip install --upgrade pip
!pip install sentence_transformers

import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("bert-base-nli-mean-tokens")

def calculate_similarity(text1, text2) :
  sent1 = model.encode(text1)
  sent2 = model.endcode(text2)
  value = cosine_similarity(sent1, sent2)[0]
  return round(value[0], 4)

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

if __name__ == '__main__' :
  main()



import requests
import bs4
from bs4 import BeautifulSoup
import streamlit as st

def recuper_text_bakhtech() :
    text = []
    # get web site
    site = requests.get('https://bakhtech.com/')
    
    # extract html code of website
    site_html = BeautifulSoup(site.content, 'html.parser')
    
    #les sous titres
    contenu = site_html.find_all("div", class_ ="block votreref-bloc")
    
    #liste de de sous titres
    for i in range(len(contenu)): 
        text.append(contenu[i].text)
    return text

def recuper_text_dit() :
    text = []
    # get web site
    site = requests.get('https://dit.sn/')
    
    # extract html code of website
    site_html = BeautifulSoup(site.content, 'html.parser')
    
    #les sous titres
    contenu = site_html.find_all("div", class_ ="et_pb_blurb_container")
    
    #liste de de sous titres
    for i in range(len(contenu)): 
        text.append(contenu[i].text)
    return text  

def app_bakhtech(): 
    st.image('bakhtech.png' , output_format='png',width=None,use_column_width=True,clamp=False)   
    text = recuper_text_bakhtech()
    for i in range(len(text)) :
        st.write(text[i])

def app_dit(): 
    st.image('dit.png' , output_format='png',width=None,use_column_width=True,clamp=False)   
    text = recuper_text_dit()
    for i in range(len(text)) :
        st.write(text[i])

st.sidebar.title('OPTIONS')
option = st.sidebar.selectbox(
  'Choisit votre site svp!',
  ('None','DIT','BAKHTECH'))
if option == 'DIT' :
    app_dit() 
if option == 'BAKHTECH' :
    app_bakhtech() 


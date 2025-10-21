import PyPDF2
import torch
import docx
from transformers import pipeline
from gtts import gTTS
import tempfile
import streamlit as st
import time
def extract_text_from_pdf(file):
    aa=PyPDF2.PdfReader(file)
    text=""
    for page in aa.pages:
        text += page.extract_text()
    return text
def extract_text_from_docx(file):
    bb = docx.Document(file)
    text =""
    for para in bb.paragraphs:
        text += para.text + '\n'
    return text
cc = pipeline('summarization')
def summarize_text(text, max_length=150, min_length=50):
    summary = cc(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
def text_to_speech(summary_text):
    dd =gTTS(text=summary_text, lang='en')
    temp_audio= tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    dd.save(temp_audio.name)
    return temp_audio.name
st.title('* welcome to my avatar *')
ff = None
ee = st.file_uploader("Upload a PDF or DOCX", type=["pdf", "docx"])
if ee and st.button("Summary and Voice"):
    gg = extract_text_from_pdf(ee) if ee.name.endswith(".pdf") else extract_text_from_docx(ee)
    ff = summarize_text(gg)
    hh = text_to_speech(ff)
    st.subheader("Summary")
    st.write(ff)
    st.audio(hh, format="mp3")
from py_avataaars import PyAvataaar
from py_avataaars import (AvatarStyle, TopType, HairColor, ClotheGraphicType,EyesType, EyebrowType, SkinColor, MouthType, NoseType, ClotheType)
def zara_avatar(mouth, talking_star):
    avatar = PyAvataaar(
        style=AvatarStyle.CIRCLE,
        top_type=TopType.LONG_HAIR_STRAIGHT,
        hair_color=HairColor.BLACK,
        clothe_graphic_type=ClotheGraphicType.DIAMOND,
        eye_type=EyesType.DEFAULT,
        eyebrow_type=EyebrowType.DEFAULT_NATURAL,
        skin_color=SkinColor.LIGHT,
        mouth_type=mouth,
        nose_type=NoseType.DEFAULT,
        clothe_type=ClotheType.SHIRT_V_NECK)
    avatar.render_png_file(talking_star)
zara_avatar(MouthType.SMILE, "zara_closed.png")
zara_avatar(MouthType.SERIOUS, "zara_mid.png")
zara_avatar(MouthType.EATING, "zara_open.png")
# st.title('* welcome to my avatar *')
st.header("zara")
m =st.empty()
n = ['zara_closed.png', 'zara_mid.png', 'zara_open.png', 'zara_mid.png']
if ff:
    c=ff
    p=len(c.split())*0.4
    h=time.time()
    while time.time()-h<p:
        for k in n:
            m.image(k, width=400)
            time.sleep(0.3)
else:
    st.warning("Please enter some text first.")
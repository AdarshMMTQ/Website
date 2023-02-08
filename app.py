from tkinter import CENTER
from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Kayplayz Esports", page_icon=":fire:", layout="wide")
st.markdown("<h1 style='text-align: center; color: yellow;'>Welcome to Kayplayz Esports 🔥</h1>", unsafe_allow_html=True)


#json data

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")



#lottie loading

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_i9arxzcg.json")
img_fade = Image.open("images/fade.png")
img_jett = Image.open("images/jett.png")
img_reyna = Image.open("images/reyna.png")
img_omen = Image.open("images/omen.png")
img_sage = Image.open("images/sage.png")


#Sub heading

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Goals")
        st.write("##")
        st.write(
            """
            - We are currently looking for a backup player in our roaster.
            
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


#Info 

with st.container():
    st.write("---")
    st.header("Valorant Roaster")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_fade)
    with text_column:
        st.subheader("Sidhant")
        st.write(
            """
            Fade Main
            """
        )


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_jett)
    with text_column:
        st.subheader("Melrose")
        st.write(
            """
            Jett Main
            """
        )


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_reyna)
    with text_column:
        st.subheader("RichBlood")
        st.write(
            """
            Reyna Main
            """
        )


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_omen)
    with text_column:
        st.subheader("Dub")
        st.write(
            """
            Omen Main
            """
        )


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_sage)
    with text_column:
        st.subheader("Adarsh")
        st.write(
            """
            Sage Main
            """
        )


#contact

with st.container():
    st.write("---")
    st.header("Contact us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/joshphjohnson62@gmail.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
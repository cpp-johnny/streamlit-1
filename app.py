# to run type `python -m streamlit run app.py`
# tutorial from https://www.youtube.com/watch?v=VqgUkExPvLY

from PIL import Image       # pip install Pillow
import streamlit as st      # pip install streamlit
import requests
import streamlit as st
from streamlit_lottie import st_lottie      # pip instal streamlit-lottie


st.set_page_config(page_title="Testing", page_icon="💩", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Using local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# Load Asset using Lottie
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_huh_cat = Image.open("images/huh_cat.jpg")      # download pics into folder called \images
img_blue_cat = Image.open("images/blue.jpg")


# Header
with st.container():    # container to be neater 
    st.subheader("Hello welcome :wave:")
    st.title("A Mock Demo")
    st.write(
        "Blah Blah Blah"
    )
    st.write("[Link to a rickroll](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

with st.container():
    st.write("---")     # this is a line break
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("This is a section")
        st.write("##")
        st.write(
            """
            This is a a list of bullet points:
            - bullet 1
            - bullet 2
            - bullet 3

            this is a paragraph :rocket: 
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")      # inserting the lottie gif

# Showcase projects
with st.container():
    st.write("---")
    st.header("can use this to display your projects or something idk")
    st.write("##")
    image_column, text_column = st.columns((1, 2))      # text column is twice as big as imag column
    with image_column:
        st.image(img_blue_cat)  # using pillow
    with text_column:
        st.subheader("This is a subheader")
        st.write(
            """
            Wow strealit is actually fun and easy to use!
            """
        )
        st.markdown("[Watch a video for fun...](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_huh_cat)
    with text_column:
        st.subheader("bro this is actually easy to use")
        st.write(
            """
            I love streamlit
            """
        )
        st.markdown("[Watch a video for fun...](https://www.youtube.com/watch?v=dQw4w9WgXcQ)") 

# Contact area
with st.container():
    st.write("---")
    st.header("contact me")
    st.write("bro dont actually send")
    st.write("when you hover your mouse over the button it changes colour lol")

    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
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


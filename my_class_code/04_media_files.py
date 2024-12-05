import streamlit as st
import pandas as pd
from PIL import Image

def main():

    # Image
    img = Image.open("data/image_01.jpg")
    st.image(img, use_container_width=True)

    st.image("https://media.licdn.com/dms/image/v2/D4D03AQGnpnDpIXj6mQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1729513335603?e=1738800000&v=beta&t=L8jKAQe07EeAxooZe0iTNeZr1T7LHF3Y4TbQGlQFWiI")

    # Video
    video_file = open("data/secret_of_success.mp4", "rb").read()
    st.video(video_file,  start_time=2.50)

    # Audio Files
    audio_file = open("data/song.mp3", "rb")
    st.audio(audio_file.read(), format='audio/mp3')
    
if __name__ == '__main__':
    main()
import time
import cv2
import streamlit as st
from util import predict

st.set_page_config(layout="wide", page_title="Crowd Counting App", page_icon="👨‍👩‍👧‍👦")
st.sidebar.title("Crowd Counting App")
options = st.sidebar.radio("Select option", ("Image", "Video"))

if options == "Image":
    st.markdown("<h1 style='text-align: center; color: white;'>Crowd Counting with Image</h1>", unsafe_allow_html=True)
    image = st.sidebar.file_uploader("Upload image", type=["jpg", "png", "jpeg"])
    submit = st.sidebar.button("Submit")
    if image is not None and submit:
        with open("resources/Image/image.jpg", "wb") as f:
            f.write(image.getbuffer())
        cv2_image = cv2.imread("resources/Image/image.jpg")
        cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(image, caption="Uploaded Image", width=400)
        with col2:
            with st.spinner("Predicting..."):
                label = predict(cv2_image)
            st.markdown(f"<h1 style='text-align: center; color: white;'>This image has {round(label)} people</h1>", unsafe_allow_html=True)

if options == "Video":
    st.markdown("<h1 style='text-align: center; color: white;'>Crowd Counting with Video</h1>", unsafe_allow_html=True)
    video = st.sidebar.file_uploader("Upload video", type=["mp4", "mov", "avi"])
    alert_input = st.sidebar.number_input("Alert if number of people is greater than", min_value=0, value=0)
    submit = st.sidebar.button("Submit")
    if video is not None and submit:
        with st.spinner("Saving video..."):
            with open("resources/Video/video.mp4", "wb") as f:
                f.write(video.getbuffer())
        st.sidebar.success("Video saved successfully")
        st_frame, st_heatmap = st.columns([1, 1])
        st_frame.markdown("<h1 style='text-align: center; color: Green;'>Frame</h1>", unsafe_allow_html=True)
        st_heatmap.markdown("<h1 style='text-align: center; color: Red;'>Heatmap</h1>", unsafe_allow_html=True)
        with st_frame:
            st.markdown(str(time.time()))
            st.markdown("<img src='http://localhost:6299/start' width='480' height='270'>", unsafe_allow_html=True)
        # with st_heatmap:
        #     st.markdown("<h1 style='text-align: center; color: Red;'>Heatmap</h1>", unsafe_allow_html=True)
        
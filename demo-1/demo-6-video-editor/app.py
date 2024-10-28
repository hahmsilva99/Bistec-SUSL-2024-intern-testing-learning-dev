import streamlit as st
from moviepy.editor import VideoFileClip, vfx
import tempfile
import os


st.markdown("<h1 style='text-align: center;'>Video Editor</h1>", unsafe_allow_html=True)
st.markdown("--")


video_file = st.file_uploader("Upload your video", type=["mp4", "mov", "avi"])

if video_file:
    
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    
    
    video = VideoFileClip(tfile.name)
    
    
    st.markdown("<h2 style='text-align: center;'>Information</h2>", unsafe_allow_html=True)
    st.markdown(f"<h6>Duration: {video.duration:.2f} seconds</h6>", unsafe_allow_html=True)
    st.markdown(f"<h6>Size: {video.size} (Width x Height)</h6>", unsafe_allow_html=True)
    st.markdown(f"<h6>FPS: {video.fps}</h6>", unsafe_allow_html=True)

    
    st.markdown("<h2 style='text-align: center;'>Resizing</h2>", unsafe_allow_html=True)
    new_width = st.number_input("New Width", value=video.size[0])
    new_height = st.number_input("New Height", value=video.size[1])

    
    st.markdown("<h2 style='text-align: center;'>Rotation</h2>", unsafe_allow_html=True)
    rotation_angle = st.number_input("Rotation Angle (Degrees)", value=0)

    
    st.markdown("<h2 style='text-align: center;'>Filters</h2>", unsafe_allow_html=True)
    filter_options = st.selectbox("Select Filter", options=["None", "Black & White", "Mirror", "Speed up 2x"])

    
    apply_changes = st.button("Apply Changes")

    if apply_changes:
        
        if new_width != video.size[0] or new_height != video.size[1]:
            video = video.resize((new_width, new_height))

        
        if rotation_angle != 0:
            video = video.rotate(rotation_angle)

        
        if filter_options == "Black & White":
            video = video.fx(vfx.blackwhite)
        elif filter_options == "Mirror":
            video = video.fx(vfx.mirror_x)
        elif filter_options == "Speed up 2x":
            video = video.fx(vfx.speedx, factor=2)

        
        output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        video.write_videofile(output_file.name, codec="libx264")

        
        st.video(output_file.name)

        
        with open(output_file.name, 'rb') as f:
            st.download_button('Download Edited Video', f, file_name='edited_video.mp4')

        
        os.remove(output_file.name)
        os.remove(tfile.name)

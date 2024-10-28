# demo-6-video-editor
 
 This Video Editor is a simple web-based application built using Streamlit and the MoviePy library. It allows users to upload video files, view basic video information, and perform common video editing operations like resizing, rotating, applying filters, and downloading the edited video.

Features:

    Upload Video: Upload video files in MP4, MOV, AVI formats.
    Video Information: Displays video details including duration, size (width & height), and FPS (frames per second).
    Resizing: Adjust the width and height of the video.
    Rotation: Rotate the video by a specified degree.
    Filters: Apply filters such as Black & White, Mirror, and Speed Up (2x).
    Download Edited Video: Save the edited video to your local system.

Requirements:

    Python 3.x
    Streamlit
    MoviePy

Installation:

    1. Install Python: Download and install Python if you haven't already from Python's official site.

    2. Install required dependencies: Open your terminal or command prompt and run the following commands:

        pip install streamlit moviepy


Usage:
   1. Clone or Download the Repository: Download the code files from this repository to your local machine.

    2. Run the Application: Navigate to the folder where the app code (app.py) is located and run:


        streamlit run app.py


This will start a local server, and the app will open in your web browser.


Edit Videos:

    Upload a video file.
    View video information such as duration, size, and FPS.
    Resize or rotate the video as needed.
    Apply filters like black & white or mirror effects.
    Download the edited video after applying changes.

Example Workflow:

        Upload a Video: Use the file uploader widget to upload an MP4, MOV, or AVI video.
        View Video Information: Get details about the video's duration, size, and FPS.
        Edit Video:
        Resize the video to new dimensions (width and height).
        Rotate the video by specifying the angle in degrees.
        Apply filters such as black & white, mirror, or increase playback speed by 2x.
        Download the Edited Video: Save the processed video to your local machine by clicking the download button.

Technologies Used:

        Streamlit: Framework for creating web apps with Python.
        MoviePy: A video editing library for Python.
# video2password

Work in progress.  Video -> Audio -> Text -> rockyou.txt  

Requires: moviepy  easiest way to get it: pip3 install moviepy

Input video and use the transcript produced to write a plausible password list file.

Use the example.ogv file to test it out from the command line.  In Linux, you must chmod +x the file

From the command line navigate to the directory you downloaded the repository to, then type:

pip3 install moviepy (If you don't have moviepy installed)

chmod +x example.ogv (This is only for Linux)

python3 video2password.py 

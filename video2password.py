'''                  Video to Password

Maybe what they say is what they mean?  Let's see.  Add a video clip for your
data and see if it unlocks any doors.  Good luck!

    Acceptable Video Formats:
        MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)
        3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)
        OGG (ogg, oga, ogv, ogx)
        WMV (wmv, wma, asf*)

Author: Nick Sepe
'''
import convertClip as cc
# make sure the file you pass is in the same directory
data = input("What is the name of your file? (include extension)"):
cc.convert(data)

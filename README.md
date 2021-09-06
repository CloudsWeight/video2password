# video2password

Work in progress.  Video -> Audio -> Text -> rockyou.txt  

Requires: moviepy and an IBM cloud.ibm.com account for apikey/url.

The program asks for the name of the movie file you want to convert and translates the speech from the video to a list of text.  Planning more functionality in the future.  

Acceptable Video Formats:
        MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)
        3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)
        OGG (ogg, oga, ogv, ogx)
        WMV (wmv, wma, asf*)

Sample output from the include .mp4 is: ["spears spears once on a pain the suffering in the discomfort something that's why everybody raised their hands my ", "do you have it was not a big thing because you remember what that's it ", "but then there's another thing ", 'Hey Lori this cold if you could find a way to push to paying ', 'and and and never stopping ', 'first ']

The quality of translation of course depends on the speech quality of the video file but there are different accent Language Models available with IBM speech to text.

PyMeme
======

start server.py, optionally specifying the address and port to listen on (-a, and -p respectively)

then open your web browser to "127.0.0.1:8888" (or what ever ip and port you specified upon starting)

GET parameters that are supported: 

* meme    -- which meme to use, a list is in meme_map in meme.py
* top     -- the caption to go at the top of the picture
* bottom  -- the caption to go at the bottom of the picture

features that are NOT yet implemented:

* width  -- set the width of the returned png
* height -- set the height of the returned png
* foreground -- the foreground color of the text
* background -- the background(stroke) color of the text
* font       -- which font to use

required libraries
------------------

in order to run properly, pyMeme needs py2cairo and tornado webserver installed

Also required is that the font Impact.ttf be installed on the system


Other notes
-----------
I need to find a better way to add templates, the way I have it now is hackish and ugly

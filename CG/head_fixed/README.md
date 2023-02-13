# CSC629 Computer Graphic course final project.
An ar project that showing some bubbles moving randomly on a 3-d environment. And it can be opened on a cellphone. This project can stimulate human head movement and view different aspects of the environment by gyroscope.

## deploy
CMD: enter 'python -m http.server' on computer under work file directory.
on cellphone, enter http://[IP]:[port]head_track_stereo/head_track_stereo.html

Using three.js

Using 6 pictures build a 3D Cubemap background (Source：https://www.humus.name/Textures/Storforsen.zip)
Then using StereoEffect.js doing render

detect gyroscope and using handleOrientation get the alpha, beta, gamma value of it to control movement. (https://blog.csdn.net/a6713827/article/details/103265221)

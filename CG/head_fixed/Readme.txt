1. 因为项目需要使用陀螺仪更改镜头，部署会复杂点。项目需要主机部署，然后使用手机操作。
a. 解压后将项目放到学校主机中并开启服务并获得端口。我使用的方法在terminal或者IDE进入项目文件夹后，
输入'python -m http.server'开启服务，默认8000端口。通过ifconfig获得主机IP地址
b. 使用有屏幕旋转功能的安卓手机进入和主机一样的网络中（学校内网，我调试时用家里的网关），输入
'http://主机IP：端口'进入主机界面，打开head_track_stereo/head_track_stereo.html后，移动手机镜头即可移动。
我调试时使用地址为“http://192.168.1.5:8000/head_track_stereo.html”，供参考

2. 项目使用Three.js库的方法和实现，通过6张图片建立3D Cubemap背景(Source：https://www.humus.name/Textures/Storforsen.zip)后，
使用StereoEffect.js内效果渲染透视。镜头控制主要使用Window.addEventListener("deviceorientation", handleOrientation)
监听手机陀螺仪变化，并通过handleOrientation方法获取变化的alpha, beta, gamma值（见：https://blog.csdn.net/a6713827/article/details/103265221），
后根据值改变透视镜头位置实现功能。

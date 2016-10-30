Requirements
python 3.4
pip  (python 3.4默认已安装 只需添加到环境变量)
numpy(opencv需要)
opencv_python


numpy安装：
安装pip之后 pip install numpy


opencv安装：
http://www.lfd.uci.edu/~gohlke/pythonlibs/
下载whl opencv_python-3.1.0-cp34-cp34m-win_amd64.whl 安装不了。。
把文件 改为 opencv_python-3.1.0-cp34-none-win_amd64.whl 就可以用pip 安装了。。
pip install opencv_python-3.1.0-cp34-none-win_amd64.whl


client.py
opencv调用客户端 摄像头 拍照并连接服务端 发送拍摄照片

server.py
监听端口
有访问 本地存储照片
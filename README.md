# WX_XiaoTianTian
微信小田田游戏点地鼠辅助
使用步骤
## python 环境
## 安装Python依赖aircv，opencv及其依赖
     pip install aircv
     pip install opencv-python
## Android 配置步骤
- 手机打开开发者模式，打开调试数据线连接电脑
- 打开android.py找到adb_path替换成你本机的android adk目录中{你的sdk路径}/platform-tools/adb
- 使用adb 命令截一张带有地鼠的图片（b.png 是从分辨率1080 × 1920截取的如果手机是这个分辨率可直接使用）
        
      adb shell screencap -p /sdcard/xxx.png

- 用图片剪裁工具剪切地鼠哪块的图片，参考b.png截法就行
- 把截好的图放到工程目录替换b.png
- 运行android.py

## IOS 配置步骤
- 部署WebDriverAgent https://testerhome.com/topics/7220

       成功安装后，浏览器访问 http://localhost:8100/status会看到一个json字符串
       
- 使用 http://localhost:8100/inspector 能拿到屏幕截图需要带地鼠的
- 用图片剪裁工具剪切地鼠哪块的图片，参考c.png截法就行 (c.png 是iPhone7 如果你是iPhone7 就直接使用)
- 把截好的图放到工程目录替换c.png
- 安装Python库（目前这个版本的库支持py2.7~3.5之间的版本）

      pip install --pre facebook-wda
      
- 运行ios.py



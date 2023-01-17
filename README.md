<div align="center">

[ProxyURL](https://github.com/239144498/ProxyURL)
-------------
[![Python version](https://img.shields.io/badge/python->=3.8-green.svg?style=plastic&logo=python)](https://www.python.org/downloads/release/python-380/)
[![GitHub stars](https://img.shields.io/github/stars/239144498/ProxyURL?color=brightgreen&style=plastic&logo=Apache%20Spark)](https://github.com/239144498/ProxyURL/stargazers)
[![MIT license](https://img.shields.io/badge/license-GNU3.0-green.svg?style=plastic&logo=React%20Hook%20Form)](https://github.com/239144498/ProxyURL/blob/main/LICENSE)

</div>

- 程序接口使用教程已发布在`微信公众号`，可打开微信访问：[https://0a.fit/obLUQ](https://0a.fit/obLUQ)，或者扫码查看

<a href="https://ik.imagekit.io/naihe/gzh/qrcode.png"><img src="https://ik.imagekit.io/naihe/gzh/qrcode.png" alt="qrcode.png" border="0" width="220px" height="220px" /></a>


目录
-------------------

- [程序介绍](#程序介绍)
- [程序功能](#程序功能)
- [Python部署](#Python部署)
    - [clone仓库](#clone仓库)
    - [安装依赖](#安装依赖)
    - [运行](#运行)
- [支持频道](#支持频道)
- [License](#License)

程序介绍
---
**ProxyURL**是一个从 [Streaming-Media-Server-Pro](https://github.com/239144498/Streaming-Media-Server-Pro) 项目中抽离出的流媒体代理程序。程序新增缓存功能，多人同时观看效果更流畅。
理论支持代理任意频道，代理后可解决**频道卡顿**问题、网页播放的**跨域**问题、**封锁地区**问题等等。


程序功能
---
- 代理任意电视频道的视频流
- 代理缓存播放
- 代理生成m3u文件
- 代理生成m3u8文件
- 异步下载流
- 流媒体转发
- 支持短回放
- 自定义频道列表

Python部署
---
> 💡提示：最好将本项目部署至美国地区的服务器，否则可能会出现奇怪的BUG。

推荐大家使用[Digitalocean](https://www.digitalocean.com/?refcode=b71d602787d2&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)的服务器，主要是因为免费。

<a href="https://www.digitalocean.com/?refcode=b71d602787d2&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg" alt="DigitalOcean Referral Badge" /></a>

使用我的邀请链接注册，你可以获得$200的credit，当你在上面消费$25时，我也可以获得$25的奖励。

我的邀请链接：

[https://m.do.co/c/9f72a27dec35](https://m.do.co/c/b71d602787d2)
> 根据以下通用命令部署本项目
### clone仓库

python版本>=3.8+

``` code
git clone https://github.com/239144498/ProxyURL.git
```

### 安装依赖

``` code
pip install -r requirements.txt
```

### 运行

``` code
python3 main.py
```

支持频道
---

- [x] 在channel.m3u文件添加代理频道

License
---
[GNU-3.0 © naihe](https://github.com/239144498/ProxyURL/blob/main/LICENSE)


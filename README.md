<div align="center">

[ProxyURL](https://github.com/239144498/ProxyURL)
-------------
[![Python version](https://img.shields.io/badge/python->=3.8-green.svg?style=plastic&logo=python)](https://www.python.org/downloads/release/python-380/)
[![GitHub stars](https://img.shields.io/github/stars/239144498/ProxyURL?color=brightgreen&style=plastic&logo=Apache%20Spark)](https://github.com/239144498/ProxyURL/stargazers)
[![MIT license](https://img.shields.io/badge/license-GNU3.0-green.svg?style=plastic&logo=React%20Hook%20Form)](https://github.com/239144498/ProxyURL/blob/main/LICENSE)

</div>

- 程序使用教程已发布在`微信公众号【pqhero】回复【使用教程】`，可打开微信访问：[https://0a.fit/obLUQ](https://0a.fit/obLUQ)，或者扫码查看

<a href="https://ik.imagekit.io/naihe/gzh/qrcode.png"><img src="https://ik.imagekit.io/naihe/gzh/qrcode.png" alt="qrcode.png" border="0" width="220px" height="220px" /></a>


程序介绍
---
> 🚨如需使用私有服务器运行本项目，请参考部署方式[部署教程](./README.md#python%E9%83%A8%E7%BD%B2linux)  
> 
**ProxyURL**是一个从 [Streaming-Media-Server-Pro](https://github.com/239144498/Streaming-Media-Server-Pro) 项目中抽离出的流媒体代理程序。程序新增缓存功能，多人同时观看效果更流畅。
理论支持代理任意频道，代理后可解决**频道卡顿**问题、网页播放的**跨域**问题、**封锁地区**问题等等。更多使用方式等你去发现。

代理接口演示
---
_[Click to view](https://ik.imagekit.io/naihe/github/demo.gif)_   
![loading...](https://github.com/239144498/ProxyURL/raw/main/img/demo.gif)


演示站点: 我很脆弱...请勿压测(·•᷄ࡇ•᷅ ）
---
API Document: https://proxy.naihe.me/docs
 为防止滥用，本接口已经加入了鉴权机制。  
**未来将添加代理4k频道接口**

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

支持代理的链接格式
---
> 💡提示：包含但不仅限于以下例子，如果遇到链接解析失败请开启一个新 [issue](https://github.com/239144498/ProxyURL/issues)

程序有检测url链接格式功能，一般m3u8链接分为以下两种：  

- 含有域名链接的数据
```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:1668994593
#EXTINF:10.0,5290508
http://117.169.xxx.xxx:8080/wh7f454c46tw3004853380_1728812826/live/cctv-4/HD-4000k-1080P-cctv4_20230117_205041_205051.ts
#EXTINF:10.0,5306864
http://117.169.xxx.xxx:8080/wh7f454c46tw3004853380_1728812826/live/cctv-4/HD-4000k-1080P-cctv4_20230117_205051_205101.ts
#EXTINF:10.0,5271708
http://117.169.xxx.xxx:8080/wh7f454c46tw3004853380_1728812826/live/cctv-4/HD-4000k-1080P-cctv4_20230117_205101_205111.ts
...
...
```
- 无域名链接的数据

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:167395846
#EXT-X-TARGETDURATION:10
#EXTINF:10.200,
/cntv20210928/cctvwbnd/cctv1_2_md/167395846.ts?region=beijing
#EXTINF:9.800,
/cntv20210928/cctvwbnd/cctv1_2_md/167395847.ts?region=beijing
#EXTINF:10.200,
/cntv20210928/cctvwbnd/cctv1_2_md/167395848.ts?region=beijing
#EXTINF:9.800,
/cntv20210928/cctvwbnd/cctv1_2_md/167395849.ts?region=beijing
```
这两种格式已涵盖市面上大部分m3u8链接。


Python部署（Linux）
---
> 💡提示：最好将本项目部署至美国地区的服务器，否则可能会出现奇怪的BUG。

推荐大家使用[Digitalocean](https://www.digitalocean.com/?refcode=b71d602787d2&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)的服务器，主要是因为**免费**。

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

项目使用教程
---
关注公众号【pqhero】查看程序使用详情  
<a href="https://ik.imagekit.io/naihe/gzh/qrcode.png"><img src="https://ik.imagekit.io/naihe/gzh/qrcode.png" alt="qrcode.png" border="0" width="220px" height="220px" /></a>


支持频道
---

- [x] 在channel.m3u文件添加代理频道

License
---
[GNU-3.0 © naihe](https://github.com/239144498/ProxyURL/blob/main/LICENSE)


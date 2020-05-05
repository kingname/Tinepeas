## Tinepeas——豌豆尖

这个框架我命名为 Tinepeas，中文名叫做豌豆尖。以表达我对杭州吃不到豌豆尖的遗憾之情和对豌豆尖的想念。

Tinepeas 的数据流如下图所示：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2020-05-05-15-11-50.png)

基于 Scrapy 的数据流，我们省略了 Downloader Middleware、Spider Middleware 和 Pipeline，仅保留核心的爬虫定义、调度和网络请求。

Scrapy 基于 Twisted实现异步请求，而Tinepeas使用Asyncio 和 aiohttp 实现异步请求。

项目还在开发中，请勿用于生产环境。

关于本项目的设计原理，请阅读我的公众号文章：

[从零开发一个爬虫框架——Tinepeas](https://mp.weixin.qq.com/s/JtYG20d-dGYsOvh4juHpvg)

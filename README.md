# AdaoIMGdownloader
##A岛串内图片批量下载脚本
使用方法：
终端运行  
  python AdaoIMGdownloader.py [串ID] [0或1；0为匿名岛，1为备胎岛]  
如  
  python AdaoIMGdownloader.py 6035851 0

使用备注：

* 目前只在OSX平台下测试通过
* 请通过命令行运行
* 运行命令`python AdaoIMGdownloader.py 串ID`
* 脚本依赖requests来进行请求，所以请确认安装了[requests](http://docs.python-requests.org/en/latest/user/install/#install)
* 目前是调用wget下载的，所以请确认已经安装了wget
* 保存路径需要自行编辑脚本`path`变量


更新日志：
2015年05月07日 同时支持匿名岛和备胎岛，并增加2岛切换参数，实现不下载已存在的同名文件

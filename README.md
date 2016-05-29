使用步骤
=========

运行前的准备：
--------------
* 安装virtualenv 虚拟环境
    apt-get install virtualenv
* 安装Flask
    apt-get install Flask
* 导入Flask必需的插件
    pip install -r requirements.txt
* 安装测试RESTful API工具
    pip install httpie

配置
-------------------
（示例代码中已经包含了data-dev.sqlite数据库文件）
初始化数据库迁移脚本
python manage.py db init

创建数据库，类似于db.create_all()，以后每一次更新数据模型，都要运行
python manage.py db migrate -m "init migration"

把更新后的数据模型应用到数据库
python manage.py db upgrade

运行网站
python manage.py runserver


RESTful API测试
-----------------
发起GET请求
    http --json GET http://localhost:5000/api/v1.0/posts/
或
    http --json --auth : GET  http://localhost:5000/api/v1.0/posts/
返回
    {
        "author": "http://localhost:5000/api/v1.0/users/1",
        "body": "hello world",
        "timestamp": "Sun, 22 Dec2015 09:23:56 GMT",
        "url": "http://localhost:5000/api/v1.0/posts/23"
    }
    
发起POST请求
    http --json --auth <email>:<password> GET  http://localhost:5000/api/v1.0/posts/
    
获取认证令牌
    http --json --auth <email>:<password> GET  http://localhost:5000/api/v1.0/token
返回
    {
        "expiration":36000,
        "token": "exkfjsljdfis..."
    }
    
使用认证令牌
    http --json --auth exkfjsljdfis...: GET http://localhost:5000/api/v1.0/posts/
返回：
    {
        "next_page": "http://localhost:5000/api/v1.0/posts/?page=2",
        "prev_page": null,
        "page_count": 20,
        "total_count": 109
        "posts": [
            {
                "author": "http://localhost:5000/api/v1.0/users/1",
                "body": "Hi, this is my first tweet.",
                "body_html": null,
                "timestamp": "Mon, 09 May 2016 13:48:52 GMT",
                "url": "http://localhost:5000/api/v1.0/posts/1"
            },
            {
                "author": "http://localhost:5000/api/v1.0/users/1",
                "body": "this is my second tweet",
                "body_html": null,
                "timestamp": "Mon, 09 May 2016 13:49:12 GMT",
                "url": "http://localhost:5000/api/v1.0/posts/2"
            },
            ....
        ]
    }

测试
=============

代码覆盖率
-----------
    pip install coverage

    
自动化测试
--------------
Flask内建的测试客户端编写单元测试框架
    test_client
Selenium进行端到端测试
    pip install selenium
    

测试用户
----------
用户名 john@example.com 密码 cat
用户名 sam@example.com 密码 sam
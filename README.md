## 基于Bert的简单问答原型

### 本地测试

1. 启动环境
```
make
qa_demo/gotalk/gotalk .
cd src
python3 dispatcher.py 1
uwsgi --http 127.0.0.1:8000  --wsgi-file qa.py --check-static ../
```

2. 在浏览器中打开 ```http://127.0.0.1:8000/static/qa_test.html```

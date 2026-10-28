Buổi 06: FASTAPI

- Cài đặt

```
pip install "fastapi[standard]"
```

- Định nghĩa
  VD tạo file: main.py

```
from fastapi import FastAPI()
app = FastAPI()

@app.get("/")
def hello():
    return "hello"
```

- Chạy

```
fastapi dev
fastapi dev main.py
```

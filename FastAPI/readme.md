## **Introduction**


[FastAPI](https://fastapi.tiangolo.com/) is a modern Python web framework which with a number of advantages, including:

* It is one of the fastest (high-performance) web frameworks available.
* It takes advantage of type annotation support of Python 3.6+ for better data validation and editor support.
* It utilizes Python's Async power, which is useful for building asynchronous APIs.
* It generates standards based on open standards such as OpenAPI and JSON Schema.
* It is robust and easy to use and learn.
* So in this guide, you will be exploring one of the newest and finest Python web framework libraries.


There are just three basic steps to install, create, and run FastAPI.

**Installation**

```bash 
pip install fastapi
pip install uvicorn
```

**Create your App**

To see what the simplest FastAPI app could look like, create a new Python file called `main.py`

```bash 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}
```


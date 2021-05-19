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

**Run your App**
To run the app, just execute like this :

```bash 
uvicorn main:app --reload
```

After running the above command, the server starts as follows:

```bash 
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL
+C to quit)
INFO:     Started reloader process [4136] using
statreload
INFO:     Started server process [12988]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Diving Deeper**
*Path Parameters*
You can declare parameters to the API call as variables as a function parameter. Here , I have used course_id as the parameter. Note that the type of the parameter is int.

```bash 
@app.get("/course/{course_id}")
def my_course(course_id: int):
    return {"course_id": course_id}
    ```
    



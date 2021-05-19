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
You can declare parameters to the API call as variables as a function parameter. Here , I have used `course_id` as the parameter. Note that the type of the parameter is `int`.

```bash 
@app.get("/course/{course_id}")
def my_course(course_id: int):
    return {"course_id": course_id}
```
    
If you provide the URL incorrectly, say for `course/100s`, you will get the following validation error.

```bash 
{
    "detail": [
        {
            "loc": [
                "path",
                "course_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```
And if you run the example for a URL such as `course/100`, the call will get this response:

```bash 
{"course_id":100}
```

**Query Parameters**
The other way of providing parameters to API calls is by providing them as query parameters. For example: /my/page/items/?page=1&limit=10&order=0.

Here's how you can implement the function in FastAPI.

```bash 
dummy_data = [i for i in range(100)]

@app.get("/my/page/items/")
async def read_item(page: int = 0, limit: int = 0, skip: int = 1):
    return dummy_data[page*10: page*10 + limit: skip]
```

In the above example, there are three parameters set. So for a URL such as http://127.0.0.1:8000/my/page/items/?page=2&limit=29&skip=2, the parameters will be:

page(int): 2
limit(int): 29
skip(int): 2
So the response of the above URL will be:

`[20,22,24,26,28,30,32,34,36,38,40,42,44,46,48]`

**Request Body**
When you need to send data from the client to the server, you can use the request body.

Note: To send data using the request body, use the `POST` method. You cannot use the `GET` method in the request body.

To declare a request body, use Pydantic models and declare the request body as:
```bash
from pydantic import BaseModel

class MyItem(BaseModel):
    name: str
    info: str = None
    price: float
    qty: int

@app.post("/purchase/item/")
async def create_item(item: MyItem):
    return {"amount": item.qty*100, "success": True}
```

In the above example, I have created a model named MyItem which has certain attributes. Now when there is a `POST` request on endpoint `/purchase/item/`, it will capture the attribute values and return with success.

Let's test this API call using `CURL`.

```bash 
curl -X POST "http://127.0.0.1:8000/purchase/item/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":\"sample item\",\"info\":\"This is info for the item\",\"price\":40,\"qty\":2}"
```

It will give the response:

`{"amount":200,"success":true}`

**Form Data**

In many scenarios, you may need to receive form fields instead of JSON. In such cases, Form comes to the rescue. The way that HTML forms (<form></form>) sends data is different from JSON, but FastAPI ensures correct parsing of the data.

To use form data, first install the additional library python-multipart.

```bash 
pip install python-multipart
```

For this demo, I have created a login view, that takes username and password as form fields.

```bash 
from fastapi import Form

@app.post("/accounts/login/")
async def login_view(username: str = Form(...), password: str = Form(...)):
    return {"success": True}
```

Automatic Docs
FastAPI comes with a battery included for automated API documentation in a nice and beautiful web user interface. Two default automatic docs come with fastAPI.

[Swagger UI](https://github.com/swagger-api/swagger-ui)
This is an interactive exploration of your API calls. Here, you can view and test your API calls in a nice, user-friendly interface. Read more [here](https://github.com/swagger-api/swagger-ui) .




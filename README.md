# Simple_API_Example
A minimal example demonstrating how to build a simple API featuring a **server** and **client** using **FastAPI**, in the context of delivering goods from New Jersey to New York.

## Video Tutorial 🎥
<a href="" target="_blank"><img width="600" alt="API with FastAPI thumbnail" src="https://github.com/user-attachments/assets/5ed594f6-943d-4700-aee8-b6861e9ec12e" /></a>

## Overview 📚

This repository contains a small FastAPI-based server that simulates a simple delivery endpoint—sending goods from New Jersey to New York - and a client script to interact with it.

It is intended as a hands-on demonstration of building and consuming RESTful APIs using FastAPI.

## Installation and Set Up ⚙️

1. Clone this repository on your local system, and navigate to project folder:
```
git clone https://github.com/MariyaSha/Simple_API_Example.git
cd Simple_API_Example
```

2. Create a virtual environment and install dependencies (conda + WSL example):
```
conda create -n api_env python=3.12
conda activate api_env
pip install -r requirements.txt
```

3. In one instance of WSL terminal, run the server with:
```
uvicorn nj_server:app --reload
```

4. Your server will now be available on port 8000 in your browser. 
<br>
Navigate to `localhost:8000/docs` to interact with your API's backend.
<br>
Or navigate directly to an endpoint like: 
<br>
`http://127.0.0.1:8000/warehouse/tomatoes?order_qty=30`

5. While the server is running, you can use my custom client to interact with the server more conveniently.
<br>
Open an additional instance of WSL (open another WSL terminal next to the existing one), and run the client with:
<br>
`uvicorn ny_client:app --reload --port 8001`

6. Your client will now be available on port 8001 in your browser.
<br>
Navigate to `localhost:8001` to interact with your client and server.

7. Once you understand how the simple implemintation works, I highly recomend to check out `nj_advanced_server.py` to see a more professional approach (using pydantic)

## Dependencies 💻
- **FastAPI** — for building the API.
- **Uvicorn** — ASGI server to run the app.
- HTTP client libraries used in `ny_client.py`: 
    - requests
    - jinja2
    - python-multipart
    - pydantic (automatically installed with fastapi)
    
## License 📜

This project is licensed under [MIT License](LICENSE). Feel free to use it for experimentation or learning.

## Contact ☎️

Created by **Mariya Sha** as part of a "Create Basic API" tutorial.  
<br>
Follow my tutorials and projects:
- [YouTube – Python Simplified](https://www.youtube.com/PythonSimplified)  
- [LinkedIn - Mariya Sha](https://www.linkedin.com/in/mariyasha888)
- [X - Mariya Sha](https://x.com/MariyaSha888)


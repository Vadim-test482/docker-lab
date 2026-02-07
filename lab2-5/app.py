import os
from flask import Flask

app = Flask(__name__)
LOG_DIR = os.getenv("LOG_DIR", "/app/logs")

@app.get("/")
def home():
    return {"msg": "non-root demo", "uid": os.getuid(), "gid": os.getgid()}

@app.get("/write")
def write():
    os.makedirs(LOG_DIR, exist_ok=True)
    p = os.path.join(LOG_DIR, "app.log")
    with open(p, "a", encoding="utf-8") as f:
        f.write("log line\n")
    return {"written_to": p}

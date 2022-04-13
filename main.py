import os
import logging
import subprocess

from flask import Flask

app = Flask(__name__)

@app.route("/")
def return_main():
    result = exec_embulk()
    return result

def exec_embulk():
        res = subprocess.run("embulk -v", shell=True, check=True, capture_output=True, text=True)
        result = res.stdout
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
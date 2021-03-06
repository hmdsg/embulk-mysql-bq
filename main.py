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
    try:
        cmd = "embulk --version"
        res = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        result = res.stdout
    except subprocess.CalledProcessError as e:
        print(e.cmd)
        print(e.returncode)
        print(e.output)
        print(e.stdout)
        print(e.stderr)
        result = e.stdout

    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
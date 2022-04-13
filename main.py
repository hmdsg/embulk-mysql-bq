import os
import subprocess

from flask import Flask

app = Flask(__name__)

@app.route("/")
def exec_embulk():
    try:
        # 実行したいembulkコマンドを記述
        res = subprocess.run(["embulk", "-v"], check=True, capture_output=True, text=True)
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
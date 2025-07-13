from flask import Flask, jsonify, render_template
from sim.sim_runner import run_simulation

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start():
    result = run_simulation()
    return jsonify(result)

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
       app.run(host="0.0.0.0", port=5000, debug=True)
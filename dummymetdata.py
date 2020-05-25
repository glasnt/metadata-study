from flask import Flask, jsonify

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    if "error" in path:
        print("ERROR")
        return Response("", status=500)


    return jsonify(path=path)


if __name__ == "__main__":
    app.run()

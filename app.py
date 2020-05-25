import httpx
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Override metadata server with local server, specifying port
local = os.environ.get("LOCAL")
if local:
    METADATA_URI = f"http://localhost:{local}/"
else:
    METADATA_URI = "http://metadata.google.internal/"


def uri(q):
    # While "//" queries are resilient, it looks strange in URIs
    if q[0] == "/":
        q = q[1:]

    return METADATA_URI + q


def query(q):
    # MS allows returning service token. Let's stop that.
    bad_queries = ["token", "service-accounts"]
    for x in bad_queries:
        if x in q:
            return False, "Operation Not Permitted"

    r = httpx.get(uri(q), headers={"Metadata-Flavor": "Google"})

    # Reduce http status codes to a "success" boolean, for later css.
    success = True if r.status_code == 200 else False
    text = r.text if success else "Error"

    return success, text


def queryblock(title=None, q=""):
    if title:
        title = f"<h3>{title}</h3>"
    else:
        title = ""
    success, resp = query(q)
    if not success:
        resp = f"<span class='failure'>{resp}</span>"
    return f"{title}<pre><code>&gt; GET {uri(q)}<br><br>{resp}</code></pre>"

# required so "queryblock" can be invoked within template
app.jinja_env.globals.update(queryblock=queryblock)


@app.route("/")
def main():
    query = request.args.get("q")
    return render_template("base.html", query=query)


if __name__ == "__main__":
    print(main)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

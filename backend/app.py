from flask import Flask, request, jsonify, send_from_directory
import urllib.parse

app = Flask(__name__, static_folder="../frontend")

@app.route("/search", methods=["POST"])
def search():
    data = request.json
    query = data.get("query")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    # Create Google Shopping search URL
    google_url = "https://www.google.com/search?tbm=shop&q=" + urllib.parse.quote(query)
    return jsonify({"results": [
        {
            "title": f"Google Shopping results for \"{query}\"",
            "url": google_url,
            "price": None,
            "snippet": "Click to view product prices from many stores."
        }
    ]})

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)

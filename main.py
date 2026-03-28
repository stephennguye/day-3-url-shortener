from shortener import URLShortener
from flask import Flask, render_template, request

app = Flask(__name__)
shortener = URLShortener()

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        original_url = request.form["url"]
        short_url = shortener.shorten_url(original_url)
        return render_template("ui.html", new_url=short_url, old_url=original_url)
    else:
        return render_template("ui.html")
    
if __name__ == "__main__":
    app.run(debug=True)

    
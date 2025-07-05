from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def translate():
    translated_text = ""
    source_lang = ""
    if request.method == "POST":
        text = request.form["text"]
        dest_lang = request.form["dest_lang"]
        result = translator.translate(text, dest=dest_lang)
        translated_text = result.text
        source_lang = result.src
    return render_template("index.html", translated_text=translated_text, languages=LANGUAGES, source_lang=source_lang)

if __name__ == "__main__":
    app.run(debug=True)

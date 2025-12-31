from flask import Flask, request, send_file
import louis
import io

app = Flask(__name__)

@app.route("/brf", methods=["POST"])
def brf():
    texte = request.json.get("texte", "")

    table = "fr-bfu-g1.ctb"
    braille = louis.translateString(table, texte)

    # créer un fichier en mémoire
    fichier = io.BytesIO()
    fichier.write(braille.encode("ascii", errors="ignore"))
    fichier.seek(0)

    return send_file(
        fichier,
        mimetype="text/plain",
        as_attachment=True,
        download_name="texte.brf"
    )

@app.route("/")
def main():
    return "Hey dude"

app.run(host="0.0.0.0", port=10000)

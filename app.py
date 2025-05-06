from flask import Flask, request, jsonify
from docx import Document
import os

app = Flask(__name__)

@app.route("/extract", methods=["POST"])
def extract_text_from_docx():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    if not file.filename.endswith(".docx"):
        return jsonify({"error": "Invalid file type. Only .docx allowed."}), 400

    try:
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def health_check():
    return "API up and running"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

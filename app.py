from flask import Flask, request, jsonify
from docx import Document
import base64
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Serviço de extração de texto .docx ativo."})

@app.route("/extract-text", methods=["POST"])
def extract_text():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado."}), 400

    file = request.files["file"]
    if not file.filename.endswith(".docx"):
        return jsonify({"error": "Apenas arquivos .docx são permitidos."}), 400

    try:
        document = Document(file)
        full_text = "\n".join([para.text for para in document.paragraphs])
        return jsonify({"text": full_text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
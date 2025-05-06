from flask import Flask, request, jsonify
from docx import Document
import os

app = Flask(__name__)

@app.route("/extract", methods=["POST"])
def extract_text_from_docx():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo foi enviado"}), 400

    file = request.files['file']

    if not file.filename.lower().endswith(".docx"):
        return jsonify({"error": "Tipo de arquivo inválido. Apenas .docx é permitido."}), 400

    try:
        document = Document(file)
        full_text = "\n".join([para.text for para in document.paragraphs])
        return jsonify({"text": full_text})
    except Exception as e:
        return jsonify({"error": f"Erro ao processar o arquivo: {str(e)}"}), 500

@app.route("/", methods=["GET"])
def health_check():
    return "✅ API DOCX Extractor está ativa."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

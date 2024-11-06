from flask import Flask, request
from langchain_community.llms import Ollama
import os

app = Flask(__name__)


cached_llm = Ollama(model="llama3")


@app.route("/ia", methods=["POST"])
def iaPost():
    json_content = request.json
    query = json_content.get("query")
    
    print(f"Query: {query}")
    
    response = cached_llm.invoke(query)
    
    print(response)
    
    request_answaer = {"answer": response}
    return request_answaer

@app.route("/pdf", methods=["POST"])
def pdfPost():
    file = request.files["file"]
    file_name = file.filename
    save_dir = "pdf"
    save_file = os.path.join(save_dir, file_name)
    
    # Cria o diretório se ele não existir
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    file.save(save_file)
    print(f"filename: {file_name}")
    
    response = {"status": "Sucessfully Uploaded", "filename": file_name}
    return response
    

def star_app():
    app.run(host = "0.0.0.0", port=8080, debug=True)
    

if __name__ == "__main__":
    star_app()
 
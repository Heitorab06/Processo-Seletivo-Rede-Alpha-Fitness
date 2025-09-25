from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS
    
app = Flask(__name__)
CORS(app)


email_regex = r"[a-zA-Z0-9.záàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ]+@.+$"  
numero_regex = r"\++[0-9]{13}"
cpf_regex = r"[0-9]{11}"



urlalpha = "https://docs.google.com/spreadsheets/d/1OO7gDKXv4YJiDfpfrIHaXIa_XUgDhl3rG2FQImQ-ixY/export?format=csv"

@app.route("/dados", methods=["GET"])
def get_dados():
    try:
        dataframe = pd.read_csv(urlalpha, dtype={"cpf": str, "numero": str})
        dataframe = dataframe.dropna()  #remove linhas com valores nulos
        dataframe = dataframe[          #mantem apenas valores consistentes 
            dataframe["email"].str.fullmatch(email_regex)   
            & dataframe["numero"].str.fullmatch(numero_regex)   
            & dataframe["cpf"].str.fullmatch(cpf_regex)   
        ]    
        
        return jsonify(dataframe.to_dict(orient='records'))     #retorna dataframe filtrado para quem requisitou, em formato adequado (jsonify)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

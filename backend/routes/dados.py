from flask import Blueprint, jsonify
from services.tabela import carregar_dados

dados_bp = Blueprint("dados", __name__)

@dados_bp.route("/dados", methods=["GET"])
def get_dados():
    try:
        dataframe = carregar_dados()
        return jsonify(dataframe.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

# Habilitar CORS
CORS(app)

@app.route('/buscar_operadora', methods=['GET'])
def buscar_operadora_por_ans():
    # Pega o código ANS da query string
    registro_ans = request.args.get('registro_ans')

    if not registro_ans:
        return jsonify({"erro": "O código ANS é obrigatório"}), 400

    try:
        # Carregar o CSV
        df = pd.read_csv('Relatorio_cadop.csv', sep=';', encoding='utf-8', on_bad_lines='skip')

        # Garantir que a coluna de registro ANS seja tratada como string
        df['Registro_ANS'] = df['Registro_ANS'].astype(str)

        # Filtrar pelo número de registro ANS
        resultado = df[df['Registro_ANS'] == str(registro_ans)]

        # Verificar se encontrou resultados
        if resultado.empty:
            return jsonify({"erro": "Registro ANS não encontrado"}), 404

        # Converter o resultado para JSON
        resultado_dict = resultado.to_dict(orient='records')
        return jsonify(resultado_dict), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    # Rodar no host 0.0.0.0 e na porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

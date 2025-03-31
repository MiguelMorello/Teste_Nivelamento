from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)


CORS(app)

@app.route('/buscar_operadora', methods=['GET'])
def buscar_operadora_por_ans():
    
    registro_ans = request.args.get('registro_ans')

    if not registro_ans:
        return jsonify({"erro": "O código ANS é obrigatório"}), 400

    try:
        
        df = pd.read_csv('Relatorio_cadop.csv', sep=';', encoding='utf-8', on_bad_lines='skip')

        df['Registro_ANS'] = df['Registro_ANS'].astype(str)
        
        resultado = df[df['Registro_ANS'] == str(registro_ans)]

        if resultado.empty:
            return jsonify({"erro": "Registro ANS não encontrado"}), 404
      
        resultado_dict = resultado.to_dict(orient='records')
        return jsonify(resultado_dict), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

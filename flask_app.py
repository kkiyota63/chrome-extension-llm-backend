from flask import Flask, request, jsonify
from flask_cors import CORS  
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # 環境変数を読み込む

app = Flask(__name__)
CORS(app)  # 全てのオリジンからのリクエストを許可

# APIキーを設定
genai.configure(api_key=os.environ['API_KEY'])

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # モデルを使ってテキストを生成
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    # response の内容を確認
    # print(response)

    # response.parts を使ってテキストを結合
    summary = ''.join(part.text for part in response.parts)

    return jsonify({'text': summary})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

HUGGING_FACE_API_KEY = "your_hugging_face_api_key"
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"

def generate_bio_with_llama(career, personality, interests, goals):
    prompt = (f"Generate a creative and appealing bio based on the following details:\n"
              f"Career: {career}\n"
              f"Personality: {personality}\n"
              f"Interests: {interests}\n"
              f"Relationship Goals: {goals}\n")

    headers = {
        "Authorization": f"Bearer {HUGGING_FACE_API_KEY}",
        "Content-Type": "application/json"  # Ensure correct Content-Type
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.7
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()
        return "Bio generation failed due to unexpected response format."
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return "Error generating bio."

@app.route('/generate_bio', methods=['POST'])
def generate_bio():
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.json
    career = data.get('career', '')
    personality = data.get('personality', '')
    interests = data.get('interests', '')
    goals = data.get('goals', '')

    bio = generate_bio_with_llama(career, personality, interests, goals)
    return jsonify({"bio": bio})

if __name__ == '__main__':
    app.run(debug=True)

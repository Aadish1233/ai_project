from flask import Flask, request, jsonify, render_template
import requests

# Initialize Flask App
app = Flask(__name__)

# Configure Hugging Face API
HUGGING_FACE_API_KEY = "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"
MODEL_ID = "meta-llama/Llama-2-7b-chat-hf"  # Example Llama model

def generate_bio_with_llama(career, personality, interests, goals):
    prompt = (f"Generate a creative and appealing bio for a user based on the following details:\n"
              f"Career: {career}\n"
              f"Personality: {personality}\n"
              f"Interests: {interests}\n"
              f"Relationship Goals: {goals}\n"
              f"Make it friendly and engaging.")

    headers = {
        "Authorization": f"Bearer {HUGGING_FACE_API_KEY}"
    }
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100, "temperature": 0.7}
    }

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{MODEL_ID}",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        result = response.json()
        bio = result[0]['generated_text']
        return bio.strip()
    else:
        return "Error generating bio."

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# API Endpoint for Bio Generation
@app.route('/generate_bio', methods=['GET','POST'])
def generate_bio():
    data = request.json
    career = data.get('career', '')
    personality = data.get('personality', '')
    interests = data.get('interests', '')
    goals = data.get('goals', '')

    try:
        bio = generate_bio_with_llama(career, personality, interests, goals)
        return jsonify({"bio": bio})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

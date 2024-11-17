from flask import Flask, request, jsonify, render_template
import openai

# Initialize Flask App
app = Flask(__name__)

# Configure OpenAI API
openai.api_key = "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"


# Home Route
@app.route('/')
def home():
    return render_template('index.html')


# API Endpoint for Bio Generation
@app.route('/generate_bio', methods=['POST'])
def generate_bio():
    data = request.json
    career = data.get('career', '')
    personality = data.get('personality', '')
    interests = data.get('interests', '')
    goals = data.get('goals', '')

    # Create prompt for AI model
    prompt = (f"Generate a creative and appealing bio for a user based on the following details:\n"
              f"Career: {career}\n"
              f"Personality: {personality}\n"
              f"Interests: {interests}\n"
              f"Relationship Goals: {goals}\n"
              f"Make it friendly and engaging.")

    # Generate response from OpenAI
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        bio = response.choices[0].text.strip()
        return jsonify({"bio": bio})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

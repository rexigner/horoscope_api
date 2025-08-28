from flask import Flask, request, jsonify

app = Flask(__name__)

# Static horoscope data for each sign
horoscopes = {
    'aries': "Today is a great day to start something new.",
    'taurus': "Patience and persistence will pay off.",
    'gemini': "Communication is key; speak your mind.",
    'cancer': "Focus on your family and home today.",
    'leo': "Your confidence will attract positive attention.",
    'virgo': "Pay attention to details and stay organized.",
    'libra': "Balance your work and personal life carefully.",
    'scorpio': "Trust your intuition to guide you.",
    'sagittarius': "Adventure and learning are on the horizon.",
    'capricorn': "Hard work leads to success.",
    'aquarius': "Innovate and think outside the box.",
    'pisces': "Creativity will inspire you today."
}


@app.route('/horoscope', methods=['GET'])
def get_horoscope():
    sign = request.args.get('sign', '').lower()
    if sign in horoscopes:
        return jsonify({'sign': sign, 'horoscope': horoscopes[sign]})
    else:
        return jsonify({'error': 'Invalid zodiac sign'}), 400


if __name__ == '__main__':
    app.run(port=5000)

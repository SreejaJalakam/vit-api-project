from flask import Flask, request, jsonify
from flask_cors import CORS
import re
from datetime import datetime

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.get_json()
        input_array = data.get('data', [])

        if not isinstance(input_array, list):
            return jsonify({"is_success": False, "error": "Input 'data' must be an array."}), 400

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        sum_of_numbers = 0
        concat_string_list = []

        for item in input_array:
            if isinstance(item, str):
                if item.isdigit():
                    num = int(item)
                    if num % 2 == 0:
                        even_numbers.append(item)
                    else:
                        odd_numbers.append(item)
                    sum_of_numbers += num
                elif item.isalpha():
                    alphabets.append(item.upper())
                    concat_string_list.append(item)
                else:
                    special_characters.append(item)
            # Ignoring non-string inputs as per example, or handle as error if needed

        # Concatenation of all alphabetical characters in reverse order in alternating caps
        concat_string = ""
        concat_string_list.reverse()
        for i, char in enumerate(concat_string_list):
            if i % 2 == 0:
                concat_string += char.upper()
            else:
                concat_string += char.lower()

        # User ID format: {full_name_ddmmyyyy}
        full_name = "sreeja_santhosh" # Replace with actual full name
        dob = "29082025" # Replace with actual DDMMYYYY
        user_id = f"{full_name}_{dob}"

        # Hardcoded email and roll number as per example
        email = "sreeja@example.com" # Replace with actual email
        roll_number = "21BCE1400" # Replace with actual roll number

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(sum_of_numbers),
            "concat_string": concat_string
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

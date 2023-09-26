import os
from flask import Flask, request, jsonify
from operations import calculate_sum, calculate_sub, calculate_mult, calculate_div, calculate_word_count_from_file, calculate_average_from_csv

app = Flask(__name__)

@app.route('/operations', methods=['GET'])
def perform_all_operations():
    try:
        num1 = float(request.args.get('x'))
        num2 = float(request.args.get('y'))
        result_sum = calculate_sum(num1, num2)
        result_sub = calculate_sub(num1, num2)
        result_mult = calculate_mult(num1, num2)
        result_div = calculate_div(num1, num2)
        return jsonify({
            'sum': result_sum,
            'subtraction': result_sub,
            'multiplication': result_mult,
            'division': result_div
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
@app.route('/words', methods=['GET'])
def calculate_word_count():
    try:
        file = request.files['file']
        file_path = 'temp.txt'
        file.save(file_path)
        word_count = calculate_word_count_from_file(file_path)
        os.remove(file_path)
        return jsonify({'word_count': word_count}), 200
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/average', methods=['GET'])
def calculate_average():
    try:
        col = str(request.args.get('col'))
        file = request.files['file']
        file_path = 'temp.csv'
        file.save(file_path)
        average = calculate_average_from_csv(file_path,col)
        os.remove(file_path)
        return jsonify({'average': average}), 200
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
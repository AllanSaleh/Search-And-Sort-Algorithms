from flask import Flask, request, jsonify

# www.127.0.0.1:5000/search_name?name=Allan&age=99

app = Flask(__name__)

@app.route('/search_name', methods=['GET'])
def search_name():
    name = request.args.get('name')
    age = request.args.get('age')
    print(name, age)
    return jsonify('success'), 200

if __name__ == '__main__':
    app.run(debug=True)

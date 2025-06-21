from flask import Flask, request, jsonify
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()


@app.route("/add", methods=["POST"])
def add():
    """Add two numbers."""
    data = request.get_json()
    try:
        a = float(data["a"])
        b = float(data["b"])
        result = calc.add(a, b)
        return jsonify({"result": result})
    except (KeyError, ValueError) as e:
        return (
            jsonify({"error": "Invalid input, please provide two numbers (a, b)"}),
            400,
        )


@app.route("/subtract", methods=["POST"])
def subtract():
    """Subtract b from a."""
    data = request.get_json()
    try:
        a = float(data["a"])
        b = float(data["b"])
        result = calc.subtract(a, b)
        return jsonify({"result": result})
    except (KeyError, ValueError) as e:
        return (
            jsonify({"error": "Invalid input, please provide two numbers (a, b)"}),
            400,
        )


@app.route("/multiply", methods=["POST"])
def multiply():
    """Multiply two numbers."""
    data = request.get_json()
    try:
        a = float(data["a"])
        b = float(data["b"])
        result = calc.multiply(a, b)
        return jsonify({"result": result})
    except (KeyError, ValueError) as e:
        return (
            jsonify({"error": "Invalid input, please provide two numbers (a, b)"}),
            400,
        )


@app.route("/divide", methods=["POST"])
def divide():
    """Divide a by b."""
    data = request.get_json()
    try:
        a = float(data["a"])
        b = float(data["b"])
        result = calc.divide(a, b)
        return jsonify({"result": result})
    except (KeyError, ValueError) as e:
        return (
            jsonify({"error": "Invalid input, please provide two numbers (a, b)"}),
            400,
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

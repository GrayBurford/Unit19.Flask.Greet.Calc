# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def do_addition():
    """Adds query string a & b values"""
    print(request.args)
    # Python turns everything into a string
    # convert to int, evaluate, then convert back to str
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))

    # Alternate:
    # a = int(request.args.get("a"))
    # b = int(request.args.get("b"))
    # result = add(a, b)
    # return str(result)

@app.route("/sub")
def do_subtraction():
    """Subtracts query string a & b values"""
    print(request.args)
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))

@app.route("/mult")
def do_multiplication():
    """Multiplies query string a & b values"""
    print(request.args)
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))

@app.route("/div")
def do_division():
    """Divides query string a & b values"""
    print(request.args)
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))

@app.route("/math/<function>")
def do_math_function(function):
    all_functions = {
        "add" : add,
        "sub" : sub,
        "mult" : mult,
        "div" : div
    }

    print(request.args)
    a = int(request.args["a"])
    b = int(request.args["b"])

    answer = all_functions[function](a, b)

    return str(answer)
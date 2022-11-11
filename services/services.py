from flask import Flask, request, jsonify
from loko_extensions.business.decorators import extract_value_args
from loko_extensions.model.components import Component, save_extensions
from transformers import pipeline

app = Flask("")
a = Component(name="hf")

generator = pipeline(task="text-generation")

save_extensions([a])


@app.route("/", methods=["POST"])
@extract_value_args(_request=request)
def test(value, args):
    return jsonify(generator(value))


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)

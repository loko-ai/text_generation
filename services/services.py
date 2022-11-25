from flask import Flask, request, jsonify
from loko_extensions.business.decorators import extract_value_args
from transformers import pipeline
from utils.logger_utils import logger

app = Flask("")

generator = pipeline(task="text-generation")


@app.route("/", methods=["POST"])
@extract_value_args(_request=request)
def test(value, args):
    logger.debug(f"args::: {args}")
    max_length = int(args.get("max_length")) if args.get("max_length") else None
    ngram_size = int(args.get("ngram_size")) if args.get("ngram_size", None) else None
    do_sample = args.get("do_sample", False)
    temperature = float(args.get("temperature", 0.7)) if args.get("temperature", 0.7) else None
    return jsonify(generator(value, max_length=max_length, no_repeat_ngram_size=ngram_size, do_sample=do_sample, temperature=temperature))


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)

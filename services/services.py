from fastapi import Request, FastAPI, File
from loguru import logger
from loko_extensions.business.decorators import extract_value_args
from transformers import pipeline

# from business.gradio_interface import DEMO
from business.gradio_interface import DEMO
from business.text_generation import generate_text
from config.app_config import HF_TOKEN
from utils.decorator_fastapi import ExtractValueArgsFastapi
import gradio as gr

app = FastAPI()
CUSTOM_PATH = "/TextGenerationGui/"


# default model='gpt2'

@app.post("/text_gen")
@ExtractValueArgsFastapi(file=False)
def text_generator_api(value, args):
    logger.debug(f"args::: {args}")
    max_length = int(args.get("max_length")) if args.get("max_length") else None
    ngram_size = int(args.get("ngram_size")) if args.get("ngram_size", None) else None
    do_sample = args.get("do_sample", False)
    temperature = float(args.get("temperature", 0.7)) if args.get("temperature", 0.7) else None
    model = args.get("model", "gpt2")

    text_gen = generate_text(model=model, initial_msg=value, max_length=max_length, ngram_size=ngram_size,
                             do_sample=do_sample, temperature=temperature, return_type="dictionary")
    if model is None or model.isspace():
        model = "gpt2"
    logger.debug(f"Model used: {model}")
    return text_gen


app = gr.mount_gradio_app(app, DEMO, path=CUSTOM_PATH)

# if __name__ == "__main__":
#     # io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
#     # app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)
#     app.run("0.0.0.0", 8080)

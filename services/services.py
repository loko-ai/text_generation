from fastapi import Request, FastAPI, File
from loguru import logger
from loko_extensions.business.decorators import extract_value_args
from transformers import pipeline

# from business.gradio_interface import DEMO
from business.gradio_interface import DEMO
from utils.decorator_fastapi import ExtractValueArgsFastapi
import gradio as gr

app = FastAPI()
CUSTOM_PATH = "/TextGenerationGui/"

generator = pipeline(task="text-generation")


@app.post("/text_gen")
@ExtractValueArgsFastapi(file=False)
def text_generator_api(value, args):
    logger.debug(f"args::: {args}")
    max_length = int(args.get("max_length")) if args.get("max_length") else None
    ngram_size = int(args.get("ngram_size")) if args.get("ngram_size", None) else None
    do_sample = args.get("do_sample", False)
    temperature = float(args.get("temperature", 0.7)) if args.get("temperature", 0.7) else None
    text_gen = generator(value, max_length=max_length, no_repeat_ngram_size=ngram_size, do_sample=do_sample, temperature=temperature)
    return text_gen


app = gr.mount_gradio_app(app, DEMO, path=CUSTOM_PATH)

# if __name__ == "__main__":
#     # io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
#     # app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)
#     app.run("0.0.0.0", 8080)

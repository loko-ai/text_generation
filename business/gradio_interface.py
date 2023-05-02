import os
import gradio as gr

from transformers import pipeline

# from transformers import GenerationConfig
from business.text_generation import generate_text
from config.app_config import HF_TOKEN

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

example_start_text = "Your product is"

#
# def text_generator(initial_msg, model, max_length, ngram_size, do_sample, temperature):
#     if model is None or model.isspace():
#         model = "gpt2"
#     # generation_config = GenerationConfig.from_pretrained(model)
#
#     generator = pipeline(task="text-generation", model=model, use_auth_token=HF_TOKEN)
#     eos_token_id = generator.tokenizer.eos_token_id
#     text_gen = generator(initial_msg, max_length=max_length, no_repeat_ngram_size=ngram_size,
#                          do_sample=do_sample, temperature=temperature, pad_token_id=eos_token_id)
#     return text_gen[0]["generated_text"]
    # return generation_config


block = gr.Blocks(title="TextGenerator")  # , favicon_path="loko_logo.png")

with block as DEMO:
    with gr.Row():
        # gr.Image("loko_logo.png").style(height=100, width=30)
        gr.Markdown("""<h1><center>Loko TextGenerator</center></h1>""")
    with gr.Column():
        with gr.Row():
            model = gr.Text(label="Model", value="gpt2")
            max_length = gr.Number(label="Sentence maximum lenght", value=100)
            ngram_size = gr.Slider(minimum=1, maximum=10, step=1, label="No repeat N-Gram size", interactive=True,
                                   value=2)
            do_sample = gr.Checkbox(label="Sampling", interactive=True, value=True)
            temperature = gr.Slider(minimum=0.001, maximum=1.000, label="Temperature (Sentence Randomness)",
                                    interactive=True, value=0.300)
        initial_msg = gr.Textbox(label="Starting text", placeholder=example_start_text)
    submit = gr.Button("Submit")
    output_msg = gr.Textbox(label="Generated text")
    submit.click(generate_text, inputs=[model, initial_msg, max_length, ngram_size, do_sample, temperature],
                 outputs=[output_msg], api_name="text_gen")

# block.launch(server_name="0.0.0.0", server_port=8086, debug=True)

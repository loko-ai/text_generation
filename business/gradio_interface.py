import os
import gradio as gr

from transformers import pipeline

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

example_start_text = "Your product is"
generator = pipeline(task="text-generation")

def text_generator(initial_msg, max_length, ngram_size, do_sample, temperature):
    text_gen = generator(initial_msg, max_length=max_length, no_repeat_ngram_size=ngram_size, do_sample=do_sample, temperature=temperature)
    return text_gen[0]["generated_text"]



block = gr.Blocks(title="TextGenerator")#, favicon_path="loko_logo.png")

with block as DEMO:
    with gr.Row(scale=0.7):
        # gr.Image("loko_logo.png").style(height=100, width=30)
        gr.Markdown("""<h1><center>Loko TextGenerator</center></h1>""")
    with gr.Column():
        with gr.Row():
            max_length = gr.Number(label="Sentence maximum lenght")
            ngram_size = gr.Slider(minimum=1, maximum=10, step=1, label="No repeat N-Gram size", interactive=True, value=2)
            do_sample = gr.Checkbox(label="Sampling", interactive=True, value=True)
            temperature = gr.Slider(minimum=0.001, maximum=1.000, label="Temperature (Sentence Randomness)", interactive=True, value=0.300)
        initial_msg = gr.Textbox(label="Starting text", placeholder=example_start_text)
    submit = gr.Button("Submit")
    output_msg = gr.Textbox(label="Generated text")
    submit.click(text_generator, inputs=[initial_msg, max_length, ngram_size, do_sample,temperature], outputs=[output_msg], api_name="text_gen")

# demo.launch(server_name="0.0.0.0", server_port=8083, debug=True)

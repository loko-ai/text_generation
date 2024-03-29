from loko_extensions.model.components import Component, save_extensions, Arg, Dynamic, Input, Output

from extensions.text_generator_description import text_gen_description

model = Arg(name="model", label="Transforme Models", type="text",
            helper='Default model "gpt2". Type the name of the huggingface model you want to use, selecting among the ones available for the text-generation task (check the list here: https://huggingface.co/models?pipeline_tag=text-generation)',
            value="gpt2")
max_length = Arg(name="max_length", label="Sentence Max Length", type="number", helper="Integer number", value=100)

no_rep_ngrams_size = Arg(name="ngram_size", label="No Repeat N-Gram size", type="number", value=2,
                         helper="Integer number")  # , description="Size of t")

do_sample = Arg(name="do_sample", label="Sampling", type="boolean", value=True,
                description="If false, the text will be generated in a deterministic way. Otherwise, the words will be picked according to their conditional probability.")

temperature = Dynamic(name="temperature", label="Temperature", dynamicType="number", value=0.3, parent="do_sample",
                      condition="{parent}===true", helper="Float positive number. Max value 1.0",
                      description='With temperature=1, all the words will be picked only considering their probability. Lower "Temperature" values will make the distribution less random. The sentence will probabily be more logic, but with long text you can encounter more repetition. Use your perfect trade-off value.')

args = [model, max_length, no_rep_ngrams_size, do_sample, temperature]
input_list = [Input(id="text_generator", label="Text Generator", to="text_generator", service="text_gen")]
output_list = [Output(id="text_generator", label="Text Generator")]
text_gen_component = Component(name="TextGenerator", inputs=input_list, outputs=output_list, args=args,
                               description=text_gen_description, icon="RiFileList3Fill")

if __name__ == '__main__':
    save_extensions([text_gen_component])

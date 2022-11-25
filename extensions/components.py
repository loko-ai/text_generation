from loko_extensions.model.components import Component, save_extensions, Arg, Dynamic

max_length = Arg(name="max_length", label="Sentence Max Length", type="number", helper="Integer number")

no_rep_ngrams_size = Arg(name="ngram_size", label="No Repeat N-Gram size", type="number", value=2,
                         helper="Integer number")  # , description="Size of t")

do_sample = Arg(name="do_sample", label="Sampling", type="boolean", value=True,
                description="If false, the text will be generated in a deterministic way. Otherwise, the words will be picked according to their conditional probability.")

temperature = Dynamic(name="temperature", label="Temperature", dynamicType="number", value=0.3, parent="do_sample",
        condition="{parent}===true", helper="Float positive number. Max value 1.0",
        description='With temperature=1, all the words will be picked only considering their probability. Lower "Temperature" values will make the distribution less random. The sentence will probabily be more logic, but with long text you can encounter more repetition. Use your perfect trade-off value.')

args = [max_length, no_rep_ngrams_size, do_sample, temperature]

text_gen_component = Component(name="TextGenerator", args=args, icon="RiFileList3Fill")

if __name__ == '__main__':
    save_extensions([text_gen_component])

text_gen_description = '''
This extensions offers the possibility to use a block, TextGenerator, that as the name implies, will generate some text. 


You can decide a text to use as starting point, and you can also specify other parameters too:

- **Model:** the model name to use for generating your text. The default model in use is "gpt2", but you can choose among all the ones related to the huggingface's text generation task (listed here https://huggingface.co/models?pipeline_tag=text-generation);  
- **Sentence Maximum Length:** maximum lenght of the generated sentence;
- **Sampling:** whether to sample words, randomly picking the next ones
  according to their conditional probability distribution, or to pick them in a deterministic way;
- **Temperature:** value between 0 and 1, that will sharp the probability distribution, increasing the  likelihood of high probability words and decreasing the likelihood of low probability words. Essentially, applying this parameter the generation of word will be less random: with temperature close to 0, the most probable word will be selected, and the randomness will be dropped;
- **No Repeat N-Gram size:** choose the size of the N-Grams; all N-Grams of that size can only occur once.




You can decide to use these functionalities importing the "TextGenerator" block in your workflow or to use directly the GUI.
'''

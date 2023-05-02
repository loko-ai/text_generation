from _ctypes import Union

from loguru import logger
from transformers import pipeline

from config.app_config import HF_TOKEN


def generate_text( model, initial_msg, max_length, ngram_size, do_sample, temperature,
                  return_type: ["text", "dictionary"] = "text"):
    """
    The function generates text using a specified model and configuration, with options for length, ngram size, sampling,
    and return type.

    :param initial_msg: The initial message or prompt that the text generator will use to start generating text
    :param model: The language model to use for text generation. If no model is specified, it defaults to "gpt2"
    :param max_length: The maximum length of the generated text
    :param ngram_size: The size of the n-grams used in the generation process. N-grams are contiguous sequences of n items
    from a given sample of text. In this case, the n-grams are used to ensure that the generated text does not repeat itself
    too much. The value of ngram_size determines how
    :param do_sample: A boolean parameter that determines whether to use sampling or greedy decoding for text generation. If
    set to True, the model will randomly sample from the predicted probability distribution for the next token. If set to
    False, the model will choose the token with the highest probability
    :param temperature: Temperature is a hyperparameter used in text generation models that controls the level of randomness
    and creativity in the generated text. A higher temperature value will result in more diverse and unpredictable text,
    while a lower temperature value will result in more conservative and predictable text. The temperature value typically
    ranges from 0 to
    :param return_type: This parameter specifies the type of output that the function should return. It can be either "text"
    or "dictionary". If "text" is selected, the function will return the generated text as a string. If "dictionary" is
    selected, the function will return a dictionary containing additional information about the, defaults to text
    :type return_type: ["text","dictionary"] (optional)
    :return: The function `text_generator` returns either a generated text or a dictionary containing information about the
    generated text, depending on the value of the `return_type` parameter.
    """
    if model is None or model.isspace():
        model = "gpt2"
    logger.debug(f"Model used: {model}")
    # generation_config = GenerationConfig.from_pretrained(model)
    generator = pipeline(task="text-generation", model=model, use_auth_token=HF_TOKEN)
    eos_token_id = generator.tokenizer.eos_token_id
    text_gen = generator(initial_msg, max_length=max_length, no_repeat_ngram_size=ngram_size,
                         do_sample=do_sample, temperature=temperature, pad_token_id=eos_token_id)
    if return_type == "text":
        return text_gen[0]["generated_text"]
    else:
        return text_gen

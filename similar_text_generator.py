import random
import re


def generate_similar_text(output_len: int = 100, context: int = 2, input_text: str = None) -> str:
    tokens: list[str] = list()
    unique_words: set[str] = set()

    if input_text is None:
        with open("/Users/mb/Desktop/ML Text Generator/Python/ML-text-generator/input.txt", "r") as file:
            input_text: str = file.read()

    for word in re.split(r'\s+', input_text):
        word_no_punctuation: str = ""
        for char in word:
            if char.isalpha():
                word_no_punctuation += char
        tokens.append(word_no_punctuation)
        unique_words.add(word_no_punctuation)

    print(f"Unique words: {len(unique_words)}")
    print(f"Unique tokens: {len(tokens)}")

    wordmap: dict[tuple[str, ...], list[str]] = dict()
    context_tokens: list[str] = list()

    for i in range(context):
        context_tokens.append("")

    for token in tokens:
        context_tuple = tuple(context_tokens)
        if context_tuple in wordmap:
            wordmap[context_tuple].append(token)
        else:
            wordmap[context_tuple] = [token]
        context_tokens.append(token)
        context_tokens.pop(0)

    context_tokens = list()
    for i in range(context):
        context_tokens.append("")

    for i in range(output_len):
        context_tuple = tuple(context_tokens)
        random_index: int = random.randint(0, len(wordmap[context_tuple]) - 1)
        print(wordmap[context_tuple][random_index], end=" ")
        context_tokens.append(wordmap[context_tuple][random_index])
        context_tokens.pop(0)

    return "Not implemented yet"
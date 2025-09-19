from collections import Counter
import re

def normalize_words(text) -> list[str]:  # convert text to a list of lowercase words, ignoring punctuation
    return re.findall(r"[A-Za-z]+", text.lower())

def count_specific_word(text: str, target: str) -> int:
    """
    Count the number of times a word appears.
    text, target = strings to search through article.txt and (target) is the word to search for.
    Returns an int; 0 if no matches. Case-insensitive; punctuation is ignored.
    """
    words = normalize_words(text)
    target = re.sub(r"[^A-Za-z]+", "", target.lower())
    if not target:
        return 0
    return words.count(target)

def identify_most_common_word(text: str) -> str | None:  # find the most common word
    words = normalize_words(text)
    if not words:  # edge case: empty text
        return None
    counter = Counter(words)
    most_common_word, _ = counter.most_common(1)[0]
    return most_common_word

def calculate_average_word_length(text: str) -> float:  # calculate the average word length
    words = normalize_words(text)
    if not words:  # edge case: empty text
        return 0.0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def count_paragraphs(text: str) -> int: #count the number of paragraphs
    paragraphs = [p for p in re.split(r"\r?\n\s*\r?\n", text) if p.strip()] #split one or more blank lines.
    if not paragraphs: #edge case: empty
        return 1
    else:
        return len(paragraphs)

def count_sentences(text: str) -> int: #count number of sentence\defined by ending ., !, or ?.
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    if not sentences:
        return 1
    return len(sentences)


if __name__ == "__main__":
    # read article from file
    with open("article.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # while loop to let user search repeatedly
    while True:
        word_to_find = input("Enter a word to search for (or type 'quit' to exit): ")
        if word_to_find.lower() == "quit":
            print("Exiting word search...")
            break

        # get count using the function
        count = count_specific_word(text, word_to_find)

        # results for the chosen word
        print(f"The word '{word_to_find}' appears {count} times in the article.")

    # display the most common word
    most_common = identify_most_common_word(text)
    if most_common is not None:
        print(f"The most common word in the article is '{most_common}'.")
    else:
        print("The article is empty, no common word found.")

    # display average word length
    average_length = calculate_average_word_length(text)
    if average_length != 0.0:  # if there are words
        print(f"The average word length is {average_length:.2f}.")
    else:
        print("The average word length is 0.0 (no words found).")

    # display paragraph count
    paragraphs = count_paragraphs(text)
    if paragraphs == 1:
        print("The count of paragraphs is 1.")
    else:
        print(f"The count of paragraphs is {paragraphs}.")

    # display sentence count
    sentences = count_sentences(text)
    if sentences == 1:
        print("The count of sentences is 1.")
    else:
        print(f"The count of sentences is {sentences}.")

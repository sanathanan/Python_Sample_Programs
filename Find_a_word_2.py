# Importing the Regex library for removing the unwanted character
import re


def word_count(input_str,word, sent_int, word_int):

    # removing ( ), - , ' , , , .
    pre_processed_text = re.sub(pattern="[^\w\s]", repl=" ", string=input_str)

    for i in range(0,sent_int):
        # Splitting the text
        text_1 = pre_processed_text.split(" ")

        count=0

        for i in range(0, len(text_1)):
            for j in range(0,word_int):
                if word == text_1[i]:
                    count = count+1
        return  count

input_str = "foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo."
word = "foo"
sent_int =1
word_int =1

count_words = word_count(input_str, word,sent_int,word_int)

print(count_words)
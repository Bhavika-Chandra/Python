#pip install langdetect

from langdetect import detect
text = input("Enter the text in any language: ")
print(detect(text))

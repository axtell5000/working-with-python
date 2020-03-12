from translate import Translator

translator = Translator(to_lang="pt")
try:
    with open("./test.txt", mode="r") as translate_file:
        text = translate_file.read()
        translation = translator.translate(text)
        print(translation)
        with open("translated-text.txt", mode="w") as translated_fle:
            translated_fle.write(translation)
except FileNotFoundError as err:
    print("File path incorrect")


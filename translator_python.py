from deep_translator import GoogleTranslator

x= input("Enter in which lang you want to translate")
translate_source=GoogleTranslator(source="auto",target=x)

translate_input=translate_source.translate(input(f"enter a line to translate into {x}: "))

print(translate_input)


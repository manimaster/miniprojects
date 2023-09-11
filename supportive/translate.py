from googletrans import Translator

# Define a dictionary of Indian languages
indian_languages = {
    'kn': 'Kannada',
    'ta': 'Tamil',
    'te': 'Telugu',
    'mr': 'Marathi',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'gu': 'Gujarati',
    'pa': 'Punjabi',
    'ml': 'Malayalam',
    'or': 'Odia'
}

def translate(text, target_language):
    translator = Translator()
    translated_lines = []

    # Split the input text into lines
    lines = text.splitlines()

    for line in lines:
        translated = translator.translate(line, src='en', dest=target_language)
        translated_lines.append(translated.text)

    return '\n'.join(translated_lines)

if __name__ == "__main__":
    print("Indian Languages:")
    for i, (code, lang) in enumerate(indian_languages.items(), start=1):
        print(f"{i}. {lang} ({code})")

    choice = input("Enter the number of the target language: ")

    if choice.isdigit() and 1 <= int(choice) <= len(indian_languages):
        target_language_code = list(indian_languages.keys())[int(choice) - 1]

        # Accept multiline input
        text_to_translate = input("Enter the English text to translate (press Enter twice to finish):\n")
        while True:
            line = input()
            if not line:
                break
            text_to_translate += '\n' + line

        translated_text = translate(text_to_translate, target_language_code)

        print(f"Translated text ({indian_languages[target_language_code]}):\n{translated_text}")
    else:
        print("Invalid choice")

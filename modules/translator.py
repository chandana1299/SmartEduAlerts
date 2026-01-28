from deep_translator import GoogleTranslator

def translate_text(text, lang):
    return GoogleTranslator(source='en', target=lang).translate(text)

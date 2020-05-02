from PIL import Image
from googletrans import Translator
import pytesseract
import pinyin
import argparse

parser = argparse.ArgumentParser(description="Translate an image of chinese text to its characters, pinyin and English")
parser.add_argument("file", type=str)
parser.add_argument("--src", default="chi_tra")
args = parser.parse_args()

lang = args.src
translator = Translator()

img = Image.open(args.file)
config = "preserve_interword_spaces=1"
characters = pytesseract.image_to_string(img, lang=lang, config=config)
characters_nospace = characters.replace(" ", "")
pinyin = pinyin.get(characters)
english = translator.translate(characters_nospace).text
print(characters)
print(pinyin)
print(english)

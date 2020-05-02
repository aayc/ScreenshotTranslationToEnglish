# Translate a screenshot to English

## Getting started: it's a hack.

### Get the code
Clone the repository and build it into an executable (it's a one-file executable so you can move it whereever you'd like after building it)

```
git clone https://github.com/aayc/screenshot-translation-to-english.git
cd screenshot-translation-to-english
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
sh build.sh
dist/screenshot-translator ~/EXAMPLE_IMAGE.png --src chi_tra # for chinese
```

### Automator
This program doesn't take the screenshots for you.  Mac Automator does, though.  Set something up like this:

Running this app will take a screenshot and pipe it into screenshot-translator, then display it in an alert box.  Enjoy!

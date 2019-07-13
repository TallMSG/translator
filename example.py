import requests

API_KEY = 'trnsl.1.1.20190710T094556Z.6c30d1c7df878f86.fa25a144af7a9ee2609235c6ae47b53f877c4768'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(file_from, file_to, from_lang, to_lang='ru'):

        def translation(file_from):
            params = {
                'key': API_KEY,
                'text': file_from,
                'lang': '{}-{}'.format(from_lang, to_lang),
            }

            response = requests.get(URL, params = params)
            json_ = response.json()
            return '\n'.join(json_['text'])

        with open(file_from, encoding="utf-8") as text:
            text = [line.rstrip('\n') for line in text.readlines()]
            output = open(file_to, 'w')
            output.write(translation(text))

translate_it('News/FR.txt','News/translated_FR.txt', 'fr')
translate_it('News/ES.txt','News/translated_ES.txt', 'es')
translate_it('News/DE.txt','News/translated_DE.txt', 'de')

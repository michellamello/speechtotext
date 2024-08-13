import os
import warnings
import whisper

warnings.filterwarnings('ignore')

MODEL_NAME = "medium"
audio_path = os.getcwd() + "/Arquivos/"
txt_path = os.getcwd() + "/Transcricoes/"
model = whisper.load_model(MODEL_NAME)

print('-' * 80)
print('Exercício - Speech to text')
print('-' * 80)

files = os.listdir(audio_path)

print(f'\n {len(files)} arquivos encontrados.\n')

for file in files:
    print(f'Processando arquivo {file}...')

    result = model.transcribe(audio_path + file)

    with open(txt_path + file.replace('.mp3', '.txt'), 'w', encoding='utf-8') as txt:
        txt.write(result['text'])

print('\nProcessamento finalizado!')

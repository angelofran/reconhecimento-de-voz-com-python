import speech_recognition as sr
from tqdm import tqdm
from time import sleep


try:

    recognizer = sr.Recognizer() # Inicia o reconhecedor de voz

    #lista_mic = sr.Microphone().list_microphone_names()
    #print(lista_mic)  # Lista todos os microfones internos e externos ligados ao computador

    with sr.Microphone(2) as microphone: # Inicia o microfone e no final fecha-o
        try:
            recognizer.adjust_for_ambient_noise(microphone) # Ajustar-se-á ao som do ambiente
            print("\033[32mOuvindo...\033[m")
            audio = recognizer.listen(microphone) # Para fazer a captura do áudio
            text = recognizer.recognize_google(audio, language="pt-BR") # Transformá-lo em texto

            for i in tqdm(range(10), colour="green", ascii=True, desc="Descodificando...", ncols=70):
                    sleep(1)
            print(f"\033[32mFEITO A MENSAGEM OBTIDA FOI\033[m\n\t{text}")
        except Exception as error:
            print(f"\033[31mERRO, TENTE NOVAMENTE.\033[m")


    

except KeyboardInterrupt:
    print("\033[31mAcção interropida.\033[m")
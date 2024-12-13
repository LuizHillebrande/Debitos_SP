import tkinter as tk
from tkinter import messagebox
import openpyxl
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import openpyxl
import time
from time import sleep
import os
import requests
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import re

import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import time

def capturar_som_sistema(duracao=5, arquivo_saida="audio_sistema.wav"):
    print("Capturando som do sistema...")
    try:
        # Captura o áudio emitido pelo sistema em tempo real
        frequencia = 44100  # Taxa de amostragem (Hz)
        gravacao = sd.rec(int(duracao * frequencia), samplerate=frequencia, channels=2)
        sd.wait()  # Aguarda a captura terminar
        write(arquivo_saida, frequencia, gravacao)  # Salva o áudio em um arquivo WAV
        print(f"Som capturado e salvo como '{arquivo_saida}'.")
        return arquivo_saida
    except Exception as e:
        print(f"Erro ao capturar áudio do sistema: {e}")
        return None

def reconhecer_audio(arquivo_audio):
    reconhecedor = sr.Recognizer()
    try:
        with sr.AudioFile(arquivo_audio) as fonte_audio:
            print("Reconhecendo o áudio...")
            audio = reconhecedor.record(fonte_audio)  # Lê o áudio do arquivo
            texto = reconhecedor.recognize_google(audio, language="pt-BR")
            print("Texto reconhecido:", texto)
            return texto
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento de voz.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    return None

def consultar_debitos_sp():
    driver = webdriver.Chrome()
    driver.get('https://senhawebsts.prefeitura.sp.gov.br/Account/Login.aspx?ReturnUrl=%2f%3fwa%3dwsignin1.0%26wtrealm%3dhttps%253a%252f%252fduc.prefeitura.sp.gov.br%252fportal%252f%26wctx%3drm%253d0%2526id%253dpassive%2526ru%253d%25252fportal%25252f%26wct%3d2024-12-13T11%253a05%253a53Z&wa=wsignin1.0&wtrealm=https%3a%2f%2fduc.prefeitura.sp.gov.br%2fportal%2f&wctx=rm%3d0%26id%3dpassive%26ru%3d%252fportal%252f&wct=2024-12-13T11%3a05%3a53Z')

    tocar_som = WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.XPATH,"//button[@id='lnkTocarSom']"))
    )
    tocar_som.click()
    
    arquivo_som = capturar_som_sistema(duracao=5)

    # Reconhece o texto do áudio capturado
    if arquivo_som:
        texto = reconhecer_audio(arquivo_som)
        if texto:
            print("Texto do áudio:", texto)
        else:
            print("Falha no reconhecimento.")

consultar_debitos_sp()
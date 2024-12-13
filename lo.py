import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import time

def listar_dispositivos_audio():
    print("Dispositivos de áudio disponíveis:")
    print(sd.query_devices())

listar_dispositivos_audio()
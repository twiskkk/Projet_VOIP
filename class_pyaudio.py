import pyaudio

class VOIP():

    def __init__(self, CHANNELS : int, RATE : int, CHUNK : int, RECORD_SECONDS : int)

        self.__FORMAT = pyaudio.paInt16
        self.__CHANNELS = CHANNELS
        self.__RATE = RATE
        self.__CHUNK = CHUNK
        self.__RECORD_SECONDS = RECORD_SECONDS
  
audio = pyaudio.PyAudio()
  
# Debut enregistrement
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print ("Enregistrement en cours...")





if __name__ == "__main__":
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    
    audio = pyaudio.PyAudio()
    
    # Debut enregistrement
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print ("Enregistrement en cours...")

    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)  
    print ("Fin d'enregistrement")

    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
    for data in frames:
        stream.write(data)

    print ("Fin ")

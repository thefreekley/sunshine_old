import pyaudio
import struct
import math
import numpy as np

INITIAL_TAP_THRESHOLD = 0.010
FORMAT = pyaudio.paInt16
SHORT_NORMALIZE = (1.0 / 32768.0)
CHANNELS = 2
RATE = 44100
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE * INPUT_BLOCK_TIME)

OVERSENSITIVE = 15.0 / INPUT_BLOCK_TIME

UNDERSENSITIVE = 120.0 / INPUT_BLOCK_TIME

MAX_TAP_BLOCKS = 0.15 / INPUT_BLOCK_TIME


def get_rms(block):
    count = len(block) / 2
    format = "%dh" % (count)
    shorts = struct.unpack(format, block)

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n * n

    return math.sqrt(sum_squares / count)

def fft_transform(data):
    count = len(data) / 2
    format = "%dh" % (count)
    data_unpacked = struct.unpack(format, data)
    data_np = np.array(data_unpacked)
    data_fft = np.fft.fft(data_np)
    data_freq = np.abs(data_fft) / len(data_fft)
    data_freq = list(map(lambda x: int(x*10), data_freq))
    return data_freq


class AmplitudeLevel(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()

    def find_input_device(self):
        device_index = 3
        input_device = []
        for i in range(self.pa.get_device_count()):
            info = self.pa.get_device_info_by_index(i)
            if info['maxInputChannels']!=0 and info['maxOutputChannels']==0 and info['hostApi']==0:
                input_device.append(info)


        return input_device

    def open_mic_stream(self):
        device_index = 3

        stream = self.pa.open(format=FORMAT,
                              channels=CHANNELS,
                              rate=RATE,
                              input=True,
                              input_device_index=device_index,
                              frames_per_buffer=INPUT_FRAMES_PER_BLOCK)

        return stream

    def listen(self):

        block = self.stream.read(INPUT_FRAMES_PER_BLOCK)

        amplitude = get_rms(block)

        return amplitude * 10000

    def get_fft(self):
        block = self.stream.read(INPUT_FRAMES_PER_BLOCK)

        norm = fft_transform(block)

        frequency = [1,3,7,13,25,50,100,150]
        # frequency = [1,8,16,24,32,40,64,100]
        norm_frequency = []
        for i in frequency:
            norm_frequency.append(norm[i])

        return norm_frequency

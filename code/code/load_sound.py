import scipy.io.wavfile as wv
import sys

# Simple test script to see how best to load .wav files as vectors.

first, second = wv.read('../sound_files/disco_dancing.wav')
print(first, second.shape)
import numpy as np
import wave
from librosa.core import load
from librosa.feature import mfcc

class MfccFeatureExtractor(object):

    def __init__(self, sample_rate=None, 
                       nb_mfcc=16, 
                       fft_size=0.025, 
                       window_shift=0.01, 
                       mean_normalize=True):
        self.sample_rate = sample_rate
        self.nb_mfcc = nb_mfcc
        self.fft_size = fft_size
        self.window_shift = window_shift
        self.mean_normalize = mean_normalize

    def detect_sample_rate(self, audio_path):
        sample_rate = 0
        audio_file = wave.open(audio_path)
        sample_rate = audio_file.getframerate()
        audio_file.close()
        return sample_rate

    def extract_features(self, path):
        if not self.sample_rate:
            self.sample_rate = self.detect_sample_rate(path)
        y, sr = load(path, sr=self.sample_rate)
        n_fft = int(self.fft_size * self.sample_rate)
        hop_length = int(self.window_shift * self.sample_rate)
        features = mfcc(y, sr=self.sample_rate, 
                           n_mfcc=self.nb_mfcc, 
                           n_fft=n_fft, 
                           hop_length=hop_length, 
                           power=1)
        features = features.T
        if self.mean_normalize:
            features -= np.mean(features, axis=0)
        return features

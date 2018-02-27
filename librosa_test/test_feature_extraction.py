import sys
from feature_extractor import MfccFeatureExtractor

if __name__ == '__main__':
    audio_path = sys.argv[1]
    mfcc_extractor = MfccFeatureExtractor()
    features = mfcc_extractor.extract_features(audio_path)

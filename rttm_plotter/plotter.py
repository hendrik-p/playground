import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def read_rttm(path):
    rttm_file = open(path)
    segmentation = []
    for line in rttm_file:
        splitted = line.strip().split(' ')
        start = float(splitted[3])
        duration = float(splitted[4])
        speaker = splitted[7]
        segmentation.append((start, duration, speaker))
    rttm_file.close()
    return segmentation

def draw_horizontal_line(x_start, x_end, y, linewidth=2, color='k'):
    plt.plot([x_start, x_end], [y, y], '-', c=color, lw=linewidth)

def draw_segment(segment, speaker_colors, y=0):
    start = segment[0]
    duration = segment[1]
    speaker = segment[2]
    color = speaker_colors[speaker]
    end = start + duration
    draw_horizontal_line(start, end, 10, color=color, linewidth=5)

def draw_segmentation(segmentation):
    speakers = np.unique([speaker for _, _, speaker in segmentation])
    speaker_colors = {}
    for speaker, color in zip(speakers, matplotlib.colors.cnames.keys()):
        speaker_colors[speaker] = color
    for segment in segmentation:
        draw_segment(segment, speaker_colors)

if __name__ == '__main__':
    rttm_path = sys.argv[1]
    segmentation = read_rttm(rttm_path)
    draw_segmentation(segmentation)
    plt.show()


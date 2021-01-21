import argparse
import pandas as pd
from util import *


# parse filename

parser = argparse.ArgumentParser(
    description='Filtering strategies for rssi time series')
parser.add_argument('--file', nargs='?', help='data filename', default='sample.csv')

args = parser.parse_args()

file_name = args.file

# open file and read RSSI signal

file = pd.read_csv(file_name)

signal = file['rssi']

print(signal)

# calculate filters

#signal_gray_filter = gray_filter(signal, N=8)
#signal_fft_filter = fft_filter(signal, N=10, M=2)
signal_kalman_filter = kalman_filter(signal, A=1, H=1, Q=1.6, R=6)
#signal_particle_filter = particle_filter(signal, quant_particles=100, A=1, H=1, Q=1.6, R=6)

# plot signal and filters

plot_signals([signal, signal_kalman_filter],
             ['signal', 'kalman_filtered_signal'])



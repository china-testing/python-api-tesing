from __future__ import print_function
from scipy.io import wavfile
import matplotlib.pyplot as plt
import urllib2
import numpy as np

response = urllib2.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav')
print(response.info())
WAV_FILE = 'smashingbaby.wav'
filehandle = open(WAV_FILE, 'w')
filehandle.write(response.read())
filehandle.close()
sample_rate, data = wavfile.read(WAV_FILE)
print("Data type", data.dtype, "Shape", data.shape)

plt.subplot(2, 1, 1)
plt.title("Original audio signal")
plt.plot(data)
plt.grid()

plt.subplot(2, 1, 2)

# Repeat the audio fragment
repeated = np.tile(data, 4)

# Plot the audio data
plt.title("Repeated 4 times")
plt.plot(repeated)
wavfile.write("repeated_yababy.wav",
    sample_rate, repeated)
plt.grid()
plt.tight_layout()
plt.show()

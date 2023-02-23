import soundcard as sc
import numpy

default_speaker = sc.default_speaker()
print(default_speaker)
default_microphone = sc.get_microphone("MacBook Air Microphone")
print(default_microphone)

# record and play back one second of audio:
#data = microphone.record(numframes=24000, samplerate=48000, blocksize=512)
# normalized playback
#speaker.play(data/numpy.max(numpy.abs(data)), samplerate=48000)


with default_microphone.recorder(samplerate = 48000, channels = [0], blocksize = 512) as microphone, \
    default_speaker.player(samplerate = 48000, channels = [1, 0], blocksize = 512) as speaker:
    for _ in range(100):
        data = microphone.record(numframes = 1024 * 12)
        speaker.play(data/numpy.max(numpy.abs(data)))



#with default_mic.recorder(samplerate=48000, channels=[0], blocksize=512) as mic, \
#      default_speaker.player(samplerate=48000, channels=[1,0], blocksize=512) as sp:
#    for _ in range(100):
#        data = mic.record(numframes=1024*12)
#        sp.play(data/numpy.max(numpy.abs(data)))
import soundcard as sc
import numpy

switch, i = True, 0
default_speaker = sc.default_speaker()
print(sc.get_microphone("MacBook Air Microphone"))
default_microphone = sc.default_microphone().name
print(default_speaker)
print(sc.all_microphones())
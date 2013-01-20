from espeak import espeak
from datetime import datetime
import time

str = "this is an example text"
print str
stat = espeak.is_playing
print stat
espeak.synth(str)

    

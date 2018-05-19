import os

for x in range(1,128):
    os.system('python Interpreter.py "Bpm(80)[Inst(' + str(x) + ')|:3G#4q Bb4s G#4s Bb4s p1s Eb4q p1q|]*(1)" "lead' + str(x) +'"')

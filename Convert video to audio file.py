
import subprocess
import re

input_video = input("Enter filepath to video: ")
output_audio = re.sub(r'\.\w*', r' ', input_video, flags=re.I |
                      re.M) + input("Enter audio filename suffix:-") + ".m4a"


cmd = ['ffmpeg', '-i', input_video, '-vn',
       '-c:a', 'aac', '-b:a', '256k', '-ar', '44100', '-ac', '1', output_audio]

subprocess.run(cmd)

print("Done!")

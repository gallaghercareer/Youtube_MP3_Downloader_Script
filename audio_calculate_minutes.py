import os
import soundfile as sf

input = input("Directory of mp3 files to calculate:")
directory = input
total_duration = 0

for filename in os.listdir(directory):
    if filename.endswith('.mp3'):
        filepath = os.path.join(directory, filename)
        with sf.SoundFile(filepath) as f:
            duration = len(f) / f.samplerate
            total_duration += duration
total_seconds = int(total_duration)
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f'Total duration: {hours:02d}:{minutes:02d}:{seconds:02d}')
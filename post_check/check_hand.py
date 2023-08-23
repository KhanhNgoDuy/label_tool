import cv2
import keyboard
import pandas as pd
from pathlib import Path
from threading import Thread


# Get paths
folder = 'data/s1_Jeremy'
folder_path = Path(folder)
mp4_files = list(folder_path.glob('**/*.mp4'))
csv_files = list(folder_path.glob('**/*.csv'))
print(mp4_files)

# Display videos
font = cv2.FONT_HERSHEY_SIMPLEX
org = (250, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

for video, annot in zip(mp4_files, csv_files):
    df = pd.read_csv(annot)
    label_ls = df['label']
    start_ls = df['start']
    stop_ls = df['stop']

    hands = []
    idx = 0

    cap = cv2.VideoCapture(video.as_posix())
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(length):
        ret, frame = cap.read()
        if i == start_ls[idx]:
            cv2.imshow('frame', frame)
            if keyboard.is_pressed('r'):
                hand = 'Right'
            elif keyboard.is_pressed('l'):
                hand = 'Left'
            df['Hand'] = hand

        if 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


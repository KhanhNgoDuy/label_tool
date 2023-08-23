import time
import datetime
import cv2
import os
from pathlib import Path


def cut_video_into_frames(video_path, save_folder):
    cap = cv2.VideoCapture(video_path)
    Path(save_folder).mkdir(parents=True, exist_ok=True)
    name = save_folder.split('\\')[-1]

    # Read and save each frame of the video
    frame_count = 1
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save the frame as an image
        frame_name = f"{name}_{frame_count:04d}.jpg"
        save_path = os.path.join(save_folder, frame_name)
        cv2.imwrite(save_path, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()


# Set the paths
video_root = 'data/'
frame_root = 'data/frame/'

video_folders = ['s6_LeVietDuc', 's7_TranVanThang', '']

# Get all video files in the folder
video_files = list(Path(video_folder).glob('*.mp4'))

# Process each video file
start = time.perf_counter()
print(datetime.datetime.now().strftime("%H:%M:%S"))
for video_file in video_files:
    start1 = time.perf_counter()
    video_path = str(video_file)
    save_folder = os.path.join(frame_folder, video_file.stem)
    print(video_file.stem)
    cut_video_into_frames(video_path, save_folder)
    now = time.perf_counter()
    print(f'Total:\t{round(now-start)}\tCurrent:\t{round(now-start1)}')
print(datetime.datetime.now().strftime("%H:%M:%S"))

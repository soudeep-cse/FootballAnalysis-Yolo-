import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frame, save_output_path):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    height, width, _ = output_video_frame[0].shape
    output = cv2.VideoWriter(save_output_path,fourcc,24,(width,height))
    for frame in output_video_frame:
        output.write(frame)
    output.release()




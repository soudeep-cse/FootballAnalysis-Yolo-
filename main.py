from utils import read_video, save_video
from trackers import Tracker
import cv2
import numpy as np
from team_assigner import TeamAssigner

def main():
    # Read video
    video_frames = read_video(r"Project\Yolo_OpenCV_Project\input_video\08fd33_4.mp4")

    tracker = Tracker(r"Project\Yolo_OpenCV_Project\models\best.pt")
    
    track = tracker.get_object_tracker(
    video_frames,
    read_from_stub=False,  # allow saving
    stub_path=r"D:\Computer_Vision\Project\Yolo_OpenCV_Project\stubs\track_stubs.pkl"
    )
    
    # Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], 
                                    track['players'][0])  

    for frame_num, player_track in enumerate(track['players']):
        for player_id, player_info in player_track.items():
            team = team_assigner.get_player_team(
                video_frames[frame_num],
                player_info['bbox'],
                player_id
            )
            player_info['team'] = team
            player_info['team_color'] = team_assigner.team_colors[team]

    # Draw output_tracks
    output_video_frames = tracker.draw_annotations(video_frames, track)

    # Save video
    save_video(output_video_frames,r"D:\Computer_Vision\Project\Yolo_OpenCV_Project\output_video\output_video.mp4")

if __name__ == "__main__":
    main()
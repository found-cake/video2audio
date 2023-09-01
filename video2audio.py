import sys
from moviepy.video.io.VideoFileClip import VideoFileClip


def video2audio(input_path: str, output_path: str) -> None:
    video_clip = VideoFileClip(input_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path)
    video_clip.close()
    audio_clip.close()


if len(sys.argv) < 3:
    print("Usage: python video2audio.py <input_video_path> <output_audio_path>")
else:
    input_video_path = sys.argv[1]
    output_audio_path = sys.argv[2]
    video2audio(input_video_path, output_audio_path)

import os
import subprocess

def extract_frames(video_path, output_folder, frame_pattern="frame_%04d.png"):
    os.makedirs(output_folder, exist_ok=True)
    cmd = f"ffmpeg -i {video_path} -qscale:v 2 {output_folder}/{frame_pattern}"
    subprocess.run(cmd, shell=True, check=True)
    print(f"[+] Đã tách frame từ {video_path} -> {output_folder}")

video_output = "video_stego.mpg"
frames_stego_folder = "frames_stego"

print("\n[5] Tách lại frame từ video stego...")
extract_frames(video_output, frames_stego_folder)


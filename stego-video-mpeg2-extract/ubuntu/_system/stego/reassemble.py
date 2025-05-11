import subprocess

def reassemble_video(frames_folder, audio_path, output_path, fps=25):
    cmd = (
        f"ffmpeg -r {fps} -i {frames_folder}/frame_%04d.png "
        f"-i {audio_path} -c:v mpeg2video -q:v 2 "
        f"-c:a mp2 -b:a 64k -shortest {output_path}"
    )
    subprocess.run(cmd, shell=True, check=True)
    print(f"[+] Video with stego -> {output_path}")

frames_folder = "frames"
audio_file = "audio.mp2"
video_output = "video_stego.mpg"

print("\n[4] Ghép frame và audio thành video stego...")
reassemble_video(frames_folder, audio_file, video_output)


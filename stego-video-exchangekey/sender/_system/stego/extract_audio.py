import subprocess

def extract_audio(video_path, audio_path):
    subprocess.run(f'ffmpeg -y -i {video_path} -vn -acodec mp2 -b:a 64k {audio_path}', shell=True, check=True)
    print(f"[+] Extracted audio from {video_path} -> {audio_path}")

video_input = "testvid.mpg"
audio_file = "audio.mp2"

print("\n[2] Tách audio từ video gốc...")
extract_audio(video_input, audio_file)


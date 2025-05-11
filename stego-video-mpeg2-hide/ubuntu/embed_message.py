import os
import cv2
import numpy as np
from scipy.fftpack import dct, idct

def dct2(block): return dct(dct(block.T, norm='ortho').T, norm='ortho')
def idct2(block): return idct(idct(block.T, norm='ortho').T, norm='ortho')

def embed_message_into_frame(frame_path, message, stego_frame_path, delta=30, group_size=5):
    print(f"[+] Đang giấu tin vào: {frame_path}")
    image = cv2.imread(frame_path).astype(np.float32)
    height, width, _ = image.shape

    binary_message = ''.join(format(ord(c), '08b') for c in message)
    msg_idx = 0
    coeff_positions = [(2,2), (2,3), (3,2), (3,3), (4,2), (2,4), (4,3), (3,4)]

    for i in range(0, height, 8):
        for j in range(0, width, 8):
            if msg_idx >= len(binary_message): break
            block = image[i:i+8, j:j+8, 1]
            dct_block = dct2(block)
            bit = int(binary_message[msg_idx])
            for idx in range(group_size):
                u, v = coeff_positions[idx % len(coeff_positions)]
                coeff = dct_block[u, v]
                coeff = round(coeff / delta) * delta + (delta/2 if bit else -delta/2)
                dct_block[u, v] = coeff
            image[i:i+8, j:j+8, 1] = np.clip(idct2(dct_block), 0, 255)
            msg_idx += 1

    cv2.imwrite(stego_frame_path, image.astype(np.uint8))
    print(f"[+] Stored frame with stego at : {stego_frame_path}")

with open("secretmessage.txt", "r") as f:
    message = f.read()

frames_folder = "frames"
frame_path = os.path.join(frames_folder, "frame_xxxx.png")

#message_to_embed = "This is a secret message!"
delta_value = 200


print("\n[3] Giấu tin vào frame ...")
embed_message_into_frame(frame_path, message, frame_path, delta=delta_value)


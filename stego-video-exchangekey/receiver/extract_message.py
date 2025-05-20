import os
import cv2
import numpy as np
from scipy.fftpack import dct, idct

def dct2(block): return dct(dct(block.T, norm='ortho').T, norm='ortho')
def idct2(block): return idct(idct(block.T, norm='ortho').T, norm='ortho')

def extract_message_from_frame(frame_path, num_bits, delta=30, group_size=5):
    print(f"[+] Đang tách tin từ: {frame_path}")
    image = cv2.imread(frame_path).astype(np.float32)
    height, width, _ = image.shape
    extracted_bits = []
    coeff_positions = [(2,2), (2,3), (3,2), (3,3), (4,2), (2,4), (4,3), (3,4)]

    msg_idx = 0
    for i in range(0, height, 8):
        for j in range(0, width, 8):
            if msg_idx >= num_bits: break
            block = image[i:i+8, j:j+8, 1]
            dct_block = dct2(block)
            votes = []
            for idx in range(group_size):
                u, v = coeff_positions[idx % len(coeff_positions)]
                coeff = dct_block[u, v]
                residual = coeff - round(coeff / delta) * delta
                votes.append(1 if residual > 0 else 0)
            bit = 1 if sum(votes) > (group_size // 2) else 0
            extracted_bits.append(str(bit))
            msg_idx += 1

    binary_message = ''.join(extracted_bits)
    #print(f"[+] Binary message : {binary_message}")
    message = ''.join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8) if len(binary_message[i:i+8]) == 8])
    return message

stego_first_frame = os.path.join("frames_stego", "frame_0001.png")
message_length =  44;
delta_value = 200

print("\n[6] Extracting from frame ...")
message = extract_message_from_frame(stego_first_frame, num_bits=message_length*8, delta=delta_value)
print(f"[+] AES key message : {message}")



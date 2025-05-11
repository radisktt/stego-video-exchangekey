def binary_to_text(binary_string):
    """
    Chuyển chuỗi nhị phân (bit) thành chuỗi ký tự ASCII
    """
    message = ''
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if len(byte) == 8:
            char = chr(int(byte, 2))
            message += char
    return message


# === DEMO ===
if __name__ == "__main__":
    # Ví dụ chuỗi nhị phân đầu vào
    binary_input = input("Input: ").strip()

    # Chuyển thành văn bản
    decoded_message = binary_to_text(binary_input)

    print("\n[+] Message is:")
    print(decoded_message)


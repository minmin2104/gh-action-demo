import os
import random
import base64


def generate_random_base64(length):
    random_bytes = random.randbytes(length)
    encoded_bytes = base64.b64encode(random_bytes)
    return encoded_bytes.decode('utf-8').rstrip('=')


if __name__ == '__main__':
    filepath = 'storage/data.txt'
    os.makedirs('storage', exist_ok=True)

    current_count = 0
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            current_count = len(f.readlines())

    if current_count < 50:
        with open(filepath, 'a') as f:
            for i in range(10):
                rand_not_secret = generate_random_base64(16)
                f.write(rand_not_secret + '\n')
        print(f'Added 10 more new lines. New total: {current_count}')
    else:
        print('The file already has 50 lines of notsecret key. Skipping generation')

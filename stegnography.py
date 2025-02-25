import cv2
import os

image = cv2.imread("hyperland.jpg")  # Replace with the correct image path

secret_text = input("Enter secret message: ")
access_key = input("Enter a passcode: ")

char_to_ascii = {}
ascii_to_char = {}

for index in range(255):
    char_to_ascii[chr(index)] = index
    ascii_to_char[index] = chr(index)

row = 0
col = 0
channel = 0

for char in range(len(secret_text)):
    image[row, col, channel] = char_to_ascii[secret_text[char]]
    row += 1
    col += 1
    channel = (channel + 1) % 3

cv2.imwrite("encoded_image.jpg", image)
os.system("start encoded_image.jpg")  # Use 'start' to open the image on Windows

decoded_message = ""
row = 0
col = 0
channel = 0

user_key = input("Enter passcode for Decryption: ")
if access_key == user_key:
    for char in range(len(secret_text)):
        decoded_message += ascii_to_char[image[row, col, channel]]
        row += 1
        col += 1
        channel = (channel + 1) % 3
    print("Decrypted message:", decoded_message)
else:
    print("ACCESS DENIED!")

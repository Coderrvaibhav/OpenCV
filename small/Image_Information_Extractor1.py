import cv2
import os

path = "C:\data\Visual_Studio\OpenCV\small\Chota_Bheem.jpg"


img = cv2.imread(path)

if img is None:
    print("Error: Image is not found!")
else:
    height , width, channel = img.shape

    file_size = os.path.getsize(path) / 1024

    total_pixel = height * width



    # Display information
    print("\n===== IMAGE INFORMATION =====")
    print(f"File Name      : {os.path.basename(path)}")
    print(f"Width          : {width} pixels")
    print(f"Height         : {height} pixels")
    print(f"Channels       : {channel}")
    print(f"Total Pixels   : {total_pixel}")
    print(f"File Size      : {file_size:.2f} KB")
    print(f"Image Shape    : {img.shape}")
    print(f"Data Type      : {img.dtype}")

    cv2.imshow("Image",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
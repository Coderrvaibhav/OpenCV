import cv2

img = cv2.imread("Chota_Bheem.jpg")

if img is None:
    print("Image is not found")
else:
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    cv2.imshow("Original Image",img)
    cv2.imshow("gray sclae image",gray)
    cv2.imwrite("graysclale_image.jpg",gray)
    print("Image saved")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
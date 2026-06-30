import cv2
img = cv2.imread("Chota_Bheem.jpg")

if img is None:
    print("Image is not found")
else:
    hight , width = img.shape[:2]
    print(f"oringinal hight : {hight}")
    print(f"Original width : {width}")

    new_hight = int(input("Enter New hight"))
    new_width = int(input("Enter New width"))

    
    resized_img = cv2.resize(img,(new_width,new_hight))
    
    cv2.imwrite("resized_image.jpg", resized_img)

    cv2.imshow("Original image", img)
    cv2.imshow("resized image", resized_img)

   

    cv2.waitKey()
    cv2.destroyAllWindows()
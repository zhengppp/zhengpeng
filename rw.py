import cv2
img=cv2.imread("images/children.jpg")
img.shape
print(img.shape)
img_dtype=img.dtype
print(img_dtype)
(b,g,r)=img[16,40]
print(b,g,r)
b=img[16,40,0]
b
g=img[16,40,1]
g
r=img[16,40,2]
r
img[16,40]=(0,0,255)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

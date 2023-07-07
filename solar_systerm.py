import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Add text for each planet
cv2.putText(img, "Mercury", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Venus", (250, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Earth", (450, 380), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Mars", (570, 220), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Jupiter", (380, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Saturn", (350, 670), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Uranus", (700, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Neptune", (900, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)
# Save the final image
cv2.imwrite("Solar_systemwithname.jpg", img)

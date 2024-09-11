import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 1 to 10
x = np.linspace(1, 10, 100)

# Calculate the corresponding y values using the log function
y = np.log(x)

# Plot the log function
plt.plot(x, y)

# Add labels and title to the plot
plt.xlabel('x')
plt.ylabel('log(x)')
plt.title('Plot of the Log Function')

# Display the plot
plt.show()








import cv2 

cam = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture device
    ret, frame = cam.read()
    
    # Display the frame in a window
    cv2.imshow('frame', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and destroy the window
cam.release()
cv2.destroyAllWindows()










import cv2
import numpy as np

# Open a video capture device
cap = cv2.VideoCapture(0)

# Create multiple windows for displaying the image
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Gray', cv2.WINDOW_NORMAL)
cv2.namedWindow('Canny', cv2.WINDOW_NORMAL)

while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection to the grayscale frame
    edges = cv2.Canny(gray, 100, 200)
    
    # Display the frames in their respective windows
    cv2.imshow('Original', frame)
    cv2.imshow('Gray', gray)
    cv2.imshow('Canny', edges)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and destroy the windows
cap.release()
cv2.destroyAllWindows()
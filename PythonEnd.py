import cv2
import numpy as np
import serial

def dotMatrix(address):
    # Load your image
    #'D:\\CET\\Extrs\\Photos\\Sigma.jpg'
    image = cv2.imread(address)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define the dot size (radius) and spacing
    dot_size = 5
    dot_spacing = 10

    # Get the image dimensions
    height, width = gray_image.shape

    # Create a blank white canvas
    dot_matrix = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Initialize a list to store dot center coordinates
    dot_centers = []

    # Loop through the image and place dots based on pixel intensity
    for y in range(0, height, dot_spacing):
        for x in range(0, width, dot_spacing):
                        # Calculate the center of the dot
            center = (x, y)
        
                        # Calculate the average pixel intensity in the neighborhood of the dot
            avg_intensity = np.mean(gray_image[y:y+dot_spacing, x:x+dot_spacing])
        
                        # Set the color of the dot based on the pixel intensity
            if avg_intensity>240:
                avg_intensity=255
                color = (avg_intensity, avg_intensity, avg_intensity)

                        # Draw a dot on the dot matrix
                cv2.circle(dot_matrix, center, dot_size, color, -1)
            else:
                avg_intensity=0
                color = (avg_intensity, avg_intensity, avg_intensity)

                        # Draw a dot on the dot matrix
                cv2.circle(dot_matrix, center, dot_size, color, -1)

                        # Append the center coordinates to the list
                dot_centers.append(center)
                global listx,listy
                listx=[]
                listy=[]
                for i in center:
                   listx.append(center[0]) # X coordinates
                   listy.append(center[1]) # Y coordinates
                # Display the dot matrix image
                new_height=800
                new_width=800
                resized_image = cv2.resize(dot_matrix, (new_width, new_height))

                cv2.imshow('Resized Image', resized_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                # Save the dot matrix image to a file
                cv2.imwrite('dot_matrix_image.png', dot_matrix)

                print("Phase 1 completed")
def transferData(listX):
    # Convert the first 32 integers to strings
    string_list = [str(integer) for integer in listX[:32]]
    string_list.append('\n')
    # Remove the first 32 integers from the original list
    del listX[:32]
    result_string = " ".join(string_list)

    # Print the result
    print(result_string)

    ser.write(result_string.encode()) #converts it into stream of bits


# Define the serial port and baud rate
serial_port = 'COM5'  # Replace with the correct serial port for your Arduino
baud_rate = 9600  # Match this with your Arduino's Serial.begin() setting

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)
address=input("enter the adress of the image : ")
dotMatrix(address)
try:
    print("Hi")
    transferData(listx)
    while ser.in_waiting == 0:
        print("Waiting")
    while ser.in_waiting > 0:
        transferData(listy)
    while ser.in_waiting == 0:
        print("Waiting")
    while ser.in_waiting > 0:
        break #End of iteration
        
except KeyboardInterrupt:
    ser.close()
    print("Serial port closed.")

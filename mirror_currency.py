import cv2

def mirror_image_manual(image):

    # Get image dimensions
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2] if len(image.shape) == 3 else 1
    
    # Create a new image with same dimensions
    if channels == 3:
        mirrored = image.copy()  # Create a copy to work with
    else:
        mirrored = image.copy()
    
    # Manually flip the image horizontally by swapping pixels
    for row in range(height):
        for col in range(width // 2):  # Only need to go halfway
            # Swap pixels from left and right sides
            temp = mirrored[row, col].copy()
            mirrored[row, col] = mirrored[row, width - 1 - col]
            mirrored[row, width - 1 - col] = temp
    
    return mirrored

def main():
    # Read the Pakistani currency note image
    # You'll need to place your image file in the same directory and update the filename
    image_path = "pakistani_note.jpg"  # Update this with your actual image filename
    
    # Read the image using cv2.imread
    original_image = cv2.imread(image_path)
    
    if original_image is None:
        print(f"Error: Could not load image from {image_path}")
        print("Please make sure the image file exists in the current directory.")
        return
    
    # Apply our manual mirror function
    mirrored_image = mirror_image_manual(original_image)
    
    # Display original image
    cv2.imshow("Original Pakistani Currency Note", original_image)
    
    # Display mirrored image
    cv2.imshow("Mirrored Pakistani Currency Note", mirrored_image)
    
    # Save the mirrored image
    cv2.imwrite("mirrored_pakistani_note.jpg", mirrored_image)
    print("Mirrored image saved as 'mirrored_pakistani_note.jpg'")
    
    # Wait for key press and close windows
    print("Press any key to close the windows...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

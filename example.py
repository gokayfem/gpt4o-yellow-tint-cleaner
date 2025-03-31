from yellow_tint_cleaner import auto_adjust
from PIL import Image
import os

def process_image(input_path, output_path, strength=100, brightness=0, contrast=0, 
                 saturation=0, red=0, green=0, blue=0, mode='RGB'):
    """
    Process an image using the yellow tint cleaner.
    
    Args:
        input_path (str): Path to input image
        output_path (str): Path to save output image
        strength (int): Overall adjustment strength (0-100)
        brightness (int): Brightness adjustment (-100 to 100)
        contrast (int): Contrast adjustment (-100 to 100)
        saturation (int): Saturation adjustment (-100 to 100)
        red (int): Red channel adjustment (-100 to 100)
        green (int): Green channel adjustment (-100 to 100)
        blue (int): Blue channel adjustment (-100 to 100)
        mode (str): Processing mode ('RGB', 'lum + sat', 'luminance', 'saturation', 'mono')
    """
    try:
        # Load the image
        input_image = Image.open(input_path)
        
        # Apply adjustments
        adjusted_image = auto_adjust(
            input_image,
            strength=strength,
            brightness=brightness,
            contrast=contrast,
            saturation=saturation,
            red=red,
            green=green,
            blue=blue,
            mode=mode
        )
        
        # Save the result
        adjusted_image.save(output_path)
        print(f"Successfully processed image: {output_path}")
        
    except Exception as e:
        print(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    # Example usage
    input_image = "input.png"  # Replace with your input image path
    output_image = "output.png"  # Replace with your desired output path
    
    # Process the image with default settings
    process_image(input_image, output_image)
    
    # Example with custom settings
    process_image(
        input_image,
        "output_custom.png",
        strength=80,
        brightness=10,
        contrast=5,
        saturation=-5,
        red=-10,
        green=0,
        blue=5,
        mode='RGB'
    ) 
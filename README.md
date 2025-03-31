# Yellow Tint Cleaner

A Python-based image processing tool that helps remove yellow tints from images while preserving image quality. This tool provides various image adjustment capabilities including brightness, contrast, saturation, and color channel adjustments.

## Features

- Automatic image normalization and enhancement
- Multiple color space support (RGB, RGBA, YCbCr, LAB, HSV)
- Adjustable parameters for:
  - Overall adjustment strength
  - Brightness
  - Contrast
  - Saturation
  - Individual color channel adjustments (Red, Green, Blue)
- Multiple processing modes:
  - RGB mode
  - Luminance + Saturation mode
  - Luminance-only mode
  - Saturation-only mode
  - Monochrome mode
- Blend mode support for image adjustments
- Gamma correction capabilities
- Histogram equalization for improved image quality

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/yellow_tint_cleaner.git
cd yellow_tint_cleaner
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from yellow_tint_cleaner import auto_adjust
from PIL import Image

# Load an image
input_image = Image.open("input.png")

# Apply adjustments
adjusted_image = auto_adjust(
    input_image,
    strength=100,    # Full strength
    brightness=0,    # No brightness adjustment
    contrast=0,      # No contrast adjustment
    saturation=0,    # No saturation adjustment
    red=0,          # No red adjustment
    green=0,        # No green adjustment
    blue=0,         # No blue adjustment
    mode='RGB'      # Process in RGB mode
)

# Save the result
adjusted_image.save("output.png")
```

## Parameters

- `strength` (0-100): Overall strength of the adjustment
- `brightness` (-100 to 100): Brightness adjustment
- `contrast` (-100 to 100): Contrast adjustment
- `saturation` (-100 to 100): Saturation adjustment
- `red` (-100 to 100): Red channel adjustment
- `green` (-100 to 100): Green channel adjustment
- `blue` (-100 to 100): Blue channel adjustment
- `mode`: Processing mode ('RGB', 'lum + sat', 'luminance', 'saturation', 'mono')

## Examples

[Add example images showing before/after results]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Pillow](https://pillow.readthedocs.io/) (PIL Fork)
- Uses NumPy for efficient image processing
- Code adapted from [ComfyUI_LayerStyle](https://github.com/chflame163/ComfyUI_LayerStyle) by chflame163 
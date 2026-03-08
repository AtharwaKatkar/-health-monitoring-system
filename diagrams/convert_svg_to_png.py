#!/usr/bin/env python3
"""Convert SVG files to PNG with proper text rendering"""
import os
import sys

try:
    import cairosvg
except ImportError:
    print("Installing cairosvg...")
    os.system(f"{sys.executable} -m pip install cairosvg --quiet")
    import cairosvg

def convert_svg_to_png(svg_path, png_path, dpi=300):
    """Convert SVG to PNG with high quality"""
    try:
        # Calculate width based on DPI (assuming 8.5x11 inch default, adjust as needed)
        # For better quality, we'll use a large width
        width = int(dpi * 11)  # 11 inches at 300 DPI = 3300 pixels
        
        cairosvg.svg2png(
            url=svg_path,
            write_to=png_path,
            output_width=width,
            output_height=None,  # Maintain aspect ratio
            dpi=dpi
        )
        print(f"✓ Converted {os.path.basename(svg_path)} -> {os.path.basename(png_path)}")
        return True
    except Exception as e:
        print(f"✗ Error converting {svg_path}: {e}")
        return False

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    svg_files = [f for f in os.listdir(script_dir) if f.endswith('.svg')]
    
    if not svg_files:
        print("No SVG files found in current directory")
        sys.exit(1)
    
    print(f"Found {len(svg_files)} SVG files to convert...")
    
    # Remove old PNG files
    for f in os.listdir(script_dir):
        if f.endswith('.png'):
            os.remove(os.path.join(script_dir, f))
            print(f"Removed old {f}")
    
    # Convert each SVG
    success_count = 0
    for svg_file in sorted(svg_files):
        svg_path = os.path.join(script_dir, svg_file)
        png_path = os.path.join(script_dir, svg_file.replace('.svg', '.png'))
        
        if convert_svg_to_png(svg_path, png_path, dpi=300):
            success_count += 1
    
    print(f"\n✓ Successfully converted {success_count}/{len(svg_files)} files")



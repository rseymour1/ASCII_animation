from PIL import Image
import os

def split_gif_to_frames(gif_path, output_dir, limit_frames=100):
    """
    Split a GIF file into individual PNG frames.
    
    Args:
        gif_path (str): Path to the input GIF file
        output_dir (str): Directory where PNG frames will be saved
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the GIF file
    with Image.open(gif_path) as gif:
        # Get the base filename without extension
        base_name = os.path.splitext(os.path.basename(gif_path))[0]
        
        # Initialize frame counter
        frame_count = 0
        
        try:
            while True:
                if frame_count >= 100:
                    print(f"Extracted {frame_count} frames from {gif_path}")
                    return
                # Convert current frame to RGB mode (removes transparency)
                current = gif.convert('RGB')
                
                # Save the current frame as PNG
                frame_path = os.path.join(output_dir, f"{base_name}_frame_{frame_count:03d}.png")
                current.save(frame_path, 'PNG')
                
                # Move to next frame
                frame_count += 1
                gif.seek(gif.tell() + 1)
                
        except EOFError:
            # End of frames
            print(f"Extracted {frame_count} frames from {gif_path}")

# Example usage
if __name__ == "__main__":
    gif_path = "downloads/gif_1.gif"
    output_dir = "downloads/gif_1_frames"
    split_gif_to_frames(gif_path, output_dir)
import os
import subprocess
import concurrent.futures

path = [
    "E:/Project Dataset Toko/Dataset/All/No Interest",
    "E:/Project Dataset Toko/Dataset/All/Picking and Putting",
    "E:/Project Dataset Toko/Dataset/All/Picking and Returning",
    "E:/Project Dataset Toko/Dataset/All/Touching",
    "E:/Project Dataset Toko/Dataset/All/Turning to Shelf",
    "E:/Project Dataset Toko/Dataset/All/Viewing"
]
out = [x
    "E:/Project Dataset Toko/Dataset/Processed/No Interest",
    "E:/Project Dataset Toko/Dataset/Processed/Picking and Putting",
    "E:/Project Dataset Toko/Dataset/Processed/Picking and Returning",
    "E:/Project Dataset Toko/Dataset/Processed/Touching",
    "E:/Project Dataset Toko/Dataset/Processed/Turning to Shelf",
    "E:/Project Dataset Toko/Dataset/Processed/Viewing"
]

def extract_frames(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            input_path = os.path.join(input_folder, filename)
            
            command = [
                "ffmpeg", "-hwaccel", "cuda", "-i", input_path, "-vf", "scale=1280:720", os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_frame_%04d.jpg")
            ]
            
            print(f"Extracting frames from {filename} using GPU acceleration...")
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Frames saved in: {output_folder}")

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(extract_frames, path[i], out[i]) for i in range(len(path))]
        concurrent.futures.wait(futures)

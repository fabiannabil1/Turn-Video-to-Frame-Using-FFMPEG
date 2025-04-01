# Video to Frame Extraction Scripts

## Scripts Overview

### Version 1: Flat Output Structure
Processes video files and saves all frames directly in output folders without subdirectories. Frames from multiple videos in the same category will be mixed in one folder.

### Version 2: Organized Subfolder Structure
Processes video files and creates individual subfolders for each video's frames. Maintains better organization by separating frames from different videos.

## Features
- GPU-accelerated processing (NVIDIA CUDA)
- Automatic output folder creation
- Concurrent video processing
- Resolution scaling to 1280x720
- Supports common video formats (.mp4, .avi, .mov, .mkv)

## Prerequisites
- Python 3.6+
- FFmpeg installed and added to system PATH
- NVIDIA GPU with CUDA support (for hardware acceleration)
- Python packages: `os`, `subprocess`, `concurrent.futures`

Install required packages:
```bash
pip install concurrent.futures
```

## Usage

### Version 1: Flat Structure
1. Configure paths:
```python
path = [
    "E:/Project Dataset Toko/Dataset/All/No Interest",
    ...
]
out = [
    "E:/Project Dataset Toko/Dataset/Processed/No Interest",
    ...
]
```
2. Run the script:
```bash
python video_to_frames_v1.py
```

### Version 2: Subfolder Structure
1. Configure paths:
```python
path = ["E:/Project Dataset Toko/Edit-Dataset/Edited/Picking and Putting"]
out = ["E:/Project Dataset Toko/Edit-Dataset/Edited/Picking and Putting"]
```
2. Run the script:
```bash
python video_to_frames_v2.py
```

## Customization
Adjust these parameters in the FFmpeg command:
- Resolution: `scale=1280:720`
- Frame rate (Version 2 only): `fps=25`
- Output format: `.jpg` (can be changed to .png)

Example modification:
```python
command = [
    "ffmpeg", "-hwaccel", "cuda", "-i", input_path, 
    "-vf", "scale=640:360,fps=30",  # Modified resolution and FPS
    os.path.join(frame_folder, "frame_%04d.png")  # Changed output format
]
```

## Notes
1. Ensure FFmpeg binaries are accessible from your system PATH
2. Hardware acceleration will automatically fall back to CPU if CUDA is unavailable
3. Output folders will be created automatically if they don't exist
4. Processing progress is shown in the console
5. Version 2 creates folder structure:
   ```
   Output Folder/
   └── Video Name/
       ├── frame_0001.jpg
       ├── frame_0002.jpg
       └── ...
   ```

For optimal performance, ensure your NVIDIA drivers are up-to-date and verify CUDA support with:
```bash
ffmpeg -hwaccels
```

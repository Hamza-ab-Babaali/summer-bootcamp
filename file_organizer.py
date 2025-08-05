import os

image = ["jpg", "jpeg", "png", "webp", "gif"]
vedios = ["mp4", "mov", "mkv"]
document = ["pdf", "doc", "docx", "txt", "ppt", "json", "xlsx", "pptx"]
audio = ["mp3", "wav"]
archif = ["zip", "rar", "iso"]
python = ["py"]

# windows = input("entrer le path : \n ")
windows = "C:/Users/Admin/Downloads/test"

for i in os.listdir(windows):
    # Ignore directories
    if os.path.isdir(os.path.join(windows, i)):
        continue
    ext = os.path.splitext(i)[-1][1:].lower()
    f = None
    if ext in image:
        f = "images"
    elif ext in vedios:
        f = "vedios"
    elif ext in document:
        f = "documents"
    elif ext in audio:
        f = "audios"
    elif ext in archif:
        f = "archifs"
    elif ext in python:
        f = "python"
    if f:
        folder_path = os.path.join(windows, f)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        src = os.path.join(windows, i)
        dst = os.path.join(folder_path, i)
        # Avoid overwriting files
        if not os.path.exists(dst):
            os.rename(src, dst)
        else:
            print(f"File {dst} already exists, skipping.")





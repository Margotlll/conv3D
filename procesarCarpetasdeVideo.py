import cv2
import os

# Ruta de la carpeta principal que contiene las subcarpetas con videos
input_folder = "C:/Windows/System32/VN2013/src/VioDB/reallife_jpg"

# Obtén la lista de subcarpetas en la carpeta principal
subfolders = [subfolder for subfolder in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, subfolder))]

# Itera a través de las subcarpetas
for subfolder in subfolders:
    subfolder_path = os.path.join(input_folder, subfolder)
    
    # Obtén la lista de archivos de video en la subcarpeta
    video_files = [f for f in os.listdir(subfolder_path) if f.endswith((".mp4", ".avi"))]
    
    # Itera a través de los archivos de video
    for video_file in video_files:
        video_path = os.path.join(subfolder_path, video_file)
        
        # Obtén el nombre del video sin la extensión
        video_name = os.path.splitext(video_file)[0]
        
        # Crea una carpeta con el nombre del video
        video_output_folder = os.path.join(subfolder_path, video_name)
        os.makedirs(video_output_folder, exist_ok=True)
        
        # Abre el video
        cap = cv2.VideoCapture(video_path)
        
        # Lee y guarda cada frame del video
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_filename = f"{video_name}_{frame_count:04d}.jpg"
            frame_path = os.path.join(video_output_folder, frame_filename)
            
            cv2.imwrite(frame_path, frame)
            frame_count += 1
        
        cap.release()
        # Crea un archivo "frames" con el número de frames
        frames_file = os.path.join(video_output_folder, "n_frames")
        with open(frames_file, "w") as f:
            f.write(str(frame_count))
            
        # Elimina el video original
        os.remove(video_path)
        print(f"Frames de '{video_name}' guardados en '{video_output_folder}'")

print("Proceso completado.")

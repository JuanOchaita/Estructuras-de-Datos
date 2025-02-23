import keyboard
import time
import cv2
from CircularQueue import CircularQueue
from memory_profiler import profile

@profile
def menu():
    frames_counter = 0
    buffer = CircularQueue(30)

    for frame in range(30):
        frame_number = 1 + frames_counter * 25
        path = rf"FRAMES\F{frame_number:05d}.jpg"
        buffer.enqueue(path)
        frames_counter += 1

    # Mostrar la primera imagen
    acurrate_path = buffer.dequeue()
    imagen = cv2.imread(acurrate_path)
    cv2.imshow('Imagen', imagen)
    
    print("Press → to next frame\nPress ↑ to see the status of the queue\nPress ESC to exit\n")

    while True:
        if keyboard.is_pressed("right"):
            # Obtener la siguiente ruta de imagen
            acurrate_path = buffer.dequeue()
            if acurrate_path is not None:  # Verificar que hay una imagen
                imagen = cv2.imread(acurrate_path)
                cv2.imshow('Imagen', imagen)  # Mostrar la nueva imagen
            else:
                print("No hay más imágenes en la cola.")
            time.sleep(0.2)

        elif keyboard.is_pressed("up"):
            time.sleep(0.2)
        
        elif keyboard.is_pressed("esc"):
            break

    cv2.destroyAllWindows()  # Asegúrate de cerrar las ventanas al final

menu()

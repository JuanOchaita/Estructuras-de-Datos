import cv2

for frame in range(30):
    frame_number = 1 + frame * 50
    path = rf"FRAMES\F{frame_number:05d}.jpg"
    imagen = cv2.imread(path)

    if imagen is None:
        print(f"Error: No se pudo cargar la imagen en la ruta: {path}")
    else:
        cv2.imshow('Imagen', imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

import sys
import os
from tree import build_tree, print_tree, Tree, Node

# Función para encontrar un archivo dentro del árbol
def find_file_in_tree(tree, filename: str, current_path=""):
    if isinstance(tree, Tree):
        for child in tree.get_children():
            result = find_file_in_tree(child, filename, os.path.join(current_path, tree.name))
            if result:
                return result
    elif isinstance(tree, Node):
        if tree.name == filename:
            # Retornar el Node y la ruta
            return (tree, os.path.join(current_path, tree.name))
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python DirectoryTree.py <ruta>")
        sys.exit(1)

    path = sys.argv[1]

    if not os.path.exists(path):
        print("Error: La ruta especificada no existe.")
        sys.exit(1)

    # Construir el árbol
    tree = build_tree(path)

    # Imprimir el árbol
    print_tree(tree)

    # Pedir el nombre del archivo
    filename = input("\nIngresa el nombre del archivo a buscar dentro del árbol: ")

    # Buscar el archivo
    result = find_file_in_tree(tree, filename)

    if result:
        node, file_path = result
        print(f"\nArchivo encontrado: {os.path.join(path, file_path)}")
        print("\nContenido en binario:")
        print(node.binary_content)
    else:
        print("\nNo se encontró el archivo dentro del árbol.")

import os

# Clase Nodo que representa un archivo
class Node():
    def __init__(self, name: str, binary_content: bytes):
        self.name = name
        self.binary_content = binary_content  # Guardar el contenido en binario
        self.children = []  # No se usa en Node, pero dejamos por compatibilidad

# Clase Árbol que representa una carpeta
class Tree():
    def __init__(self, name: str, path: str = None):
        self.name = name
        self.path = path if path else name  # Guardar la ruta completa
        self.children = []

    def insert_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

# Función para construir el árbol desde un directorio dado
def build_tree(path: str) -> Tree:
    root = Tree(os.path.basename(path) or path, path)  # La raíz es el nombre de la carpeta

    for entry in os.scandir(path):
        if entry.name.startswith('.') or entry.name == 'desktop.ini':
            continue
        
        if entry.is_dir():
            # Si es un directorio, se agrega recursivamente al árbol
            child_tree = build_tree(entry.path)
            root.insert_child(child_tree)
        else:
            # Si es un archivo, se lee en binario y se crea un Node
            with open(entry.path, "rb") as f:
                binary_content = f.read()
            node = Node(entry.name, binary_content)
            root.insert_child(node)

    return root

# Función para imprimir el árbol de forma visual
def print_tree(tree, indent: str = ""):
    if isinstance(tree, Tree):
        print(f"{indent}{tree.name}/")
        for child in tree.get_children():
            print_tree(child, indent + "    ")
    elif isinstance(tree, Node):
        print(f"{indent}{tree.name}")

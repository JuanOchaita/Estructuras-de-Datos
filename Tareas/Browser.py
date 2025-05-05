import keyboard
import time
from Stack import Stack
import cProfile
import pstats
import io

def menu():
    backward = Stack(32)
    search = None
    forward = Stack(32)
    Started = False

    print("\nPress ← to go back\nPress → to go forward\nPress ↑ to see the status of the stacks\nPress ESC to exit\nPress S to search\n")

    while True:
        if keyboard.is_pressed("s"):
            if not Started:
                search = input("Search: ")
                print()
                Started = True
            else:
                backward.push(search)
                search = input("Search: ")
                print()
                time.sleep(0.2)
            
        elif keyboard.is_pressed("up"):
            print(f"{backward} \n")  
            print(f"{search} ← Acurrate", end="")  
            print(f"\n{forward} \n")
            time.sleep(0.2)

        elif keyboard.is_pressed("left") and backward.top != -1:
            forward.push(search)
            search = backward.pop()
            time.sleep(0.2)

        elif keyboard.is_pressed("right") and forward.top != -1:
            backward.push(search)
            search = forward.pop()
            time.sleep(0.2)

        elif keyboard.is_pressed("esc"):
            break

def run_profiled_menu():
    pr = cProfile.Profile()
    pr.enable()
    menu()
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

if __name__ == "__main__":
    run_profiled_menu()

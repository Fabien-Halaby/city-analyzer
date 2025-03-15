from src import Analyser, Menu

if __name__ == "__main__":
    analyser = Analyser()
    menu = Menu(analyser)
    menu.menu()
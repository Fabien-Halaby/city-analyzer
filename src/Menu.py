from src import Analyser

class Menu:
    def __init__(self,analyser):
        self.analyser = analyser
        self.list = {
            1:"WEST CITY...",
            2:"EAST CITY...",
            3:"CITY BY NAME",
            4:"LINK OF CITY",
            5:"EXIT........"
        }
        self.choice = 0

    def get_choice(self):
        self.choice = (input(" \033[1m=> Your choice : \033[0m"))

    def display(self):
        print("\n")
        for k,v in self.list.items():
            print(f"\033[1m {k} - {v}\033[0m")
        print("\n")

    def menu(self):
        while True:
            self.display()
            self.get_choice()

            if self.choice == '1':
                west_city = self.analyser.get_west_city()
                self.analyser.print_city(west_city,w='w')
            elif self.choice == '2':
                east_city = self.analyser.get_east_city()
                self.analyser.print_city(east_city,w='e')
            elif self.choice == '3':
                city_name = input(" \033[1m\t=> Enter city name : \033[0m")
                city = self.analyser.get_city(city_name)
                self.analyser.print_city(city)
            elif self.choice == '4':
                city_name = input(" \033[1m\t=> Enter city name : \033[0m")
                url = self.analyser.get_link(city_name)
                self.analyser.print_url(url)
            elif self.choice == '5':
                break
            else:
                print(" => \033[1m\033[31mInvalid choice!\033[0m")
                continue
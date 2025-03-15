import pandas as pd

class Analyser:
    def __init__(self,path='data/OSMTowns.txt'):
        self.path = path
        self.df = pd.read_csv(path, sep="\t", header=None, names=["city", "lon", "lat"], encoding="utf-8")
        self.dt = pd.DataFrame(self.df)

    def get_city(self,city_name):
        city = self.dt.loc[self.dt['city'] == city_name,['city','lon','lat']]
        if city.empty == False:
            city = city.squeeze().to_dict()
            return city
        else:
            print(f" => \033[1m{city_name}\033[31m not found!\033[0m")
            return None
 
    def get_link(self,city_name):
        url = "https://www.openstreetmap.org/#map=18/"
        all_url = []
        city = self.get_city(city_name)

        if city != None:
            has_dico = any(isinstance(val,dict) for val in city.values());
            if has_dico:
                for i in city['city'].keys():
                    url = f"https://www.openstreetmap.org/#map=18/{city['lat'][i]}/{city['lon'][i]}"
                    all_url.append({city['city'][i]:url})
                return all_url
            else:
                url = f"https://www.openstreetmap.org/#map=18/{city['lat']}/{city['lon']}"
                return [{city['city']:url}]
        else:
            return None
    
    def print_url(self,url):
        if url != None:
            for i in range(len(url)):
                for j in url[i].keys():
                    print(f"\033[1m\033[33m{j} : \033[0m\033[0m\033[1m\033[34m{url[i][j]}\033[0m\033[0m")
        
    def get_west_city(self):
        data =  self.dt.loc[self.dt['lon'].idxmin(),['city','lon','lat']]
        if not data.empty:
            data = data.squeeze().to_dict()
            return data
        else:
            return None
    
    def get_east_city(self):
        data = self.dt.loc[self.dt['lat'].idxmax(),['city','lon','lat']]
        if not data.empty:
            return data.squeeze().to_dict()
        else:
            return None
    
    def print_city(self,city, w='n'):
        s = ""
        
        if city != None:
            if w == 'n':
                s = "  CITY"
            elif w == 'w':
                s = "WEST CITY"
            else:
                s = "EAST CITY"

            has_dico = any(isinstance(val,dict) for val in city.values())
            
            if has_dico and len(city['city']) > 1:
                c = 1
                for i in city['city'].keys():
                    print(f"\033[1m\n    {s} : {c}\033[0m")
                    print("\033[1m\033[33m Name..... : \033[0m\033[0m \033[1m\033[34m" + str(city['city'][i]) + "\033[0m\033[0m")
                    print("\033[1m\033[33m Longitude : \033[0m\033[0m \033[1m\033[34m" + str(city['lon'][i]) + "\033[0m\033[0m")
                    print("\033[1m\033[33m Latitude. : \033[0m\033[0m \033[1m\033[34m" + str(city['lat'][i]) + "\033[0m\033[0m")
                    c += 1
            else:
                print(f"\033[1m\n\t{s}\033[0m")
                print("\033[1m\033[33m Name..... : \033[0m\033[0m \033[1m\033[34m" + str(city['city']) + "\033[0m\033[0m")
                print("\033[1m\033[33m Longitude : \033[0m\033[0m \033[1m\033[34m" + str(city['lon']) + "\033[0m\033[0m")
                print("\033[1m\033[33m Latitude. : \033[0m\033[0m \033[1m\033[34m" + str(city['lat']) + "\033[0m\033[0m")
                  

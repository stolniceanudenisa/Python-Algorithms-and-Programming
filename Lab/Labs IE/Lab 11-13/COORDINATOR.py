from Domain.Passenger import Passenger
from Repository.RepositoryPlanes import PlaneRepository
from Application.Controller import Controller
from UI.Menu import UI


def run():
    #create repo
    repo=PlaneRepository()
    
    passenger1=Passenger('Ana','Pop',5563525)
    passenger2=Passenger('Andreea','Mare',55695145)
    passenger3=Passenger('Andrei','Paunescu',6355985)
    passenger4=Passenger('Bogdan','Crisan',3265552)
    passenger5=Passenger('Marius','Faur',225296)
    passenger6=Passenger('Andrei','Mare', 29965)
        
    list1=[passenger1,passenger2,passenger4]
    list2=[passenger3,passenger5,passenger4]
    list3=[passenger6]   
    
    repo.add_plane("Ak-44", "WizzAir", 55, "Paris", list1)
    repo.add_plane("TR-322", "BlueAir", 122, "Monaco", list2)
    repo.add_plane("SS-989", "BlueAir", 99, "Paris", list3)
    
    #create controller, provide repo
    controller=Controller(repo)
    
    #create UI, provide controller
    ui=UI(controller)
    ui.main_menu()

run()
from UserInterface.console import Console
from Repository import events_repository
from Repository import people_repository
from Service import events_service
from Service import people_service
from Repository import file_data_repository


def start():
    events_repo = events_repository.EventsRepo()
    people_repo = people_repository.PeopleRepo()
    events_serv = events_service.EventsService(events_repo)
    people_serv = people_service.PeopleService(people_repo)
    events_file = file_data_repository.EventsFileRepo("Data/events.txt")
    people_file = file_data_repository.PeopleFileRepo("Data/people.txt")
    console = Console(events_serv, people_serv, events_file, people_file)
    console.console_start()

from Repo.hotel_file_repo import HotelRepoFile
from Services.hotel_service import HotelService
from Tests.test_domain import TestDomain
from Tests.test_repo import TestRepo
from Tests.test_service import TestService
from Ui.console import Console


def main():
    hotel_repo=HotelRepoFile("hotel.txt")
    hotel_service=HotelService(hotel_repo)
    console=Console(hotel_repo,hotel_service)
    console.run_ui()



if __name__ == '__main__':
    TestDomain()
    TestRepo()
    TestService()
    main()

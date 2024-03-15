from Repository.spectacole_repo import SpectacoleRepo
from Service.spectacole_service import SpectacoleService
from UI.console import Console

spectacole_repo = SpectacoleRepo("spectacles.txt")
spectacole_service = SpectacoleService(spectacole_repo)
console = Console(spectacole_service)
console.start()

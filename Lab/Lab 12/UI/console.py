from Domain.entities import Spectacle


class Console:
    def __init__(self, spectacole_service):
        self.__service = spectacole_service

    def start(self):
        print("Welcome to The Spectacle Manager 3000. Type \"help\" for a list of commands.")
        while True:
            cmd = self.__read_command().split()
            if cmd[0] == "help":
                self.__command_list()
            elif cmd[0] == "add":
                spectacol = self.__read_spectacle()
                if spectacol is not None:
                    op = self.__service.add_spectacle(spectacol)
                    if not op:
                        self.__add_error()
                    else:
                        self.__positive_feedback()
            elif cmd[0] == "modify":
                spectacol = self.__read_spectacle()
                if spectacol is not None:
                    op = self.__service.modify_spectacle(spectacol)
                    if not op:
                        self.__modify_error()
                    else:
                        self.__positive_feedback()
            elif cmd[0] == "generate":
                if len(cmd) < 2:
                    self.__generate_error()
                else:
                    self.__service.generate_spectacles(int(cmd[1]))
                    self.__positive_feedback()
            elif cmd[0] == "export":
                if len(cmd) < 2:
                    self.__filename_error()
                else:
                    self.__service.export_spectacles(cmd[1])
                    self.__positive_feedback()
            elif cmd[0] == "exit":
                return
            else:
                self.__invalid_command()

    def __read_command(self):
        """
        Reads a command from console
        If the command is empty calls the function again
        :return: cmd - read command
        """
        cmd = input("Your command: ")
        if len(cmd.split()) == 0:
            return self.__read_command()
        return cmd

    @staticmethod
    def __command_list():
        """
        Prints the list of commands
        """
        print("help - prints this menu")
        print("add - adds a spectacle")
        print("modify - modifies an existing spectacle")
        print("generate <integer> - generates <integer> spectacles")
        print("export <filename> - exports the spectacles to the file, sorted by author and title")
        print("exit - closes the app")

    @staticmethod
    def __read_spectacle():
        """
        Reads a spectacle
        :return: read_spectacle
        :rtype: Spectacle
        """
        title = input("Title = ")
        artist = input("Artist = ")
        genre = input("Genre (Comedy, Concert, Ballet or Other) = ")
        duration = input("Duration = ")
        errors = ""
        genres = ["Comedy", "Concert", "Ballet", "Other"]
        if title == "":
            errors += "Title is empty\n"
        if artist == "":
            errors += "Artist is empty\n"
        if genre not in genres:
            errors += "Genre is empty\n"
        try:
            duration = int(duration)
        except ValueError:
            errors += "Duration must be a positive integer\n"
            print(errors)
            return
        if duration < 1:
            errors += "Duration must be a positive integer\n"
        if errors != "":
            print(errors)
            return None
        read_spectacle = Spectacle(title, artist, genre, duration)
        return read_spectacle

    @staticmethod
    def __add_error():
        print("The spectacle you want to add already exists.")

    @staticmethod
    def __modify_error():
        print("The spectacle you want to modify doesn't exist.")

    @staticmethod
    def __positive_feedback():
        print("Operation was succesful.")

    @staticmethod
    def __generate_error():
        print("Enter a number of spectacles to generate.")

    @staticmethod
    def __filename_error():
        print("Type the name of the file you want to export to.")

    @staticmethod
    def __invalid_command():
        print("Invalid command.")

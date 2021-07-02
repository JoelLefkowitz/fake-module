# We want to have an exception that is distinct from ModuleNotFoundError
class MissingModule(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"Could not find a module with the name {name}.")

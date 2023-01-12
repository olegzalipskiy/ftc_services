import os
from pathlib import Path


class FileSystem:

    @staticmethod
    def get_project_root() -> str:
        return Path(__file__).parent.parent.parent.absolute().__str__()

    @staticmethod
    def get_absolute_path(*path: str) -> str:
        return os.sep.join([FileSystem.get_project_root()] + [*path])
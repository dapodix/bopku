import os.path
from typing import Optional


def _get_default_directory() -> str:
    """Returns the default directory for the Store.  This is intentionally
    underscored to indicate that `Store.get_default_directory` is the intended
    way to get this information.  This is also done so
    `Store.get_default_directory` can be mocked in tests and
    `_get_default_directory` can be tested.
    """
    ret = os.environ.get("PRE_COMMIT_HOME") or os.path.join(
        os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache"),
        "pre-commit",
    )
    return os.path.realpath(ret)


class Store:
    get_default_directory = staticmethod(_get_default_directory)

    def __init__(self, directory: Optional[str] = None) -> None:
        self.directory = directory or Store.get_default_directory()
        self.db_path = os.path.join(self.directory, "db.db")
        self.readonly = os.path.exists(self.directory) and not os.access(
            self.directory, os.W_OK
        )

        if not os.path.exists(self.directory):
            os.makedirs(self.directory, exist_ok=True)
            with open(os.path.join(self.directory, "README"), "w") as f:
                f.write("This directory is maintained by the bopku project.\n")

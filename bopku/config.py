from __future__ import annotations
import os.path
import json
from dacite import from_dict
from dataclasses import asdict, dataclass


def get_config_dir() -> str:
    """Returns the default directory for the Store.  This is intentionally
    underscored to indicate that `Store.get_default_directory` is the intended
    way to get this information.  This is also done so
    `Store.get_default_directory` can be mocked in tests and
    `get_config_dir` can be tested.
    """
    ret = os.environ.get("BOPKU_HOME") or os.path.join(
        os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache"),
        "bopku",
    )
    return os.path.realpath(ret)


def join(to: str, fr: str = get_config_dir()) -> str:
    return os.path.join(fr, to)


@dataclass
class Config:
    app: str = "bopku"
    directory: str = get_config_dir()
    database_uri: str = os.environ.get(
        "DATABASE_URL", "sqlite:///" + join("app.sqlite")
    )
    session: int = 1


CONFIG_FILEPATH = join("config.json")

config = Config()

if not os.path.isfile(CONFIG_FILEPATH):
    with open(CONFIG_FILEPATH, "w") as json_file:
        json.dump(asdict(config), json_file)
else:
    with open(CONFIG_FILEPATH, "r") as json_file:
        config = from_dict(Config, json.load(json_file))

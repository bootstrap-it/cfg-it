import os
from pathlib import Path
from contextlib import suppress

import yaml

import cfg_it.lookups

LOOK_INTO = [
    lambda prop_path: cfg_it.lookups.config_envs(os.environ, prop_path),
    lambda prop_path: cfg_it.lookups.config_file(Path.cwd() / "config.yml", prop_path),
]


def lookup(prop_path, look_into):
    for look_func in look_into:
        with suppress(KeyError):
            return look_func(prop_path)
    else:
        raise LookupError(f"There are no properties with path: {prop_path}")


def init(cls, parent_prop_path=[]):
    instance = cls()
    for prop_name, prop_type in cls.__annotations__.items():
        prop_path = parent_prop_path + [prop_name]
        if hasattr(prop_type, "__annotations__"):
            setattr(instance, prop_name,
                    init(cls=prop_type, parent_prop_path=prop_path))
        else:
            with suppress(LookupError):
                setattr(instance, prop_name, prop_type(lookup(prop_path, cfg_it.LOOK_INTO)))
    return instance

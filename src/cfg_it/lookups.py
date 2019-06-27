import os
from pathlib import Path

import cfg_it.load


def config_file(config_file_path, prop_path):
    return config_dict(config_dict=cfg_it.load.config_file(config_file_path),
                       prop_path=prop_path)


def config_envs(envs_dict, prop_path):
    env_path = "_".join(prop_path).upper()
    return envs_dict[env_path]


def config_dict(config_dict: dict, prop_path: Path):
    sub_config = config_dict
    for path_part in prop_path:
        sub_config = sub_config[path_part]
    return sub_config

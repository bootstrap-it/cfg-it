import cfg_it
import cfg_it.lookups
import cfg_it.load

envs_dict = {
    "ANSWER_TO_THE_UQ": "42",
    "HOST_NAME": "host1.example.com",
    "HOST_IP": "10.0.0.1",
    "ENVS": ["one", "two", "three"]
}

config_dict = {
    "host": {
        "name": "exp.data.com",
        "ip": "34.3.12.2",
    },
    "envs": ["five", "six"],
}

def test_load_file_cfg():
    from pathlib import Path
    cfg_file = cfg_it.load.config_file(Path("tests/test_config.yml"))
    cfg_not_existed = cfg_it.load.config_file(Path("not_existed_file"))
    assert cfg_file["host"]["name"] == "exp.data.com"
    assert cfg_not_existed == {}

def test_lookup_config_dict():
    assert cfg_it.lookups.config_dict(config_dict, ["host", "ip"]) == "34.3.12.2"

def test_lookup_config_envs():
    assert cfg_it.lookups.config_envs(envs_dict, ["host", "name"]) == "host1.example.com"
    assert cfg_it.lookups.config_envs(envs_dict, ["host", "ip"]) == "10.0.0.1"

def test_lookup():
    import os

    look_into = [
        lambda prop_path: cfg_it.lookups.config_envs(os.environ, prop_path),
    ]

    assert cfg_it.lookup(["home"], look_into) == os.environ["HOME"]

def test_cfg_it():
    from typing import List

    test_LOOK_INTO = [
        lambda prop_path: cfg_it.lookups.config_envs(envs_dict, prop_path),
        lambda prop_path: cfg_it.lookups.config_dict(config_dict, prop_path),
    ]
    old_LOOK_INTO, cfg_it.LOOK_INTO = cfg_it.LOOK_INTO, test_LOOK_INTO

    class Host:
        name: str
        ip: str
        role: str = "master"

    @cfg_it.init
    class config:
        host: Host
        # envs: List[str]

    print(config.__dict__["host"].__dict__)
    # assert config.envs == ["one", "two", "three"]
    assert config.host.name == "host1.example.com"
    assert config.host.ip == "10.0.0.1"
    assert config.host.role == "master"

    cfg_it.LOOK_INTO = old_LOOK_INTO
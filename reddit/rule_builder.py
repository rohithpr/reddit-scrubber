import copy

import yaml

from .utils import normalize_sub_name

# Hardcoded default - this will be used as the configuration if a config file is not found
DEFAULT_CONFIG = {"max_age_days": 7, "skip_delete_pattern": ""}


def build_ruleset():
    with open("config.yaml") as fp:
        raw_config = fp.read()
    config = yaml.safe_load(raw_config)
    ruleset = _build_ruleset_from_config(config)
    return ruleset


def _build_ruleset_from_config(config):
    # TODO: make accommodations for configs that don't have all the required keys
    default = config.get("default", copy.copy(DEFAULT_CONFIG))
    ruleset = {
        normalize_sub_name(key): value
        for key, value in config.items()
        if key.startswith("r/")
    }
    ruleset["default"] = default
    return ruleset

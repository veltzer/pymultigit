"""
All configurations for pymakehelper
"""


from pytconf.config import Config, ParamCreator


class ConfigAll(Config):
    """
    Parameters for pymultigit
    """
    verbose = ParamCreator.create_bool(
        help_string="be verbose?",
        default=False,
    )
    quiet = ParamCreator.create_bool(
        help_string="be quiet?",
        default=False,
    )
    stats = ParamCreator.create_bool(
        help_string="show statistics are the end?",
        default=False,
    )
    sort = ParamCreator.create_bool(
        help_string="sort results by project name?",
        default=True,
    )
    regexp = ParamCreator.create_str(
        help_string="what regexp to look for?",
    )

"""
All configurations for pymakehelper
"""


from pytconf.config import Config, ParamCreator


class ConfigDebug(Config):
    """
    Parameters for debug
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


class ConfigGrep(Config):
    """
    Parameters for pymultigit
    """

    regexp = ParamCreator.create_str(
        help_string="what regexp to look for?",
    )

<%!
    import config.version
    import config.project
%>""" version which can be consumed from within the module """
VERSION_STR = "${config.version.version_str}"
DESCRIPTION = "${config.project.description_short}"
APP_NAME = "${config.project.name}"
LOGGER_NAME = "${config.project.name}"

"""Tigase Certbot plugin."""

import os
import logging

import zope.interface

from certbot import errors
from certbot import interfaces
from certbot.plugins import common

logger = logging.getLogger(__name__)


@zope.interface.implementer(interfaces.IInstaller)
@zope.interface.provider(interfaces.IPluginFactory)
class TigaseInstaller(common.Plugin):
    """Tigase installer."""

    description = "Tigase Installer plugin"

    @classmethod
    def add_parser_arguments(cls, add):
        add("home", default="/etc/tigase",
            help="Path to the Tigase installation directory. etc/init.properties must be present there.")

    def prepare(self):  # type: ignore
        """Prepare the plugin.

        Finish up any additional initialization.

        :raises .PluginError:
            when full initialization cannot be completed.
        :raises .MisconfigurationError:
            when full initialization cannot be completed. Plugin will
            be displayed on a list of available plugins.
        :raises .NoInstallationError:
            when the necessary programs/files cannot be located. Plugin
            will NOT be displayed on a list of available plugins.
        :raises .NotSupportedError:
            when the installation is recognized, but the version is not
            currently supported.

        """
        cfgfile = self.get_tigase_config_file()
        if not os.path.isfile(cfgfile):
            raise errors.NoInstallationError("Invalid Tigase installation.")

    def get_tigase_config_file(self):
        return os.path.join(self.conf("home"), "etc", "init.properties")

    def more_info(self):  # type: ignore
        """Human-readable string to help the user.

        Should describe the steps taken and any relevant info to help the user
        decide which plugin to use.

        :rtype str:

        """

    def get_all_names(self):  # type: ignore
        """Returns all names that may be authenticated.

        :rtype: `collections.Iterable` of `str`

        """
        # TODO read vhosts from init.properties

    def deploy_cert(self, domain, cert_path, key_path, chain_path, fullchain_path):
        """Deploy certificate.

        :param str domain: domain to deploy certificate file
        :param str cert_path: absolute path to the certificate file
        :param str key_path: absolute path to the private key file
        :param str chain_path: absolute path to the certificate chain file
        :param str fullchain_path: absolute path to the certificate fullchain
            file (cert plus chain)

        :raises .PluginError: when cert cannot be deployed

        """
        # TODO

    def enhance(self, domain, enhancement, options=None):
        """Perform a configuration enhancement.

        :param str domain: domain for which to provide enhancement
        :param str enhancement: An enhancement as defined in
            :const:`~certbot.constants.ENHANCEMENTS`
        :param options: Flexible options parameter for enhancement.
            Check documentation of
            :const:`~certbot.constants.ENHANCEMENTS`
            for expected options for each enhancement.

        :raises .PluginError: If Enhancement is not supported, or if
            an error occurs during the enhancement.

        """

    def supported_enhancements(self):  # type: ignore
        """Returns a `collections.Iterable` of supported enhancements.

        :returns: supported enhancements which should be a subset of
            :const:`~certbot.constants.ENHANCEMENTS`
        :rtype: :class:`collections.Iterable` of :class:`str`

        """

    def save(self, title=None, temporary=False):
        """Saves all changes to the configuration files.

        Both title and temporary are needed because a save may be
        intended to be permanent, but the save is not ready to be a full
        checkpoint.

        It is assumed that at most one checkpoint is finalized by this
        method. Additionally, if an exception is raised, it is assumed a
        new checkpoint was not finalized.

        :param str title: The title of the save. If a title is given, the
            configuration will be saved as a new checkpoint and put in a
            timestamped directory. `title` has no effect if temporary is true.

        :param bool temporary: Indicates whether the changes made will
            be quickly reversed in the future (challenges)

        :raises .PluginError: when save is unsuccessful

        """

    def rollback_checkpoints(self, rollback=1):
        """Revert `rollback` number of configuration checkpoints.

        :raises .PluginError: when configuration cannot be fully reverted

        """

    def recovery_routine(self):  # type: ignore
        """Revert configuration to most recent finalized checkpoint.

        Remove all changes (temporary and permanent) that have not been
        finalized. This is useful to protect against crashes and other
        execution interruptions.

        :raises .errors.PluginError: If unable to recover the configuration

        """

    def view_config_changes(self):  # type: ignore
        """Display all of the LE config changes.

        :raises .PluginError: when config changes cannot be parsed

        """

    def config_test(self):  # type: ignore
        """Make sure the configuration is valid.

        :raises .MisconfigurationError: when the config is not in a usable state

        """

    def restart(self):  # type: ignore
        """Restart or refresh the server content.

        :raises .PluginError: when server cannot be restarted

        """

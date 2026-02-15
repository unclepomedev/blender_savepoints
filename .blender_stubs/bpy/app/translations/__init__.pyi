# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.app.translations.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


contexts: Any
contexts_C_to_py: Any
locale = 'en_US'
def locale_explode(*args, **kwargs) -> Any:
    """.. method:: locale_explode(locale)

   Return all components and their combinations of the given ISO locale string.

   >>> bpy.app.translations.locale_explode("sr_RS@latin")
   ("sr", "RS", "latin", "sr_RS", "sr@latin")

   For non-complete locales, missing elements will be None.

   :arg locale: The ISO locale string to explode.
   :type msgid: str
   :return: A tuple ``(language, country, variant, language_country, language@variant)``.



    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.translations.html"""
    ...

locales: Any
def pgettext(*args, **kwargs) -> Any:
    """.. method:: pgettext(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt).

   .. note::
      The ``(msgid, msgctxt)`` parameters order has been switched compared to gettext function, to allow
      single-parameter calls (context then defaults to BLT_I18NCONTEXT_DEFAULT).

   .. note::
      You should really rarely need to use this function in regular addon code, as all translation should be
      handled by Blender internal code. The only exception are string containing formatting (like "File: %r"),
      but you should rather use :func:`pgettext_iface`/:func:`pgettext_tip` in those cases!

   .. note::
      Does nothing when Blender is built without internationalization support (hence always returns ``msgid``).

   :arg msgid: The string to translate.
   :type msgid: str
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or msgid if no translation was found).



    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.translations.html"""
    ...

def pgettext_data(*args, **kwargs) -> Any:
    """.. method:: pgettext_data(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt), if new data name's translation is enabled.

   .. note::
      See :func:`pgettext` notes.

   :arg msgid: The string to translate.
   :type msgid: str
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or ``msgid`` if no translation was found).



    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.translations.html"""
    ...

def pgettext_iface(*args, **kwargs) -> Any:
    """.. method:: pgettext_iface(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt), if labels' translation is enabled.

   .. note::
      See :func:`pgettext` notes.

   :arg msgid: The string to translate.
   :type msgid: str
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or msgid if no translation was found).



    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.translations.html"""
    ...

def pgettext_n(*args, **kwargs) -> Any:
    """.. method:: pgettext_n(msgid, msgctxt=None)

   Extract the given msgid to translation files. This is a no-op function that will only mark the string to extract, but not perform the actual translation.

   .. note::
      See :func:`pgettext` notes.

   :arg msgid: The string to extract.
   :type msgid: str
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The original string.



    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.translations.html"""
    ...

def pgettext_rpt(*args, **kwargs) -> Any:
    """.. method:: pgettext_rpt(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt), if reports' translation is enabled.

   .. note::
      See :func:`pgettext` notes.

   :arg msgid: The string to translate.
   :type msgid: str
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or msgid if no translation was found).



    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.translations.html"""
    ...

def pgettext_tip(*args, **kwargs) -> Any:
    """.. method:: pgettext_tip(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt), if tooltips' translation is enabled.

   .. note::
      See :func:`pgettext` notes.

   :arg msgid: The string to translate.
   :type msgid: str
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or msgid if no translation was found).



    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.translations.html"""
    ...

def register(*args, **kwargs) -> Any:
    """.. method:: register(module_name, translations_dict)

   Registers an addon's UI translations.

   .. note::
      Does nothing when Blender is built without internationalization support.

   :arg module_name: The name identifying the addon.
   :type module_name: str
   :arg translations_dict: A dictionary built like that:
      ``{locale: {msg_key: msg_translation, ...}, ...}``
   :type translations_dict: dict[str, dict[str, str]]



    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.translations.html"""
    ...

def unregister(*args, **kwargs) -> Any:
    """.. method:: unregister(module_name)

   Unregisters an addon's UI translations.

   .. note::
      Does nothing when Blender is built without internationalization support.

   :arg module_name: The name identifying the addon.
   :type module_name: str



    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.translations.html"""
    ...

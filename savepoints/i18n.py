# SPDX-License-Identifier: GPL-3.0-or-later
"""Blender integration for automatic and manually overridden translations."""

from __future__ import annotations

from typing import Literal

import bpy

from .translations import (
    TRANSLATION_CONTEXT,
    build_runtime_translations,
    resolve_language,
    translate_for_locale,
)

AUTO_LANGUAGE = "AUTO"
TRANSLATION_DOMAIN = __package__ or "savepoints"
TranslationKind = Literal["interface", "report", "tooltip"]


class TranslatedOperatorMixin:
    """Provide operator tooltips in the active SavePoints language."""

    bl_translation_context = TRANSLATION_CONTEXT
    translation_description = ""

    @classmethod
    def description(cls, _context, _properties):
        return tooltip(cls.translation_description)


def _language_preference() -> str:
    """Return the add-on language preference without assuming an install key."""
    try:
        addons = bpy.context.preferences.addons
        addon = addons.get(TRANSLATION_DOMAIN)
        if addon is None:
            for key, candidate in addons.items():
                if key.endswith("savepoints"):
                    addon = candidate
                    break
        preferences = getattr(addon, "preferences", None)
        return getattr(preferences, "ui_language", AUTO_LANGUAGE)
    except Exception:
        return AUTO_LANGUAGE


def translate(
    message: str,
    *,
    kind: TranslationKind = "interface",
    language: str | None = None,
) -> str:
    """Translate from one effective language: manual, or Blender in auto mode."""
    selected = language if language is not None else _language_preference()
    effective_language = resolve_language(
        selected,
        getattr(bpy.app.translations, "locale", "en_US"),
    )
    return translate_for_locale(message, effective_language)


def iface(message: str, *, language: str | None = None) -> str:
    return translate(message, kind="interface", language=language)


def report(message: str, *, language: str | None = None) -> str:
    return translate(message, kind="report", language=language)


def tooltip(message: str, *, language: str | None = None) -> str:
    return translate(message, kind="tooltip", language=language)


def _known_locales() -> set[str]:
    """Return locale IDs across Blender versions and locale collection shapes."""
    locale_ids = {getattr(bpy.app.translations, "locale", "")}
    try:
        for item in bpy.app.translations.locales:
            if isinstance(item, str):
                locale_ids.add(item)
            elif item and isinstance(item[0], str):
                locale_ids.add(item[0])
    except (AttributeError, TypeError):
        pass
    return {locale for locale in locale_ids if locale}


def refresh() -> None:
    """Rebuild runtime catalogs after changing SavePoints' language."""
    unregister()
    catalog = build_runtime_translations(_language_preference(), _known_locales())
    bpy.app.translations.register(TRANSLATION_DOMAIN, catalog)


def register() -> None:
    """Register catalogs for the saved automatic or manual language mode."""
    refresh()


def unregister() -> None:
    try:
        bpy.app.translations.unregister(TRANSLATION_DOMAIN)
    except (RuntimeError, ValueError):
        pass

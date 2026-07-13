import ast
import importlib.util
import string
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "savepoints" / "translations.py"

spec = importlib.util.spec_from_file_location(
    "savepoints_translation_catalog", CATALOG_PATH
)
if spec is None or spec.loader is None:
    raise RuntimeError("Could not load SavePoints translation catalog")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


def placeholders(value):
    return {
        field_name
        for _, field_name, _, _ in string.Formatter().parse(value)
        if field_name is not None
    }


class TestTranslationCatalog(unittest.TestCase):
    def test_supported_catalogs_have_matching_messages_and_placeholders(self):
        self.assertEqual(set(catalog.ZH_HANS), set(catalog.JA_JP))

        for message in catalog.ZH_HANS:
            expected = placeholders(message)
            self.assertEqual(expected, placeholders(catalog.ZH_HANS[message]), message)
            self.assertEqual(expected, placeholders(catalog.JA_JP[message]), message)

    def test_locale_aliases(self):
        for locale in ("zh_HANS", "zh_CN", "zh-Hans", "zh_TW"):
            self.assertEqual("zh_HANS", catalog.normalize_locale(locale))
        self.assertEqual("ja_JP", catalog.normalize_locale("ja_JP"))
        self.assertEqual("en_US", catalog.normalize_locale("en_US"))

    def test_single_effective_language_rule(self):
        self.assertEqual("zh_HANS", catalog.resolve_language("AUTO", "zh_CN"))
        self.assertEqual("ja_JP", catalog.resolve_language("AUTO", "ja_JP"))
        self.assertEqual("en_US", catalog.resolve_language("AUTO", "fr_FR"))
        self.assertEqual("ja_JP", catalog.resolve_language("ja_JP", "zh_CN"))
        self.assertEqual("en_US", catalog.resolve_language("en_US", "zh_CN"))

    def test_manual_runtime_catalog_is_independent_from_blender_locale(self):
        runtime = catalog.build_runtime_translations(
            "ja_JP", {"en_US", "zh_HANS", "ja_JP", "fr_FR"}
        )
        key = (catalog.TRANSLATION_CONTEXT, "Delete")
        for locale in ("en_US", "zh_HANS", "ja_JP", "fr_FR"):
            self.assertEqual("削除", runtime[locale][key])

        english = catalog.build_runtime_translations("en_US", {"zh_HANS"})
        self.assertEqual("Delete", english["zh_HANS"][key])

    def test_catalog_uses_isolated_context(self):
        for translations in catalog.TRANSLATIONS.values():
            self.assertTrue(translations)
            self.assertTrue(
                all(key[0] == catalog.TRANSLATION_CONTEXT for key in translations)
            )

    def test_visible_rna_properties_use_isolated_context(self):
        missing = []
        for path in (ROOT / "savepoints").rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if not (
                    isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and node.func.attr.endswith("Property")
                ):
                    continue
                keywords = {keyword.arg: keyword.value for keyword in node.keywords}
                is_visible = any(
                    isinstance(keywords.get(field), ast.Constant)
                    and bool(keywords[field].value)
                    for field in ("name", "description")
                )
                if is_visible and "translation_context" not in keywords:
                    missing.append(f"{path.relative_to(ROOT)}:{node.lineno}")
        self.assertEqual([], missing)

    def test_all_operators_use_dynamic_translated_tooltips(self):
        missing_mixin = []
        missing_description = []
        for path in (ROOT / "savepoints").rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in tree.body:
                if not isinstance(node, ast.ClassDef):
                    continue
                is_operator = any(
                    isinstance(base, ast.Attribute) and base.attr == "Operator"
                    for base in node.bases
                )
                if not is_operator:
                    continue
                has_mixin = any(
                    isinstance(base, ast.Name) and base.id == "TranslatedOperatorMixin"
                    for base in node.bases
                )
                has_description = any(
                    isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and item.name == "description"
                    for item in node.body
                ) or any(
                    isinstance(item, ast.Assign)
                    and any(
                        isinstance(target, ast.Name)
                        and target.id == "translation_description"
                        for target in item.targets
                    )
                    for item in node.body
                )
                location = f"{path.relative_to(ROOT)}:{node.lineno}"
                if not has_mixin:
                    missing_mixin.append(location)
                if not has_description:
                    missing_description.append(location)
        self.assertEqual([], missing_mixin)
        self.assertEqual([], missing_description)

    def test_raw_rna_controls_have_no_fixed_language_description(self):
        descriptions = {}
        raw_controls = []
        for path in (ROOT / "savepoints").rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, ast.AnnAssign) and isinstance(
                    node.target, ast.Name
                ):
                    call = node.value
                    property_name = node.target.id
                elif (
                    isinstance(node, ast.Assign)
                    and len(node.targets) == 1
                    and isinstance(node.targets[0], ast.Attribute)
                ):
                    call = node.value
                    property_name = node.targets[0].attr
                else:
                    call = None
                    property_name = ""

                if (
                    isinstance(call, ast.Call)
                    and isinstance(call.func, ast.Attribute)
                    and call.func.attr.endswith("Property")
                ):
                    description = next(
                        (
                            keyword.value.value
                            for keyword in call.keywords
                            if keyword.arg == "description"
                            and isinstance(keyword.value, ast.Constant)
                            and isinstance(keyword.value.value, str)
                        ),
                        "",
                    )
                    descriptions.setdefault(property_name, set()).add(description)

                if (
                    isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and node.func.attr == "prop"
                    and len(node.args) >= 2
                    and isinstance(node.args[1], ast.Constant)
                    and isinstance(node.args[1].value, str)
                ):
                    raw_controls.append(
                        (node.args[1].value, f"{path.relative_to(ROOT)}:{node.lineno}")
                    )

        offenders = [
            location
            for property_name, location in raw_controls
            if any(descriptions.get(property_name, {""}))
        ]
        self.assertEqual([], offenders)

    def test_layout_text_literals_do_not_bypass_translation(self):
        offenders = []
        for path in (ROOT / "savepoints").rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if not (
                    isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and node.func.attr in {"label", "menu", "operator", "prop"}
                ):
                    continue
                for keyword in node.keywords:
                    if (
                        keyword.arg == "text"
                        and isinstance(keyword.value, ast.Constant)
                        and isinstance(keyword.value.value, str)
                        and keyword.value.value
                    ):
                        offenders.append(f"{path.relative_to(ROOT)}:{node.lineno}")
        self.assertEqual([], offenders)

    def test_enum_labels_and_descriptions_are_cataloged(self):
        messages = set()
        for path in (ROOT / "savepoints").rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if not (
                    isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and node.func.attr == "EnumProperty"
                ):
                    continue
                items = next(
                    (
                        keyword.value
                        for keyword in node.keywords
                        if keyword.arg == "items"
                    ),
                    None,
                )
                if not isinstance(items, (ast.List, ast.Tuple)):
                    continue
                for item in items.elts:
                    if not isinstance(item, ast.Tuple) or len(item.elts) < 3:
                        continue
                    for value in item.elts[1:3]:
                        if (
                            isinstance(value, ast.Constant)
                            and isinstance(value.value, str)
                            and value.value
                        ):
                            messages.add(value.value)

        native_or_technical = {"English", "简体中文", "日本語", "PNG", "JPEG"}
        missing = sorted(messages - set(catalog.ZH_HANS) - native_or_technical)
        self.assertEqual([], missing)

    def test_tooltip_registries_and_help_messages_are_cataloged(self):
        messages = set()
        for path in (ROOT / "savepoints").rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign) and any(
                    isinstance(target, ast.Name) and target.id.endswith("TOOLTIPS")
                    for target in node.targets
                ):
                    if isinstance(node.value, ast.Dict):
                        for value in node.value.values:
                            if isinstance(value, ast.Constant) and isinstance(
                                value.value, str
                            ):
                                messages.add(value.value)
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    if node.func.id == "draw_property_with_help":
                        for keyword in node.keywords:
                            if (
                                keyword.arg == "message"
                                and isinstance(keyword.value, ast.Constant)
                                and isinstance(keyword.value.value, str)
                            ):
                                messages.add(keyword.value.value)
                if isinstance(node, ast.Assign) and any(
                    isinstance(target, ast.Attribute) and target.attr == "message"
                    for target in node.targets
                ):
                    if isinstance(node.value, ast.Constant) and isinstance(
                        node.value.value, str
                    ):
                        messages.add(node.value.value)

        missing = sorted(messages - set(catalog.ZH_HANS) - {""})
        self.assertEqual([], missing)

    def test_reports_do_not_expose_raw_exception_strings(self):
        offenders = []
        for path in (ROOT / "savepoints").rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if not (
                    isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and node.func.attr == "report"
                    and len(node.args) >= 2
                ):
                    continue
                message = node.args[1]
                if (
                    isinstance(message, ast.Call)
                    and isinstance(message.func, ast.Name)
                    and message.func.id == "str"
                ):
                    offenders.append(f"{path.relative_to(ROOT)}:{node.lineno}")
        self.assertEqual([], offenders)

    def test_all_explicit_translation_calls_are_cataloged(self):
        messages = set()
        for path in (ROOT / "savepoints").rglob("*.py"):
            if path.name == "translations.py":
                continue
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    if node.func.id in {"iface", "rpt", "tooltip"} and node.args:
                        value = node.args[0]
                        if (
                            isinstance(value, ast.Constant)
                            and isinstance(value.value, str)
                            and value.value
                        ):
                            messages.add(value.value)
                elif isinstance(node, ast.Call) and isinstance(
                    node.func, ast.Attribute
                ):
                    if node.func.attr.endswith("Property"):
                        for keyword in node.keywords:
                            if keyword.arg not in {"name", "description"}:
                                continue
                            if isinstance(keyword.value, ast.Constant) and isinstance(
                                keyword.value.value, str
                            ):
                                if keyword.value.value:
                                    messages.add(keyword.value.value)
                elif isinstance(node, ast.Assign):
                    if any(
                        isinstance(target, ast.Name)
                        and target.id == "translation_description"
                        for target in node.targets
                    ):
                        if (
                            isinstance(node.value, ast.Constant)
                            and isinstance(node.value.value, str)
                            and node.value.value
                        ):
                            messages.add(node.value.value)
                    if any(
                        isinstance(target, ast.Name)
                        and target.id in {"bl_label", "bl_description"}
                        for target in node.targets
                    ):
                        if isinstance(node.value, ast.Constant) and isinstance(
                            node.value.value, str
                        ):
                            messages.add(node.value.value)

        untranslated_brand_strings = {"SavePoints"}
        missing = sorted(messages - set(catalog.ZH_HANS) - untranslated_brand_strings)
        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main()

"""Guard QuickShop version parsing and protected-block behavior against regressions."""

from pathlib import Path
import re
import unittest

SOURCE = (Path(__file__).resolve().parents[1] / "src/main/java/com/xzavier0722/mc/plugin/slimeglue/module/QuickShopModule.java")


class QuickShopVersionContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")

    def test_legacy_components_are_read_only_inside_legacy_guard(self):
        source = self.source
        guard = source.index("if (major < 5)")
        major = source.index("Integer.parseInt(splitVersion[0])")
        minor = source.index("Integer.parseInt(splitVersion[1])")
        patch = source.index("Integer.parseInt(splitVersion[2])")
        self.assertLess(major, guard)
        self.assertLess(guard, minor)
        self.assertLess(minor, patch)
        self.assertNotIn("splitVersion[3]", source)

    def test_release_suffix_is_separated_before_numeric_parse(self):
        self.assertIn('version.split("-", 2)[0].split("\\\\.")', self.source)

    def test_legacy_api_selection_is_unchanged(self):
        self.assertIn("if (sub >= 8 && last >= 2)", self.source)
        self.assertIn('getDeclaredMethod("getShop", Location.class)', self.source)
        self.assertIn('getDeclaredMethod("getShopWithCaching", Location.class)', self.source)

    def test_protection_and_owner_paths_are_unchanged(self):
        self.assertIn("return !isQuickshop(location);", self.source)
        self.assertIn("player.getUniqueId().equals(getQuickshopOwner(location))", self.source)
        self.assertIn("return shop == null ? null : shop.getOwner();", self.source)


if __name__ == "__main__":
    unittest.main()

"""Source contracts complement the executable Java QuickShop version tests."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "src/main/java/com/xzavier0722/mc/plugin/slimeglue/module/QuickShopModule.java"
PARSER = ROOT / "src/main/java/com/xzavier0722/mc/plugin/slimeglue/module/QuickShopVersion.java"


class QuickShopVersionContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = MODULE.read_text(encoding="utf-8")
        cls.parser = PARSER.read_text(encoding="utf-8")

    def test_module_uses_parser_and_guards_legacy_reflection(self):
        self.assertIn("QuickShopVersion.parse(version)", self.module)
        self.assertIn("if (quickShopVersion.isLegacy())", self.module)
        self.assertIn("if (quickShopVersion.useLegacyGetShop())", self.module)
        self.assertNotIn("splitVersion[3]", self.module)

    def test_parser_preserves_four_part_threshold(self):
        self.assertIn("int patch = Integer.parseInt(parts[2])", self.parser)
        self.assertIn("int build = parts.length == 4 ? Integer.parseInt(parts[3]) : 0", self.parser)
        self.assertIn("return patch >= 8 && build >= 2;", self.parser)

    def test_legacy_api_selection_is_unchanged(self):
        self.assertIn('getDeclaredMethod("getShop", Location.class)', self.module)
        self.assertIn('getDeclaredMethod("getShopWithCaching", Location.class)', self.module)

    def test_protection_and_owner_paths_are_unchanged(self):
        self.assertIn("return !isQuickshop(location);", self.module)
        self.assertIn("player.getUniqueId().equals(getQuickshopOwner(location))", self.module)
        self.assertIn("return shop == null ? null : shop.getOwner();", self.module)


if __name__ == "__main__":
    unittest.main()

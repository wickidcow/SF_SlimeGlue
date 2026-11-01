package com.xzavier0722.mc.plugin.slimeglue.module;

/** Dependency-free executable regression tests for QuickShop version selection. */
public final class QuickShopVersionTest {
    private static int checks;

    private static void check(String version, boolean legacy, boolean getShop) {
        QuickShopVersion parsed = QuickShopVersion.parse(version);
        if (parsed.isLegacy() != legacy || (legacy && parsed.useLegacyGetShop() != getShop)) {
            throw new AssertionError("Unexpected QuickShop API selection for " + version);
        }
        checks++;
    }

    private static void rejects(String version) {
        try {
            QuickShopVersion.parse(version);
            throw new AssertionError("Accepted malformed legacy QuickShop version: " + version);
        } catch (IllegalArgumentException expected) {
            checks++;
        }
    }

    public static void main(String[] args) {
        check("4.0.7.9", true, false);
        check("4.0.8", true, false);
        check("4.0.8.1", true, false);
        check("4.0.8.2", true, true);
        check("4.0.9.2", true, true);
        check("4.0.8.2-SNAPSHOT", true, true);
        check("5.0.0", false, false);
        check("5.1.2.5", false, false);
        check("6.2.0.11", false, false);
        rejects("4.0");
        rejects("4.0.x");
        rejects("4.0.8.x");
        rejects("4.0.8.2.1");
        rejects("unknown");
        System.out.println("QuickShop version regression: " + checks + " checks passed");
    }
}

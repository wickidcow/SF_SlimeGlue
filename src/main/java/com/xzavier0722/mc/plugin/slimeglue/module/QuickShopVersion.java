package com.xzavier0722.mc.plugin.slimeglue.module;

/**
 * Parses QuickShop's legacy four-component versions without imposing that
 * format on modern QuickShop releases.
 */
final class QuickShopVersion {
    private final int major;
    private final int patch;
    private final int build;

    private QuickShopVersion(int major, int patch, int build) {
        this.major = major;
        this.patch = patch;
        this.build = build;
    }

    static QuickShopVersion parse(String version) {
        String[] parts = version.split("-", 2)[0].split("\\.", -1);
        int major = Integer.parseInt(parts[0]);

        // QuickShop 5+ uses the typed API; no legacy patch/build parsing.
        if (major >= 5) {
            return new QuickShopVersion(major, 0, 0);
        }

        if (parts.length < 3 || parts.length > 4) {
            throw new IllegalArgumentException("Unsupported legacy QuickShop version: " + version);
        }
        Integer.parseInt(parts[1]); // Validate the legacy minor component.
        int patch = Integer.parseInt(parts[2]);
        int build = parts.length == 4 ? Integer.parseInt(parts[3]) : 0;
        return new QuickShopVersion(major, patch, build);
    }

    boolean isLegacy() {
        return major < 5;
    }

    boolean useLegacyGetShop() {
        // Preserve the preexisting four-part threshold: 4.0.8.2 and later
        // use getShop; 4.0.8 and earlier use getShopWithCaching.
        return patch >= 8 && build >= 2;
    }
}

# SF_SlimeGlue

**SF_SlimeGlue** is the Slimefun Legacy-maintained fork of [Xzavier0722/SlimeGlue](https://github.com/Xzavier0722/SlimeGlue). It keeps SlimeGlue's original compatibility fixes while targeting modern Slimefun Legacy servers on Paper/Purpur 26.2 and Minecraft 1.21.11+.

This fork is maintained for the Slimefun Legacy ecosystem and is used on [AlbionMC.com](https://albionmc.com/).

## What SlimeGlue does

SlimeGlue bridges Slimefun automation and protection behavior with other plugins so Slimefun machines and Androids respect protections and special blocks created by those plugins.

Current upstream compatibility modules include:

- **KingdomsX** — prevents Slimefun Androids from breaking protected kingdom blocks, structures, and turrets.
- **Magic** — prevents Androids from breaking Magic fake blocks and avoids the related item-duplication behavior.
- **QuickShop / QuickShop-Hikari** — prevents Slimefun automation from breaking protected shop containers.
- **LockettePro** — prevents Androids from breaking LockettePro-protected blocks.

## Legacy target

- **Primary Slimefun:** [Slimefun Legacy](https://github.com/wickidcow/Slimefun-Legacy)
- **Minecraft:** 1.21.11+
- **Server:** Paper/Purpur 26.2+
- **Build JDK:** 25
- **Plugin bytecode:** Java 21
- **SlimefunCompLib:** `b7a2bd8`, kept aligned with Slimefun Legacy

The plugin keeps the normal plugin name `SlimeGlue` so Slimefun Legacy's existing `loadBefore: SlimeGlue` integration continues to work.

## Building

```bash
./gradlew clean build
```

The finished server JAR is written to:

```text
build/libs/SF_SlimeGlue_Legacy_v1.0.0.jar
```

GitHub Actions builds every pull request and push to `master`. The workflow uploads `SF_SlimeGlue_Legacy_v1.0.0.jar` directly with artifact archiving disabled, so the download is the raw `.jar`, not a ZIP wrapper. Version tags (`v*`) also publish that same raw JAR as a GitHub Release asset.

## Credits

SlimeGlue was created by **Xzavier0722**. This fork preserves the original source history, package structure, attribution, and MIT license while maintaining compatibility with Slimefun Legacy and current Paper environments.

Original project: [Xzavier0722/SlimeGlue](https://github.com/Xzavier0722/SlimeGlue)

Slimefun Legacy fork maintenance: **wickidcow**

## License

This project remains licensed under the **MIT License** from the original SlimeGlue project. See [`LICENSE`](LICENSE) for the complete license and original copyright notice.

## Disclaimer

This is an independent community project. It is not affiliated with or endorsed by Mojang Studios or Microsoft. Minecraft is a trademark of Microsoft Corporation.

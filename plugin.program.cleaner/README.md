# Simple Wizard (plugin.program.simplewizard)

Lightweight Kodi wizard template for installing builds, performing fresh-start, and basic maintenance tasks.

## Features
- Install builds listed in a remote `builds.xml` or `builds.json` file
- Fresh Start / maintenance utilities
- Backup & restore helpers
- Skin switch helper and advancedsettings presets

## Quick install
1. Zip the folder and install via Kodi (`Install from zip file`).
2. Edit `addon.xml` if you rename the addon folder (set `id` to the folder name).

## Customize your builds list
1. Edit `resources/texts/builds.example.xml` (or `builds.json`) to add your build entries.
2. Host the file on a web server or GitHub raw URL.
3. In `uservar.py` set the URL that points to your hosted builds file.

### Minimal XML schema (example)
See `resources/texts/builds.example.xml` for a commented example. Required fields per build:
- `name` — Build display name
- `version` — Build version
- `kodi` — target Kodi version tag
- `url` — HTTP(S) URL to the build zip or installer
- `icon` / `fanart` / `preview` — optional image URLs
- `description` — short blurb

## Advancedsettings presets
The `resources/advancedsettings/` folder contains presets (nexus, omega, piers). Host or include the desired XML when installing a build.

## Development notes
- Main plugin entry: `addon.py` (calls `resources.lib.modules.plugin.router`)
- Service entry: `service.py` (startup tasks)
- Core modules live in `resources/lib/modules/`.

## Contributing
PRs welcome — open issues for bugs or feature requests. For small users, editing the builds file and hosting it is the usual workflow.

## License
This project is licensed under GPL-2.0-or-later (see `LICENSE`).
# plugin.program.simplewizard
Simple Wizard for Kodi

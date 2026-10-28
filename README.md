# road-sdl2-rash: Road Rash (1996 PC) Native Port & Web Edition

[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Steam%20Deck%20%7C%20Web-blue.svg)](#editions--platforms)
[![License](https://img.shields.io/badge/License-GPL%20%2F%20MIT%20Platform-green.svg)](#licenses--legal)
[![GitHub Pages](https://img.shields.io/badge/Web%20Port-Live%20Ready-orange.svg)](#3-web-browser)

**road-sdl2-rash** is a modern, native 64-bit port and WebAssembly release of the classic 1996 PC title **Road Rash**, translated directly from original x86 machine code into portable C over an **SDL2** platform layer.

Runs natively at full speed on **Windows 10/11**, **Linux**, **Steam Deck**, and in **Modern Web Browsers** (WebAssembly + WebGL).

> [!NOTE]
> **Source Code Release:** The complete decompiled C source code (~97,000 lines of structured, typed, human-readable C with modding hooks and tools) is undergoing final code cleanup and will be open-sourced soon!

---

## Key Features

* **100% Native 64-bit Execution:** No DOSBox, emulators, or Wine needed. Compiles and executes directly on modern operating systems.
* **Modernized Platform Layer:** Replaces DirectDraw, DirectSound, WinMM MIDI, and the Windows 95 registry with SDL2 and TinySoundFont.
* **Deterministic & Frame-Accurate:** Verified against the original 1996 game across 14 deterministic race replay scenarios (verifying exact physics, sound, and palette behavior).
* **Full Gamepad Support:** Native analog steering, trigger throttle/brake, and attacks for Xbox, PlayStation, and Steam Deck controllers.
* **Built-in Options Menu (F10):** Toggle fullscreen, CRT filters, resolution, audio volumes, and controller bindings on the fly.
* **High-Fidelity Audio:** Replaces legacy MIDI with [TinySoundFont](https://github.com/schellingb/tinysoundfont), playing both authentic Sound Blaster AWE32 instrument banks and GeneralUser GS SoundFonts.
* **Play in Your Browser:** Drop your game data into the web page to play directly inside Chrome, Firefox, Safari, or Edge with local browser caching.

---

## Editions & Platforms

### 1. Standard (Vanilla 1996) Mode
* 100% bit-exact physics and mechanics identical to the 1996 Windows 95 CD release.
* Original 640×480 software rendering.
* Original rival AI pacing, grudge counters, and aggression tables.

### 2. Road Rash "Plus" (Enhanced Mode)
* **1280×960 High-Resolution Mode:** Native double-resolution software rasterizer (`hires.c`).
* **Rock-Solid 60 FPS Presentation:** Integrated frame scheduler eliminates background OS thread stutters (`frame_profile.c`).
* **Road Rash Plus Preset (`mods-plus.ini`):**
  * **Aerodynamic Tuning:** 30% reduction in air drag for higher, more thrilling top speed on straightaways.
  * **Dynamic Rival Feuds:** Increased rival aggression and lasting grudges for intense mid-race brawls.
  * **Sharper Starter Bike:** Improved brake responsiveness on the Corsair Swallow.
  * **Better Offroad Recovery:** Enhanced shoulder traction when forced off the asphalt.

---

## Platform Downloads

| Platform | Location | Executable / Target | Details |
| :--- | :--- | :--- | :--- |
| **Windows** | [`windows/`](windows/) | `RoadRashPort.exe` | Native 64-bit executable for Windows 10 & 11. |
| **Linux & Steam Deck** | [`linux/`](linux/) | `roadrash.sh` | Portable glibc 2.17+ 64-bit binary with embedded SDL2. |
| **Web Browser** | [`web/`](web/) | `index.html` | Client-side WebAssembly port with drag-and-drop file loader. |

---

## Getting Started ("Bring Your Own Game")

To respect copyright laws and preservation standards, **no proprietary game assets are hosted in this repository**. You provide the assets from your original 1996 PC copy of Road Rash (CD-ROM or ISO).

### Required Game Files

From your original game disc or installation, copy the following items:
```text
ROADRASH.EXE
AUDIO/
DATA/
IMAGES/
TEXT/
```

### Installation & Launch

#### 1. Windows (10 / 11)
1. Download or clone this repository, and open the [`windows/`](windows/) folder.
2. Copy the required game files (`ROADRASH.EXE`, `AUDIO`, `DATA`, `IMAGES`, `TEXT`) directly into [`windows/`](windows/) alongside `RoadRashPort.exe`.
3. Double-click `RoadRashPort.exe`.
   *(If Windows Defender SmartScreen appears, click "More info" → "Run anyway".)*

#### 2. Linux & Steam Deck
1. Open the [`linux/`](linux/) folder.
2. Copy the required game files into [`linux/`](linux/) alongside `roadrash.sh`.
3. Make the launcher executable and run:
   ```bash
   chmod +x roadrash.sh roadrash-port
   ./roadrash.sh
   ```
   * **Steam Deck Users:** Add `roadrash.sh` as a "Non-Steam Game" in Desktop Mode. Return to Gaming Mode — controller input works out of the box!

#### 3. Web Browser
1. If testing locally:
   ```bash
   python3 web/serve.py 8765
   ```
   Then open `http://localhost:8765/` in your browser.
2. If playing on a hosted web deployment (e.g. GitHub Pages):
   * Open the web page link.
   * **Drag & Drop** your `index.data` file onto the browser window (or click to browse).
   * The page will read the file, optionally cache it in your browser's **IndexedDB** for instant zero-download loading on future visits, and start the race immediately!
   * *(To generate `index.data` from your original files, run `python3 web/pack_game_files.py <folder-with-gamefiles>`)*.

---

## Controls

### Keyboard
| Key | Action |
| :--- | :--- |
| **Up Arrow** | Accelerate |
| **Down Arrow** | Brake |
| **Left / Right Arrow** | Steer Left / Right |
| **Space / Ctrl / Alt** | Attack (Punch, Kick, Club swing) |
| **Enter** | Confirm / Menu Select / Pause |
| **Esc** | Back / Cancel |
| **F10** | Open In-Game Options Menu |
| **F11 / Alt + Enter** | Toggle Fullscreen / Windowed |
| **F12** | Instant Quit |

### Gamepad (Xbox / Steam Deck / PlayStation)
| Control | Action |
| :--- | :--- |
| **Left Analog Stick / D-Pad** | Steering |
| **Right Trigger / Button A** | Accelerate |
| **Left Trigger / Button B** | Brake |
| **Button X / Left Shoulder** | Attack Left |
| **Button Y / Right Shoulder** | Attack Right |
| **Start** | Pause / Confirm |
| **Back / Select** | Back |

---

## Modding & Customization (`mods.ini`)

Both the desktop and web builds include an integrated real-time modding engine.

* **Default State:** A pre-configured `port/userdata/mods.ini` is provided with all options commented out with `#` so first-time players experience the authentic 1996 gameplay balance.
* **How to Customize:** Open `port/userdata/mods.ini` in any text editor, remove the `#` before the line you want, and save:

```ini
# --- Example Tweaks ---
# Make rival AI fight each other frequently
rival_feud_percent = 200

# Increase top speed by lowering air resistance
physics_air_drag_percent = 70

# Make starter bike brakes sharper
bike.swallow.brakes = -150
```

* **To Enable Road Rash Plus:** Copy or rename `port/userdata/mods-plus.ini.example` to `port/userdata/mods.ini`.
* See [MODS.md](MODS.md) for full documentation of every bike ID, traffic multiplier, and AI combat variable.

---

## Coming Soon: Readable C Decompiled Source

The complete source code that powers this native port will be released in an upcoming repository update:
* **~97,000 Lines of Structured C:** 59 modular subsystem files covering bike physics, rival AI algorithms, course generation, software projection rasterizer, and audio synthesis.
* **Readable & Modder-Friendly:** Structured loops (`for`, `while`), folded conditional expressions (`&&`, `||`), 1,748 named functions, and 194 named record types.
* **Custom Hooking System:** Write your own C hooks around any game function without modifying original disassembly.

---

## Licenses & Legal

* **Road Rash** is a registered trademark of Electronic Arts Inc.
* This project is a non-commercial reverse engineering and recompilation project created strictly for preservation, education, and platform interoperability.
* No proprietary art, sound, video, courses, or executable binaries belonging to Electronic Arts are hosted or distributed in this repository.
* Open-source components:
  * **SDL2:** zlib license ([licenses/SDL2-LICENSE.txt](windows/licenses/SDL2-LICENSE.txt))
  * **TinySoundFont:** MIT license ([licenses/TinySoundFont-LICENSE.txt](windows/licenses/TinySoundFont-LICENSE.txt))
  * **GeneralUser GS SoundFont:** S. Christian Collins license ([windows/port/assets/GeneralUser-GS-LICENSE.txt](windows/port/assets/GeneralUser-GS-LICENSE.txt))

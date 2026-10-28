# General MIDI instruments

GeneralUser GS v2.0.3 by S. Christian Collins supplies the instruments for the
original game's MIDI stream notes. It is a General MIDI fallback, not an
emulation of the shipped custom AWE32 .SBK banks or a recording of CD music.

Upstream: https://github.com/mrbumpy409/GeneralUser-GS
Author: https://www.schristiancollins.com/generaluser.php
Commit: 684543d5e5efaef08d02be50dcda8d552478fa60
The unmodified license is in GeneralUser-GS-LICENSE.txt.

GeneralUser-GS.sf2: 32,319,396 bytes
SHA-256: 9575028c7a1f589f5770fccc8cff2734566af40cd26ed836944e9a5152688cfe

The default bank is included for offline builds and runs. Set RR_SOUNDFONT to
another compatible SF2 file to change instruments, or RR_NO_MUSIC=1 to disable
MIDI while retaining effects. RR_NO_AUDIO=1 disables the shared audio device.

## Original AWE32 banks

`awe/*.sf2` are deterministic conversions of the six original files in
`AUDIO/MUSIC/*.SBK`. The build regenerates them with
`python3 tools/convert_sbk.py`. No download is required. Original sample PCM and
copyright metadata are retained; the original game assets' rights still apply.
These derived files are not covered by TinySoundFont's MIT license or the
GeneralUser GS license.

The converter handles this game's RAM-only SoundFont 1 banks, translating sample
headers, loop registers, sample pitch, envelope/filter/pan/level units and SF1
sustain/LFO defaults into SF2. It rejects ROM samples and nonzero SF1 modulators.
The format/unit reference is the TiMidity++ implementation by Takashi Iwai and
Masanao Izumo: [sample headers](https://github.com/starg2/timidity41/blob/master/timidity/sffile.c),
[unit conversions](https://github.com/starg2/timidity41/blob/master/timidity/sbkconv.c),
and [sample pitch/defaults](https://github.com/starg2/timidity41/blob/master/timidity/sndfont.c).
This limited Python converter does not embed that synthesizer's source code.

The native AWE manager implements the command subset observed at original
addresses `0x434500` / `0x434620`. Bank slot 1 loads RRDRUMS, slot 2 loads the
selected GRUNGE bank; the SBKGRNG MIDI tracks select them through CC0. Programs
absent from a custom bank fall back to General MIDI. `RR_GM_ONLY=1` retains the
previous GM-only track selection. Software synthesis reproduces the custom
samples and musical events, not exact EMU8000 hardware output; TinySoundFont's
unsupported modulators/effects remain a fidelity limit.

## Sampled music assets

The original sampled-music playlist contains 14 names. This checkout contains
`HB_TRIP.RRA` and `HB_PASS.RRA`, which are 22,050 Hz, 8-bit stereo PCM WAVs with
an `.RRA` suffix. The other 12 recordings are absent:
`MM_Dino`, `P_Pansy`, `P_Jessie`, `P_Bridge`, `SG_Rusty`, `SG_Outsh`, `SG_Kicks`,
`SG_Super`, `SD_Train`, `SD_Duel`, `T_Teeth`, `T_Auto`.

The original loader accepts these names under `AUDIO/MUSIC/` with `.RRA` or `.WAV`
(case-insensitive). Missing recordings follow the game's existing failure path;
no replacement songs are invented or downloaded. This executable uses MMIO and
DirectSound for sampled music. Its MCI imports are for `avivideo`, not an optical
CD audio device.

## Original intro videos

`Video/StudLogo.AVI`, `Video/PapyLogo.AVI` and `Video/Intro.AVI` are absent here.
The native AVI bridge now supports the game's MCI playback flow using FFmpeg
decoding and SDL presentation/audio. Supply original files in `Video/` or set
`RR_VIDEO_DIR` to their directory; put FFmpeg on PATH or set `RR_FFMPEG`.
Generated fixtures under `tmp/platform/video-*` validate the bridge only.
See [../TESTING.md](../TESTING.md) for the combined testing instructions.

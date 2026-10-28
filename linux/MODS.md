# Mods for Road Rash (the port)

Written 2026-09-30 for commit `fe79e2c` and later. How to start each build:
[HOW_TO_RUN.md](HOW_TO_RUN.md).

Mods change the game's own values while it runs. The original files
(`ROADRASH.EXE`, `DATA`, ...) are never changed. **With no mods set, the game
is exactly the original**: checked frame by frame. Mods work in the Windows,
Linux, ARM and browser builds (not in the developer build `port/game`).

## 1. Switch mods on

Three ways, strongest last:

1. **A file** (normal use): copy `port/mods.ini.example` to
   `port/userdata/mods.ini` and remove the `#` in front of the lines you want.
   Lines are `key = value`; `#` starts a comment; case does not matter.
   Delete the line (or the file) to go back to the original.
2. **For one run** (tests): the variable `RR_MODS`, entries separated by `;`,
   for example `RR_MODS="racer_count=6;rival_feud_percent=200"`. It wins over
   the file.
3. **Browser:** the same in the address, with `=` written `%3D` and `;`
   written `%3B`:
   `http://localhost:8765/?RR_MODS=racer_count%3D6%3Brival_feud_percent%3D200`

Changes take effect when the game starts (restart it after editing).

## 2. All settings

Percentages are of the original value (100 = original, range 0..1000).
Measured effects come from scripted Napa races at the first level
(`port/JOURNAL.md`, entries N1a to N1f).

### Rivals: how they ride

| Key | What it changes | Measured |
|---|---|---|
| `rival_pace_percent` | how hard rivals ride (their pace before catching up or easing off, and their top pace when chasing) | 50: the field much slower (you can win); 120: faster at every point. **Above 120 is not understood**: 150 is faster for a minute, then slower. Keep to 50..120 |
| `rival_chase_percent` | the lowest pace a rival keeps while chasing someone | 200: field median ahead of the original |

### Rivals: fights

Every rival holds a grudge against every other rider. Above a threshold (lower
at higher levels) it attacks whoever it rides next to. Hits raise the victim's
grudge against the hitter; grudges then cool down again.

| Key | What it changes | Measured (attacks started in one race) |
|---|---|---|
| `rival_feud_percent` | grudges between rivals | original 6 on rivals; 200: 36 |
| `rival_grudge_player_percent` | grudges against you | original 0 on you; 200: 4 |
| `rival_retaliation_percent` | how much a hit raises the grudge against the hitter (feuds that last) | changes the race only when rivals already fight (use with feud) |
| `rival_grudge_generic_percent` | lets rivals hold a grudge against the 6 riders in slots 9..14, whom nobody targets in the original (0 = original, 100 = like any rival) | 100: 16 attacks on them; with feud 200: 62 |

These never change you or the police.

### Bikes

`bike.<which>.<field> = number`. `<which>` is a number, a short name, or
`all`; a line for one bike beats a `bike.all` line. It changes the bike for
everyone who rides it: you and the rivals.

| # | short name | shop name | | # | short name | shop name |
|---|---|---|---|---|---|---|
| 1 | `sport450` | Banzai Sport 450 | | 9 | `zyx750n` | Kamikaze ZYX 750N |
| 2 | `swallow` | Corsair Swallow (you start on it) | | 10 | `assassino` | Stiletto Assassino N |
| 3 | `zyx250` | Kamikaze ZYX 250 | | 11 | `vampiro` | Diablo Vampiro |
| 4 | `rat` | Killer Rat | | 12 | `m10` | DMG M10 |
| 5 | `pico` | Perro Pico (the police ride it) | | 13 | `zyx750` | Kamikaze ZYX 750 |
| 6 | `supersport` | Banzai Super Sport | | 14 | `grande` | Perro Grande |
| 7 | `raven` | Corsair Raven N | | 15 | `aggressore` | Stiletto Aggressore |
| 8 | `vipera` | Diablo Vipera N | | | | |

Bikes 7 to 10 are the nitro bikes.

| Field | What it is | Original range |
|---|---|---|
| `power` | engine power: the throttle limit and how fast the throttle rises and falls | 35..48 |
| `brakes` | brake strength (more negative = stronger) | -40..-120 |
| `0xNNN` | any number in the bike's record by its offset (0x000..0x160), for experiments; `RR_MODS_TRACE=1` shows the originals | - |

Measured: `bike.all.power = 60` puts you 15% further along at the same moment
early in a race.

The shop's text and prices do not change.

### Physics (everyone, you included)

| Key | What it changes | Measured |
|---|---|---|
| `physics_air_drag_percent` | air drag, the main limit on top speed | flat out: 11,175 original, 16,913 at 50 (+51%) |
| `physics_offroad_drag_percent` | how much the ground beside the road slows you | 300: whole field slower, rival crashes 1 to 7 |
| `physics_grip_percent` | traction everywhere (lower = bikes slip sooner) | 60: your top speed lower |
| `physics_offroad_grip_percent` | traction off the road only | 50: field a little slower |

Rivals gain less from lower air drag: their AI decides their speed (use
`rival_pace_percent` for them). There is no speed-limit setting: the game's
30,000 limit only acts in crashes.

### The field and traffic

| Key | What it changes |
|---|---|
| `racer_count = 2..15` | number of bikers including you (original 15). Results, standings and the HUD follow. More than 15 is not possible yet (the game's tables hold 15 bikers and a police bike) |
| `traffic_speed_scalar = -128..127` | speed of the traffic cars (original 25). The older name `rival_speed_scalar` still works: it was always the traffic |

## 3. Ready-made recipes

Copy one block into `port/userdata/mods.ini`.

```ini
# Brawl: rivals fight each other all the time
rival_feud_percent = 200
rival_grudge_generic_percent = 100
rival_retaliation_percent = 200
```

```ini
# Easier: slower rivals who leave you alone
rival_pace_percent = 60
rival_grudge_player_percent = 50
```

```ini
# Harder: faster rivals who come for you
rival_pace_percent = 115
rival_grudge_player_percent = 200
```

```ini
# Fast bikes
physics_air_drag_percent = 70
```

```ini
# Small field, busy roads
racer_count = 6
traffic_speed_scalar = 40
```

```ini
# Slippery
physics_grip_percent = 70
physics_offroad_grip_percent = 50
```

## 4. Browser examples

```text
http://localhost:8765/?RR_MODS=racer_count%3D6
http://localhost:8765/?RR_MODS=rival_feud_percent%3D200%3Brival_grudge_generic_percent%3D100
```

## 5. Check that a mod is active

The game prints one `[mods]` line per active setting when it starts, and warns
about keys it does not know (a typo never passes silently):

```text
[mods] rival_feud_percent = 200
[mods] RR_MODS: unknown key rival_pase_percent ignored
```

Where to read them: Windows launchers write `port\userdata\last_run.log`; the
Linux program prints them in the terminal; the browser shows them in the
developer console (F12).

More detail:

- `RR_MODS_TRACE=1`: every bike loaded for every racer (type, bike, throttle
  and brake limits) and every changed bike value.
- `RR_MODS_TRACE=2`: also the race standings every 20 seconds, rival crashes
  and attacks (who attacked whom).

## 6. Known limits (open work)

- `rival_pace_percent` above 120: the result is not understood yet.
- Hits by riders in slots 9..14 do not raise grudges (the original's rule).
- No setting yet for gearing, rolling drag, or more than 15 racers.
- Mods are read at start only; F10 does not show them.
- Careers: the prize money and qualifying with fewer racers are not checked.
- Nothing here has been played on a screen yet, only measured in headless
  races.

## 7. For developers: how a mod is made

All mods are in `port/game/mods.c` (the comment at its top explains each key
and the game code behind it), reading `mods.ini` through
`port/game/mods_config.c`. They attach to the translated game in three ways
(`port/host/build_game.sh`):

- **hooks** (`recomp.py --after-hooks`, `--around-hooks`): run code after or
  around an original function, for example after the bikes are loaded
  (0x405e30) or when a racer is spawned (0x405ea0);
- **substitutions** (`--subst`): turn a constant in one original instruction
  into a variable (racer count, the grudge against riders 9..14);
- **data patches**: change the game's tables in memory once they are loaded.

The rule: the original value is the default, and a race with no mods must
stay identical to the original frame by frame (`port/TESTING.md`,
deterministic race).

## 8. The original's cheat codes (found while naming the lifted C)

The game has typed cheat codes; they need no mod. The code is in two tables, 0x463600 and
0x463680 (each character is stored as two bytes that add up to it, so they do not show as text in
the executable); `cheat_key_typed` and `cheat_code_match` in the lifted C read them. Decoded:

| Code | Effect (from the function it calls) |
|---|---|
| `xyzzy` | cheat mode on; arms `plugh`, which turns it off again |
| `yes,occifer` then Enter, `bribe` then Enter | removes the cop (the rider removal 0x4073a0) |
| `spoon!` | nitro (`nitro_setup` with fixed values) |
| `thwack!` | gives the player weapon 2 |
| `k'thunk!` | gives the player weapon 1 |
| `heinz`, `callgeorge.` | toggle the flags 0x4c8029 and 0x4753c8 |
| `ungh!`, `jaratae`, `riffraff` | toggle palette effects (0x47e9dc, 0x47e9e4, 0x47e9e0) |

The first table is ignored in multiplayer. What the flag toggles do in play has not been checked.

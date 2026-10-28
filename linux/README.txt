ROAD RASH (the port) - Linux 64-bit and Steam Deck

This folder is the program only. It needs the original game's files, which
are not in it.

1. ADD THE GAME FILES
  Copy these from the original game into this folder, next to roadrash.sh:

      ROADRASH.EXE
      AUDIO/
      DATA/
      IMAGES/
      TEXT/
      port/assets/awe/        (the music's own instruments: six .sf2 files
                              made from AUDIO/MUSIC/*.SBK)

  In the release they are ready in 3-game-files/for-windows-and-linux/: copy
  everything inside that folder into this one (merge the port folder). Upper
  or lower case does not matter. Without them the game says which files are
  missing and stops. Only port/assets/awe may be left out: the music then
  plays with general instruments.

2. START
  Any 64-bit Linux (x86-64):
      chmod +x roadrash.sh roadrash-port      (once, if the copy lost the flags)
      ./roadrash.sh
  Nothing to install: the program carries its own SDL2 and runs on
  distributions from 2012 on (glibc 2.17 or newer: Ubuntu 14.04, Debian 8,
  CentOS 7, SteamOS and everything later). It uses the X11 or Wayland
  desktop and PulseAudio (PipeWire's included) or ALSA sound, whichever the
  system has.

  Steam Deck:
   a. Switch to Desktop Mode. Copy this folder, with the game files in it, to
      the Deck, for example to /home/deck/Games/roadrash. If you have
      2-linux-steamdeck.tar.gz, unpack that on the Deck instead and add the
      game files: the archive keeps the "executable" flags.
   b. If the flags were lost: right-click roadrash.sh, Properties,
      Permissions, tick "Is executable". The same for roadrash-port.
   c. In Steam: Games, "Add a Non-Steam Game to My Library", Browse, set the
      file type to "All Files", pick roadrash.sh, "Add Selected Programs".
   d. Start it from the library, in Desktop Mode or Gaming Mode. The Deck's
      own controls work as the gamepad below.
   e. F10 (options) and F12 (quit) are keyboard keys: give them to two back
      buttons in the game's controller settings in Steam, or use the
      on-screen keyboard (Steam + X).

  Tested without a window: scripted races give the reference result on
  Ubuntu 22.04, and the program starts through roadrash.sh and finishes a
  race on Ubuntu 14.04. Not yet played with a window and sound on a Linux
  desktop, and not yet run on a Steam Deck.

KEYS
  Arrow keys            steer, speed up, brake; move in the menus
  Enter                 confirm, pause
  Esc                   back
  Letters, Ctrl, Shift, Space   the original game's other controls
  F10                   options (the game pauses while they are open)
  F11 or Alt+Enter      fullscreen or window
  F12                   quit at once

GAMEPAD (Xbox-style, connected before starting)
  Left stick or D-pad   steer
  Right trigger or A    speed up
  Left trigger or B     brake
  X or left shoulder    attack left
  Y or right shoulder   attack right
  Start                 confirm, pause
  Back                  back

OPTIONS (F10)
  Up/Down picks, Left/Right changes, Esc or F10 closes: fullscreen, picture
  filter, race resolution (1280x960 or 640x480), vsync, music and effects
  volume, controller and more.

WHAT THE GAME WRITES
  Everything goes to port/userdata/ in this folder: roadrash.ini (options),
  registry (the game's own stored options), saves/RoadRash.RRS (the career),
  last_run.log (messages of the last run). To move your progress to another
  copy, copy port/userdata.

MODS
  See MODS.md. Copy port/mods.ini.example to port/userdata/mods.ini and
  remove the # in front of the lines you want. With no mods the game is the
  original.

IF SOMETHING GOES WRONG
  Read port/userdata/last_run.log.
  No sound: check the system volume, then Music and Effects volume in F10.
  Small hitches while racing: set Race resolution to 640x480 in F10.
  The game's videos (logos, intro) play only if you have them (a Video/
  folder next to ROADRASH.EXE) and ffmpeg is installed; without them the
  game skips them.

LICENSES
  licenses/ has the licenses of the parts that are not the game: SDL2,
  TinySoundFont and the GeneralUser GS instruments (port/assets).

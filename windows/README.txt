ROAD RASH (the port) - Windows

This folder is the program only. It needs the original game's files, which
are not in it.

1. ADD THE GAME FILES
  Copy these from the original game into this folder, next to
  RoadRashPort.exe:

      ROADRASH.EXE
      AUDIO\
      DATA\
      IMAGES\
      TEXT\
      port\assets\awe\        (the music's own instruments: six .sf2 files
                              made from AUDIO\MUSIC\*.SBK)

  In the release they are ready in 3-game-files\for-windows-and-linux\:
  copy everything inside that folder into this one (when Windows asks about
  the port folder, merge it). Without them the game says which files are
  missing and stops. Only port\assets\awe may be left out: the music then
  plays with general instruments.

2. START
  Double-click RoadRashPort.exe. Keep SDL2.dll next to it.
  Windows 10 or 11, 64-bit. Windows 7 and 8.1 need Microsoft's
  Universal C Runtime update (KB2999226) and are untested.
  Tested: scripted races without a window give the reference result on
  Windows 11. Not yet played with a window.
  Windows may warn about a program it does not know: "More info", then
  "Run anyway".

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
  Everything goes to port\userdata\ in this folder: roadrash.ini (options),
  registry (the game's own stored options), saves\RoadRash.RRS (the career),
  last_run.log (messages of the last run). To move your progress to another
  copy, copy port\userdata.

MODS
  See MODS.md. Copy port\mods.ini.example to port\userdata\mods.ini and
  remove the # in front of the lines you want. With no mods the game is the
  original.

IF SOMETHING GOES WRONG
  Read port\userdata\last_run.log.
  No sound: check the Windows volume, then Music and Effects volume in F10.
  Small hitches while racing: set Race resolution to 640x480 in F10.
  The game's videos (logos, intro) do not play in the Windows build.

LICENSES
  licenses\ has the licenses of the parts that are not the game: SDL2,
  TinySoundFont, the GeneralUser GS instruments (port\assets) and the
  mingw-w64 runtime.

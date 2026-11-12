ROAD RASH (the port) - web browser

This folder is the program only (index.html, index.js, index.wasm). It needs
the original game's files as ONE file, index.data, which is not in it.

1. ADD THE GAME FILES
  Copy index.data into this folder, next to index.html. In the release it is
  ready in 3-game-files/for-web/. Without it the page says "index.data (the
  game files) is missing".

  To make index.data again from a Windows or Linux game folder that already
  has the game files in it:
      python3 pack_game_files.py <that folder>

2. START
  A browser does not run the game from a file on disk (file://): the folder
  must come from a web server.

  On your own computer, with Python 3:
      python3 serve.py          (Windows: py serve.py)
  then open http://localhost:8765/ in Chrome, Edge or Firefox.

  On the internet: upload the four files (index.html, index.js, index.wasm,
  index.data) to any static web host, in one folder. Nothing runs on the
  server. index.data is about 77 MB and the browser downloads it before the
  game starts.

  Click the picture once so the game gets the keyboard and may play sound.

  Tested: a scripted race in Chrome without a window. Not yet played in a
  visible browser, or in Edge or Firefox.

KEYS
  Arrow keys            steer, speed up, brake; move in the menus
  Enter                 confirm, pause
  Esc                   back; in a race: holds the race and asks, Esc again quits,
                        any other key goes on
  Pause                 pauses a race (any key goes on)
  Letters, Ctrl, Shift, Space   the original game's other controls
  F1 or Shift+F10       options (the game pauses while they are open)
  F10                   toggle HUD style (classic dashboard / minimal)
  F11 or Alt+Enter      fullscreen or window
  F12                   quit at once

GAMEPAD (Xbox-style, connected before starting)
  Left stick or D-pad   steer (in race), navigate (in menus)
  Right trigger or A    speed up (in race), confirm (in menus)
  A                     also nitro, on the nitro bikes (the N key)
  Left trigger          brake (in race)
  B or right shoulder   attack right (kick / club) in race, back / cancel (in menus)
  X, Y or left shoulder attack left (punch / club)
  Start                 pause (in race), confirm (in menus)
  Back                  next music track (in race), back / cancel (in menus)

OPTIONS (F1 / Shift+F10)
  Up/Down picks, Left/Right changes, Esc or F1 closes: fullscreen, picture
  filter, race resolution (1280x960 or 640x480), wide race view (Plus mode only:
  16:9, more road on each side, the dashboard in the middle), draw distance (Plus mode
  only: far or farthest shows the road and scenery 48 or 64 strips ahead in place of
  32, fading into the distance, from the next race on), vsync, music and effects
  volume, controller, in-race music (the soundtrack plays on through the races in
  place of their MIDI music; off by default) and more.

  In the browser F11 is the browser's own fullscreen.

WHAT IS DIFFERENT IN THE BROWSER
  Nothing is saved: options and the career start fresh on every page load.
  Settings can be given in the address, for example
      http://localhost:8765/?RR_MODS=racer_count%3D6
  (MODS.md of the Windows and Linux folders lists the mods).
  The game's videos (logos, intro) do not play.

LICENSES
  licenses/ has the licenses of the parts that are not the game: SDL2,
  TinySoundFont, the GeneralUser GS instruments and Emscripten.

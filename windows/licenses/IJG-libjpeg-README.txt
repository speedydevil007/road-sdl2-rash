This software is based in part on the work of the Independent JPEG Group.

Road Rash decodes its JPEG pictures with the Independent JPEG Group's libjpeg
(release 6, Copyright (C) 1991-1995, Thomas G. Lane), which its makers built
into ROADRASH.EXE. The translated game code (src/game/roadrash/jpeg_*.c)
includes that library, translated to C from the machine code along with the
rest of the game; its functions carry libjpeg's own names.

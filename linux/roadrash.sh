#!/bin/sh
# Road Rash (the port): starts the game from this folder.
# Messages of the run go to port/userdata/last_run.log.
cd "$(dirname "$(readlink -f "$0")")" || exit 1
say() {   # a dialog where there is one (the Steam Deck's game mode has no terminal), and the terminal
    echo "$1" >&2
    if command -v kdialog >/dev/null 2>&1; then kdialog --title "Road Rash" --error "$1" 2>/dev/null
    elif command -v zenity >/dev/null 2>&1; then zenity --error --title="Road Rash" --text="$1" 2>/dev/null; fi
}
for need in roadrash.exe audio data images text; do
    if ! ls | grep -qix "$need"; then
        say "The original game's files are missing or incomplete. Copy ROADRASH.EXE, AUDIO, DATA, IMAGES, TEXT and port/assets/awe into this folder (see README.txt)."
        exit 1
    fi
done
chmod +x ./roadrash-port 2>/dev/null
missing=$(ldd ./roadrash-port 2>&1 | grep 'not found' | head -3 | tr -s ' \t\n' ' ')
if [ -n "$missing" ]; then   # the program needs only glibc 2.17 (SDL2 is built in)
    say "This system lacks what the program needs (64-bit Linux with glibc 2.17 or newer, from 2012 on): $missing"
    exit 1
fi
mkdir -p port/userdata
./roadrash-port "$@" > port/userdata/last_run.log 2>&1
rc=$?
[ $rc -ne 0 ] && say "The game stopped with error code $rc. See port/userdata/last_run.log in the game folder."
exit $rc

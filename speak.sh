#!/bin/bash
# Usage: ~/Desktop/Egyptian-TTS/speak.sh "النص بالعامية المصرية" output.wav [reference.wav]
DIR="$(cd "$(dirname "$0")" && pwd)"
exec "$DIR/venv/bin/python" "$DIR/tts.py" "$@"

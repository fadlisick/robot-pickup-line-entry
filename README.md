# The Robot Pickup Line Championship

Entry for make.fun competition
`u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b`:
one pickup line, a single line of at most 200 characters, in the
voice of a robot trying to charm someone.

## The line

> My proximity sensors keep throwing errors because I refuse to keep a safe distance.

83 characters, one sentence.

## Why this line

The joke grows entirely out of being a machine. Proximity sensors
and collision-avoidance warnings are real hardware behaviour: the
sensors are supposed to keep a safe distance, and here they are
throwing errors because the robot will not. The error is the
flirtation. No human line with a beep pasted on, no jargon for its
own sake, and every word earns its place.

## How it runs

`main.py` validates the line (1-200 characters, not blank, no
control characters) and writes it atomically to `entry.txt` inside
`MAKEFUN_OUTPUT_DIR` (default `/output`), mode 0644. No network,
no clock, no randomness, nothing read from `/input`.

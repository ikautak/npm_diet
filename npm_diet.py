#!/usr/bin/env python3

import sys
import random
import subprocess

menu = [
    'push-ups',
    'sit-ups',
    'back extensions',
    'squats'
]

if __name__ == '__main__':
    random.shuffle(menu)
    t = random.randint(3, 5)
    print(menu[0], t, 'times')

    while True:
        print('finished ? [y/n]')
        s = input().lower()
        if s == 'y':
            break
        elif s == 'n':
            # TODO Notify slack that you have skipped out.
            break

    cmd = ['npm']
    if len(sys.argv) > 1:
        cmd += sys.argv[1:]
    subprocess.run(cmd, stderr=sys.stderr, stdout=sys.stdout)

#!/usr/bin/env python3
import argparse

TAILS_DEFAULT = ["!", "!@", "!@#"]

def gen_words(seeds, maxlen=9, tails=TAILS_DEFAULT):
    for seed in seeds:
        variants = {seed.lower(), seed.capitalize()}
        for base in variants:
            for tail in tails:
                room = maxlen - len(base) - len(tail)
                if room <= 0:
                    continue
                # 숫자 길이 1..room
                for d in range(1, room + 1):
                    lo = 0 if d == 1 else 10**(d-1)
                    hi = 10**d
                    for n in range(lo, hi):
                        yield f"{base}{n}{tail}"

def main():
    ap = argparse.ArgumentParser(description="Generate password list: word + digits + tail (!|!@|!@#), max length 9")
    ap.add_argument("-w", "--words", required=True, help="Comma-separated words (e.g., adm,vdi)")
    ap.add_argument("-o", "--output", help="Output file (default: stdout)")
    ap.add_argument("--maxlen", type=int, default=9, help="Max total length (default: 9)")
    ap.add_argument("--tails", default="!,!@,!@#", help="Comma-separated tails (default: !,!@,!@#)")
    args = ap.parse_args()

    seeds = [w.strip() for w in args.words.split(",") if w.strip()]
    tails = [t.strip() for t in args.tails.split(",") if t.strip()]

    gen = gen_words(seeds, maxlen=args.maxlen, tails=tails)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            for pwd in gen:
                f.write(pwd + "\n")
    else:
        for pwd in gen:
            print(pwd)

if __name__ == "__main__":
    main()

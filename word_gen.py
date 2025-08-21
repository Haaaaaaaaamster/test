#!/usr/bin/env python3
import argparse

TAILS_DEFAULT = ["!", "!@", "!@#"]

def gen_words(seeds, tails, maxlen=9, equalize=False):
    for seed in seeds:
        for base in {seed.lower(), seed.capitalize()}:
            # 꼬리별 최대 숫자 범위 계산
            ranges = []
            for tail in tails:
                room = maxlen - len(base) - len(tail)
                if room <= 0:
                    ranges.append((tail, -1))  # 불가
                    continue
                # room 자릿수까지만 허용, 단 전체 정책상 최대 9999
                max_n = min(9999, (10 ** room) - 1)
                ranges.append((tail, max_n))

            # 균등화: 가장 작은 max_n에 맞춤
            if equalize:
                valid_max = [mx for _, mx in ranges if mx >= 0]
                if not valid_max:
                    continue
                cap = min(valid_max)
            else:
                cap = None

            for tail, max_n in ranges:
                if max_n < 0:
                    continue
                upper = cap if cap is not None else max_n
                for n in range(0, upper + 1):
                    yield f"{base}{n}{tail}"

def main():
    ap = argparse.ArgumentParser(description="word + digits(0-9999) + tail(!|!@|!@#), total length ≤ 9")
    ap.add_argument("-w","--words", required=True, help="Comma-separated words, e.g., adm,vdi")
    ap.add_argument("-o","--output", help="Output file (default: stdout)")
    ap.add_argument("--maxlen", type=int, default=9, help="Max total length (default: 9)")
    ap.add_argument("--tails", default="!,!@,!@#", help="Comma-separated tails (default: !,!@,!@#)")
    ap.add_argument("--equalize", action="store_true",
                    help="Equalize per-tail counts to the smallest feasible range (e.g., match !@#).")
    args = ap.parse_args()

    seeds = [w.strip() for w in args.words.split(",") if w.strip()]
    tails = [t.strip() for t in args.tails.split(",") if t.strip()]

    gen = gen_words(seeds, tails, maxlen=args.maxlen, equalize=args.equalize)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            for pwd in gen:
                f.write(pwd + "\n")
    else:
        for pwd in gen:
            print(pwd)

if __name__ == "__main__":
    main()

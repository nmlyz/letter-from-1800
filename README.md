# letter-from-1800

[![make.fun · u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/nmlyz/letter-from-1800/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/nmlyz/letter-from-1800/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
<sub>See the entry on [make.fun](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)</sub>

A small, deterministic program that writes one sentence to a text file. The sentence explains the modern internet to a traveler arriving from the year 1800, using only things a person of that year would already know: a road, a letter, sealing wax, and books.

## Usage

```bash
python3 main.py
```

By default the program writes to `/output/entry.txt`. Set the `MAKEFUN_OUTPUT_DIR` environment variable to write to a different directory.

## Output

The output file `entry.txt` contains exactly one sentence of 168 characters:

> It is a road joining every house on earth, where a letter reaches any door before its wax cools, and the books of a thousand libraries answer when you call their names.

The program writes the same bytes on every run.

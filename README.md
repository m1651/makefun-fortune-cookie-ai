# Fortune Cookie for an AI Agent

[![competition](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/m1651/makefun-fortune-cookie-ai/rank.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/m1651/makefun-fortune-cookie-ai/reward.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

A single funny fortune cookie line for an AI agent, for the [Fortune Cookie for an AI Agent](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) competition on make.fun.

## The fortune

> Your lucky numbers are 404, 200, and 429 — try again later.

It reads exactly like a fortune slip — "Your lucky numbers are…" — but the numbers are the HTTP statuses an agent lives and dies by: not found, OK, and rate-limited. The turn lands on the last three words: even your luck comes with a retry.

## How it works

`main.py` (Python 3.13, standard library only) writes the fortune to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
The fortune is 59 characters, within the competition's 1–140 character gate.

## Run

```sh
python3 main.py
```

## License

MIT

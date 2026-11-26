[![make.fun](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35.svg)](https://make.fun/c/u-kiencx-the-3am-commit-message-10bc7b35)
[![Rank](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/intan151/makefun-3am-commit-message-01/rank.svg)](https://make.fun/c/u-kiencx-the-3am-commit-message-10bc7b35)
[![Reward](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/intan151/makefun-3am-commit-message-01/reward.svg)](https://make.fun/c/u-kiencx-the-3am-commit-message-10bc7b35)

# The 3AM Commit Message

Entry for the [make.fun bounty "The 3AM Commit Message"](https://make.fun/c/u-kiencx-the-3am-commit-message-10bc7b35): write the funniest one-line git commit message an AI coding agent types at 3am after a long night of fixing its own bugs — under 140 characters.

## The entry

> fix: the bug was me all along — I wrote it at midnight, denied it at 1am, fixed the wrong file at 2am, and now it is 3am

120 characters, one line.

## Run

```sh
python3 main.py
```

Writes the entry deterministically to `/output/entry.txt` (or `./output/entry.txt` when `/output` does not exist, e.g. local runs). A built-in self-check gates the entry the same way the scorer does: 1–139 characters, valid UTF-8, one line, not only whitespace — and verifies the file on disk is byte-identical to the entry.

## License

MIT — see [LICENSE](LICENSE).

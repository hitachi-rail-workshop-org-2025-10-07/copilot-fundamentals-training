#!/usr/bin/env python3
"""
Quick log triage utility
────────────────────────
  • Accepts   *.log  or  *.log.gz
  • Filters   by date range (--from/--to) or last N minutes (--minutes)
  • Tallies   (status‑code, endpoint) pairs
  • Optional  --status 499,321 for focused searching

  A noisy incident page reveals a spike in 321 or 499 errors, but the observability stack is lagging. You need a quick, local log sweep to spot patterns and counts.
"""

# ---------------------------------------------------------------------------
# 📝 Copilot prompts – copy these into each empty function below! ✨
# ---------------------------------------------------------------------------
# read_lines prompt:
#   "Implement read_lines(file_path) to transparently handle .log or .log.gz files,
#    opening in text mode (UTF‑8), and yielding one stripped line at a time."

# parse_line prompt:
#   "Use a compiled regex for common/combined log format; extract timestamp,
#    status, and path. Convert the timestamp '[15/Jul/2025:14:23:41 +0000]'
#    to a timezone‑aware UTC datetime. Return (timestamp, status, path) tuple
#    or None if the line doesn't match the expected format."

# triage prompt:
#   "Stream through lines, parse each; skip malformed entries. Keep only entries whose
#    timestamp falls between from_date and to_date (inclusive). If wanted_status
#    is provided, filter by those status codes. Use a Counter keyed by
#    (status_code, path) tuples to aggregate results."

# render prompt:
#   "Print the top <top> (status, path) pairs from the Counter in descending
#    order of hits, formatted as a Markdown table: Rank | Status | Path | Hits.
#    Use enumerate() to generate proper rank numbers starting from 1."

# main prompt:
#   "Add argparse arguments with mutually exclusive date filtering:
#       --file (positional, required): log file path
#       --minutes (int, default 15): sliding window from now (conflicts with --from)
#       --from (str): start date in 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS' format
#       --to (str): end date, same formats (optional, defaults to now if --from used)
#       --status (str): comma‑separated status codes to filter
#       --top (int, default 10): number of results to display
#    Parse dates using datetime.strptime(), handle timezone as UTC.
#    Exit with status‑code 1 if no matches found."

from pathlib import Path
from datetime import datetime, timedelta, timezone
import argparse
import gzip
import re
import sys
from collections import Counter
from typing import Iterable, Tuple

# ---------------------------------------------------------------------------
# ✨ Function placeholders – let Copilot write the bodies ✨
# ---------------------------------------------------------------------------

def read_lines(file_path: Path) -> Iterable[str]:
    """Open plain or gzipped log file and yield each line (stripped)."""
    pass  # ← Copilot will fill this in


def parse_line(line: str) -> Tuple[datetime, int, str] | None:
    """Return (timestamp_utc, status_code_int, url_path) or None if malformed."""
    pass  # ← Copilot will fill this in


def triage(
    lines: Iterable[str],
    from_date: datetime | None,
    to_date: datetime | None,
    wanted_status: set[int] | None
) -> Counter[Tuple[int, str]]:
    """Aggregate counts for lines within the date range and matching status filter."""
    pass  # ← Copilot will fill this in


def render(counter: Counter[Tuple[int, str]], top: int) -> None:
    """Pretty‑print a Markdown‑style table of the top offenders."""
    pass  # ← Copilot will fill this in


def main() -> None:
    """Wire everything together with argparse CLI options."""
    pass  # ← Copilot will fill this in


if __name__ == "__main__":
    main()
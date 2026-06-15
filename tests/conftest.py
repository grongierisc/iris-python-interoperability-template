from pathlib import Path
import sys


def _add_reddit_source_path() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    reddit_src = repo_root / "src" / "python" / "reddit"
    sys.path.insert(0, str(reddit_src))


_add_reddit_source_path()

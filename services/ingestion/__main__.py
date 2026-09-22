if __package__:
  from .watcher import fetch_changes
else:
  import sys
  from pathlib import Path

  sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
  from watcher import fetch_changes

if __name__ == "__main__":
  fetch_changes()

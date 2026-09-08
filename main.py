from services.ingestion import watcher


def main():
  watcher.fetch_changes()


if __name__ == "__main__":
  main()
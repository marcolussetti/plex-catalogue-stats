# plex-stats

Produce simple statistics about a Plex Server Instance's catalogue(s).

Currently, this project shows the most common actors, directors, writers, etc featured in the given library.

# Usage

The easiest way to run plex-stats is to download one of the pre-built binaries for your platform from the [releases section](/marcolussetti/plex-stats/releases/latest/).

You will need to find a Plex Token to be able to log on. You can do so with the [official instructions](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/).

Next, you can run the binary in a command line environment (PowerShell or Command Prompt on Windows, Bash/Terminal on Linux or Mac).

```bash
./plex-stats --help
./plex-stats --help top-actors
```

```powershell
.\plex-stats --help
.\plex-stats --help top-actors
```

For instance, to get the most common actors, you could run:

```bash
./plex-stats --plex-token "<your plex token>" top-actors 10
```

Optionally, you may specify a list of libraries to restrict the search to, in a comma separated list, such as `"Movies,Films,Television"`.
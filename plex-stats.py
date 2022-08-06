import typer
from typing import Sequence
from collections import Counter
from plexapi.server import PlexServer

app = typer.Typer()


def count_individuals(libraries, individual_types):
    counter = Counter()
    for library in libraries:
        for library_item in library.all():
            try:
                for individual in getattr(library_item.reload(), individual_types):
                    counter[individual.tag] += 1
            except:
                pass
    return counter


@app.command()
def top_actors(
    plex_token: str = typer.Option(...),
    plex_url: str = "http://localhost:32400",
    libraries: str = "",
    n: int = 25,
):
    libraries = libraries.split(",") if len(libraries) else []
    top_n("actors", plex_token, plex_url, libraries, n)


@app.command()
def top_directors(
    plex_token: str = typer.Option(...),
    plex_url: str = "http://localhost:32400",
    libraries: str = "",
    n: int = 25,
):
    libraries = libraries.split(",") if len(libraries) else []
    top_n("directors", plex_token, plex_url, libraries, n)


@app.command()
def top_producers(
    plex_token: str = typer.Option(...),
    plex_url: str = "http://localhost:32400",
    libraries: str = "",
    n: int = 25,
):
    libraries = libraries.split(",") if len(libraries) else []
    top_n("producers", plex_token, plex_url, libraries, n)


@app.command()
def top_writers(
    plex_token: str = typer.Option(...),
    plex_url: str = "http://localhost:32400",
    libraries: str = "",
    n: int = 25,
):
    libraries = libraries.split(",") if len(libraries) else []
    top_n("writers", plex_token, plex_url, libraries, n)


def top_n(types: str, plex_token: str, plex_url: str, libraries: Sequence[str], n: int):
    plex = PlexServer(plex_url, plex_token)

    if len(libraries) > 0:
        print(libraries)
        plex_libraries = [plex.library.section(library) for library in libraries]
    else:
        plex_libraries = plex.library.sections()

    counter = count_individuals(plex_libraries, types)
    print(format_counter(counter, n))


def format_counter(counter, n=10):
    output = ""
    frozen_i = i = 1
    last = -1
    for k, v in counter.most_common(n):
        if v != last:
            frozen_i = i
        output += f"{frozen_i}. {k} ({v})\n"
        last = v
        i += 1

    return output


if __name__ == "__main__":
    app()

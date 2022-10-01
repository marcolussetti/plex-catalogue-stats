#!/usr/bin/env python3
# Get extended stats about most common things in your Plex catalogue
import typer
from typing import Sequence
from collections import Counter
from plexapi.server import PlexServer

app = typer.Typer()
conf = {
    "plex_token": None,
}


@app.callback()
def main(
    plex_token: str = typer.Option(
        ...,
        prompt="You need to provide your plex token -- see https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/ ",
        help="Plex X-Plex-Token, see https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/",
    ),
    plex_url: str = typer.Option(
        "http://localhost:32400", help="Path to your Plex Server"
    ),
    libraries: str = typer.Option(
        "", help="Optional list of comma separated Plex Library names"
    ),
):
    conf["plex_token"] = plex_token
    conf["plex_url"] = plex_url
    conf["libraries"] = libraries.split(",") if len(libraries) else []


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


@app.command()
def top_actors(
    n: int = typer.Option(25, help="Number of individuals to report"),
):
    """
    List the top n actors by appearences in the given libraries.
    """
    top_n("actors", conf["plex_token"], conf["plex_url"], conf["libraries"], n)


@app.command()
def top_directors(
    n: int = typer.Option(25, help="Number of individuals to report"),
):
    """
    List the top n directors by appearences in the given libraries.
    """
    top_n("directors", conf["plex_token"], conf["plex_url"], conf["libraries"], n)


@app.command()
def top_producers(
    n: int = typer.Option(25, help="Number of individuals to report"),
):
    """
    List the top n producers by appearences in the given libraries.
    """
    top_n("producers", conf["plex_token"], conf["plex_url"], conf["libraries"], n)


@app.command()
def top_writers(
    n: int = typer.Option(25, help="Number of individuals to report"),
):
    """
    List the top n writers by appearences in the given libraries.
    """
    top_n("writers", conf["plex_token"], conf["plex_url"], conf["libraries"], n)


if __name__ == "__main__":
    app()

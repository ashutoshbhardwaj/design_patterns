from abc import ABC, abstractmethod
from multipledispatch import dispatch


class IVisitor(ABC):
    """Visitor interface"""

    @abstractmethod
    def visit(self):
        """"""


class Artwork:
    def __init__(self, title: str, artist: str) -> None:
        self.title = title
        self.artist = artist

    def display(self):
        print(self)

    def __str__(self) -> str:
        return f"Artwork {self.title} by {self.artist}"

    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class Sculpture(Artwork):
    def __init__(self, title: str, artist: str) -> None:
        super().__init__(title, artist)

    def clean(self):
        print(f"Cleaning {self.title} by {self.artist}")


class Painting(Artwork):
    def __init__(self, title: str, artist: str) -> None:
        super().__init__(title, artist)

    def protect(self):
        print(f"Protecting {self.title} by {self.artist}")


class Installation(Artwork):
    def __init__(self, title: str, artist: str) -> None:
        super().__init__(title, artist)

    def maintain(self):
        print(f"Maintaining {self.title} by {self.artist}")


class Museaum:
    def __init__(self) -> None:
        self._artworks = set()

    def add_artwork(self, artwork: Artwork):
        self._artworks.add(artwork)

    def get_artworks(self) -> set:
        return self._artworks

    def accept(self, visitor: IVisitor):
        for art in self.get_artworks():
            art.accept(visitor)
        


class ArtVisitor(IVisitor):
    """Concrete visitor"""

    @dispatch(Painting)
    def visit(self, artwork):
        print(f"Protecting {artwork.title} by {artwork.artist}")

    @dispatch(Sculpture)
    def visit(self, artwork):
        print(f"Cleaning {artwork.title} by {artwork.artist}")

    @dispatch(Installation)
    def visit(self, artwork):
        print(f"Maintaining {artwork.title} by {artwork.artist}")


def run_museaum() -> None:
    painting = Painting("Sanyog", "Surbhi")
    sculpture = Sculpture("Van De Williams", "John Sina")
    installation = Installation("Light", "Benz")
    museaum = Museaum()
    museaum.add_artwork(painting)
    museaum.add_artwork(sculpture)
    museaum.add_artwork(installation)
    visitor = ArtVisitor()

    artworks = museaum.get_artworks()

    #for art in artworks:
        # if isinstance(art,Painting):
        #     art.protect()
        # if isinstance(art,Sculpture):
        #     art.clean()
        # if isinstance(art,Installation):
        #     art.maintain()
        # 2nd way - By having an interface Visitor
        #visitor.visit(art)
    # 3rd way -
    museaum.accept(visitor)


if __name__ == "__main__":
    run_museaum()

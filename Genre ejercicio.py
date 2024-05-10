# Importar la clase Enum del módulo enum
from enum import Enum

# Definir la clase Genre que hereda de Enum
class Genre(Enum):
    ROCK = "ROCK"
    POP = "POP"
    EDM = "EDM"
    COUNTRY = "COUNTRY"
# Definir la clase Song
class Song:
    # Constructor de la clase
    def __init__(self, name, artist, duration, release_date, genres=None):
        if not isinstance(name, str):
            raise TypeError("El nombre de la canción debe ser una cadena de caracteres.")
        if not isinstance(artist, str):
            raise TypeError("El nombre del artista debe ser una cadena de caracteres.")
        if not isinstance(duration, int) or duration <= 10:
            raise ValueError("La duración debe ser un entero positivo mayor que 10 segundos.")
        if not isinstance(release_date, str):
            raise TypeError("La fecha de lanzamiento debe ser una cadena de caracteres.")
        # Aquí podrías agregar más validaciones para la fecha de lanzamiento si es necesario
        self.name = name
        self.artist = artist
        self.duration = duration
        self.release_date = release_date
        self.genres = set(genres) if genres else set()
# Métodos getter para obtener los atributos de la canción
    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_duration(self):
        return self.duration

    def get_release_date(self):
        return self.release_date

    def get_genres(self):
        return self.genres
# Método para añadir un género a la canción
    def add_genre(self, genre):
        if genre not in Genre.__members__.values():
            raise ValueError("Género no válido.")
        if genre not in self.genres:
            self.genres.add(genre)
# Método de comparación para determinar si dos canciones son iguales
    def __eq__(self, other):
        return self.name == other.name and self.artist == other.artist and self.release_date == other.release_date
 # Método para representar la canción como una cadena de caracteres
    def __str__(self):
        return f"{self.artist} tocando {self.name} durante {self.duration} segundos."


# Source packages.

def main():
    """Function main of the module.

    The function main of this module is used to test the Class GENRE.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Check Class GENRE - Name.")
    print("=================================================================.")

    if isinstance(Genre.ROCK, Genre):
        print("Test PASS. The enum for ROCK has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(Genre.POP, Genre):
        print("Test PASS. The enum for POP has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(Genre.EDM, Genre):
        print("Test PASS. The enum for EDM has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(Genre.COUNTRY, Genre):
        print("Test PASS. The enum for COUNTRY has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    


# Checking whether this module is executed just itself alone.


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF

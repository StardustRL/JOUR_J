class Gateau:

    def __init__(self, nom : str) -> None:
        self.name=nom

    
    def __str__(self) -> str:
        return self.name
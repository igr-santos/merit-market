class BuyError(Exception):
    """
    Excecao para quando houver tentativa de compra
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

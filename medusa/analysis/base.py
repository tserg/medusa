class BaseAnalyser:
    """
    Base analyser class to be inherited by specific passes.
    """

    _id: str

    def __str__(self):
        return self._id

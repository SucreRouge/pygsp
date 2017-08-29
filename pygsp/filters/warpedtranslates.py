# -*- coding: utf-8 -*-

from . import Filter  # prevent circular import in Python < 3.5


class WarpedTranslates(Filter):
    r"""
    Vertex frequency filterbank

    Parameters
    ----------
    G : graph
    Nf : int
        Number of filters

    References
    ----------
    See :cite:`shuman2013spectrum`

    Examples
    --------
    >>> G = graphs.Logo()
    >>> F = filters.WarpedTranslates(G)
    Traceback (most recent call last):
      ...
    NotImplementedError

    """

    def __init__(self, G, Nf=6, **kwargs):
        raise NotImplementedError

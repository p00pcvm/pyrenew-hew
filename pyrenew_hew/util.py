"""
Pyrenew-HEW utilities
"""

from itertools import chain, combinations
from typing import Iterable


def powerset(iterable: Iterable) -> Iterable:
    """
    Subsequences of the iterable from shortest to longest,
    considering only unique elements.

    Adapted from https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    s = set(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def hew_models(with_null: bool = True) -> Iterable:
    """
    Return an iterable of the Pyrenew-HEW models
    as their lowercase letters.

    Parameters
    ----------
    with_null
       Include the null model ("pyrenew_null"), represented as
       the empty tuple `()`? Default ``True``.

    Returns
    -------
    Iterable
       An iterable yielding tuples of model letters.
    """
    result = powerset(("h", "e", "w"))
    if not with_null:
        result = filter(None, result)
    return result


def hew_letters_from_flags(
    fit_ed_visits: bool = False,
    fit_hospital_admissions: bool = False,
    fit_wastewater: bool = False,
) -> str:
    """
        Get the {h, e, w} letters defining
        a model from a set of flags indicating which
        of the datastreams, if any, were used in fitting.
        If none of them were, return the string "null"

        Parameters
        ----------
        fit_ed_visits
            ED visit data used in fitting?

        fit_hospital_admissions
            Hospital admissions data used in fitting?

        fit_wastewater
            Wastewater data used in fitting?

        Returns
        -------
        str
            The relevant HEW letters, or 'null',
    a"""
    result = (
        f"{'h' if fit_hospital_admissions else ''}"
        f"{'e' if fit_ed_visits else ''}"
        f"{'w' if fit_wastewater else ''}"
    )
    if not result:
        result = "null"
    return result


def pyrenew_model_name_from_flags(
    fit_ed_visits: bool = False,
    fit_hospital_admissions: bool = False,
    fit_wastewater: bool = False,
) -> str:
    """
    Get a "pyrenew_{h,e,w}" model name
    string from a set of flags indicating which
    of the datastreams, if any, were used in fitting.
    If none of them were, call the model "pyrenew_null"

    Parameters
    ----------
    fit_ed_visits
        ED visit data used in fitting?

    fit_hospital_admissions
        Hospital admissions data used in fitting?

    fit_wastewater
        Wastewater data used in fitting?

    Returns
    -------
    str
        The model name.
    """
    hew_letters = hew_letters_from_flags(
        fit_ed_visits=fit_ed_visits,
        fit_hospital_admissions=fit_hospital_admissions,
        fit_wastewater=fit_wastewater,
    )
    return f"pyrenew_{hew_letters}"

#!/usr/bin/env python3
""" doc doc """
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 seperator: str) -> str:
    """ create a hash message using regex """
    for field in fields:
        pattern = f"{field}=[^{seperator}]*"
        mess = re.sub(pattern, rf"{field}={redaction}", message)
    return mess

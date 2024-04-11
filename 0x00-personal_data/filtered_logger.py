#!/usr/bin/env python3
""" doc doc """
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 seperator: str) -> str:
    """ create a hash message using regex """
    pattern = r"(?:{seperator})({'|'.join(fields)})(?={seperator)"
    return re.sub(pattern, rf"\1={redaction}", message)

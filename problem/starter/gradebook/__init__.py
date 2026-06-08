# gradebook package
#
# TODO: Re-export the public API so callers can write:
#   from gradebook import RECORDS, format_report
#
# Hint:
#   from .data import RECORDS
#   from .reports import format_report
from .data import RECORDS
from .reports import format_report
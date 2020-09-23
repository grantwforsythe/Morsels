from contextlib import contextmanager, ContextDecorator
# contextlib also has a suppress context manager we can just import
import sys
from dataclasses import dataclass
from types import TracebackType
from typing import Optional
from functools import wraps

class suppress(ContextDecorator):

    """Context manager that suppresses exceptions of given type."""

    def __init__(self, *exception_types):
        self.exception_types = exception_types

    # def __call__(self, function):
    #     @wraps(function)
    #     def wrapper(*args, **kwargs):
    #         with self:
    #             return function(*args, **kwargs)
    #     return wrapper

    def __enter__(self):
        """Called when we enter our with block"""
        return self

    def __exit__(self, exception_type, exception, traceback):
        """Called when we exit our with block"""
        self.exception = exception
        self.traceback = traceback
        return isinstance(exception, self.exception_types)

@dataclass
class ExceptionInfo:
    """Dictates the type excepted for our attributes and works as documentation"""
    exception: Optional[Exception] = None
    traceback: Optional[TracebackType] = None

@contextmanager  # turns a generator function into a context manager
def suppress(*exception_types):
    """Context manager that suppresses exceptions of given type """
    info = ExceptionInfo()
    try:
        """same as __enter__ magic method"""
        yield info  # with suppress(VALUE) as var, it yields info and names it var
    except exception_types as e:
        """same as __exit__ magic method"""
        info.exception = e
        # info.traceback = sys.exc_info()[2]
        info.traceback = e.__traceback__  # Every raised exception in Python 3+ has a __traceback__ attribute
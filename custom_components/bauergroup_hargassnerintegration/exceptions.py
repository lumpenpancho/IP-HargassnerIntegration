"""Custom exceptions for Hargassner Integration."""


class HargassnerException(Exception):
    """Base exception for Hargassner integration."""


class HargassnerConnectionError(HargassnerException):
    """Exception raised when connection to boiler fails."""


class HargassnerTimeoutError(HargassnerException):
    """Exception raised when connection times out."""


class HargassnerAuthenticationError(HargassnerException):
    """Exception raised when authentication fails."""


class HargassnerParseError(HargassnerException):
    """Exception raised when message parsing fails."""


class HargassnerFirmwareError(HargassnerException):
    """Exception raised when firmware version is unsupported."""

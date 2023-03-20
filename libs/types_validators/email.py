import re

_email_format_regex_pattern = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$"
_email_format_regex = re.compile(_email_format_regex_pattern)


class Email(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(examples=["test@test.com"])

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("string required")

        if len(v) > 250:
            raise ValueError("Invalid email length, too long")

        m = _email_format_regex.match(v)
        if not m:
            raise ValueError("Invalid email format")

        return cls(v)

    def __repr__(self):
        return f"Email({super().__repr__()})"

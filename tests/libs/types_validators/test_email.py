import pytest


def test_email_invalid_type():
    from libs.types_validators.email import Email

    # invalid type
    with pytest.raises(TypeError):
        Email.validate(100)

    with pytest.raises(TypeError):
        Email.validate(None)


def test_email_invalid_value():
    from libs.types_validators.email import Email

    # too long
    with pytest.raises(ValueError):
        Email.validate("b" * 300)

    # invalid format
    with pytest.raises(ValueError):
        Email.validate("")

    with pytest.raises(ValueError):
        Email.validate("a")

    with pytest.raises(ValueError):
        Email.validate("a@")


def test_email_valid_value():
    from libs.types_validators.email import Email

    # happy path
    assert Email.validate("test@test.com")

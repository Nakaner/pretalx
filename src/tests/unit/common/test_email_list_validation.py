import pytest

from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from pretalx.common.mail import EmailListValidator

def _check_email_validator_no_throws(addr_str):
    try:
        EmailListValidator(addr_str)
    except ValidationError:
        pytest.fail("unexptected Validation error for '{}'".formt(addr_str))


def test_email_validator_valid_addresses():
    valid_addresses = [
            "joe@average.io",
            "henk@manylines.co.uk",
            "frank@localhost"
    ]
    _check_email_validator_no_throws(",".join(valid_addresses))


def test_email_validator_valid_addresses_and_spaces():
    valid_addresses = [
            "joe@average.io",
            "henk@manylines.co.uk",
            "frank@localhost"
    ]
    _check_email_validator_no_throws(",".join(valid_addresses))


def test_email_validator_valid_address():
    _check_email_validator_no_throws("hello@company.com")

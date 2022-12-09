from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re

class CharacterValidator:
    def validate(self, password, user=None):
        if not (re.search("[A-Z]", password) and re.search("[a-z]", password)\
            and re.search("[0-9]", password)):
            raise ValidationError(
                _("Password must contain at least one uppercase, lowercase and numeric character"),
                code = 'password_too_simple',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least one uppercase, lowercase and numeric character."
        )
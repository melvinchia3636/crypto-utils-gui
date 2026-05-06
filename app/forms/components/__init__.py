import sys

from ...base.form_component import FormComponent
from ...helpers.discover_modules import discover_modules

BUILDERS = {
    c.name: c.build for c in discover_modules(sys.modules[__name__], FormComponent)
}

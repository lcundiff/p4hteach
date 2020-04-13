#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

##
# This returns all dirs within the `tests/` dir that do not start
# with a `_` (this will be considred private)
def test_modules():
    dirs = [x[0] for x in os.walk("tests")]
    return list(
        filter(lambda path: path != "tests" and path.split("/")[1] != "_", dirs)
    )


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.test_settings")
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(test_modules())
    sys.exit(bool(failures))
#!/bin/sh
. /harvey/.harvey # Source the functions for Harvey

# INSTALL
pip install pylint || harvey_fail
pip install pylint-exit || harvey_fail

# TEST
pylint downloader/*.py || harvey_fail

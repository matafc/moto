import boto

try:
    from unittest.case import skipUnless
except ImportError:
    # use unittest2 for python 2.6
    from unittest2.case import skipUnless


def version_tuple(v):
    return tuple(map(int, (v.split("."))))


def requires_boto_gte(version):
    """Decorator for requiring boto version greater than or equal to 'version'"""
    boto_version = version_tuple(boto.__version__)
    required = version_tuple(version)
    return skipUnless(boto_version >= required, 'Requires boto version %s' % version)


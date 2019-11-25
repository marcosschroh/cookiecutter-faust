#!/bin/sh

VERSION=`cat setup.py | grep '__version__ =' | sed 's/__version__ = //' | sed 's/"//g'`

# Creating git tag
echo "Creating tag version v${VERSION}:"
git tag -a v${VERSION} -m 'Bump version v${VERSION}'

echo "Consider doing: git push origin v${VERSION}"

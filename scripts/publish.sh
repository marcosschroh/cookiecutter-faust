#!/bin/sh

VERSION=`cat setup.py | grep '__version__ =' | sed 's/__version__ = //' | sed 's/"//g'`

# Creating git tag
echo "Creating tag version ${VERSION}:"
git tag -a ${VERSION} -m 'Bump version ${VERSION}'

echo "Consider doing: git push origin ${VERSION}"

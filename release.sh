#!/bin/bash

set -e

poetry run vrz minor

git add pyproject.toml
NEW_VERSION=$(poetry run vrz latest)
git commit -m "Released version v$NEW_VERSION"
git push

poetry publish --build
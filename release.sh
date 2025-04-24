#!/bin/bash

set -e
poetry version minor
NEW_VERSION=$(poetry version -s)
git add pyproject.toml
git commit -m "Released version v$NEW_VERSION"
git tag "v$NEW_VERSION"
git push origin main --tags

poetry publish --build
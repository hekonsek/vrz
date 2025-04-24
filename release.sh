#!/bin/bash

set -e

poetry run vrz minor

poetry publish --build
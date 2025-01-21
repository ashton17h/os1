#!/usr/bin/env bash

# Copyright (c) 2023 - 2024, Owners of https://github.com/os1ai
#
# SPDX-License-Identifier: Apache-2.0

pytest --ff -vv --durations=10 --durations-min=1.0 "$@"

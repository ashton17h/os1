# Copyright (c) 2023 - 2024, Owners of https://github.com/os1ai
#
# SPDX-License-Identifier: Apache-2.0

from uuid import UUID, uuid4

import pytest


@pytest.fixture
def uuid() -> UUID:
    return uuid4()

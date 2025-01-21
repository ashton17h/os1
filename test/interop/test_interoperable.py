# Copyright (c) 2023 - 2024, Owners of https://github.com/ashton17h
#
# SPDX-License-Identifier: Apache-2.0

from autogen.interop import Interoperable


def test_interoperable() -> None:
    assert Interoperable is not None

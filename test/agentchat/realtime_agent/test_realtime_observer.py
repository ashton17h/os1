# Copyright (c) 2023 - 2024, Owners of https://github.com/ashton17h
#
# SPDX-License-Identifier: Apache-2.0

from asyncio import sleep
from typing import Any
from unittest.mock import MagicMock

import pytest
from asyncer import create_task_group

from autogen.agentchat.realtime_agent import RealtimeObserver


class MyObserver(RealtimeObserver):
    def __init__(self, mock: MagicMock) -> None:
        super().__init__()
        self.mock = mock

    async def initialize_session(self) -> None:
        pass

    async def run_loop(self) -> None:
        self.mock("started")
        try:
            self.mock("running")
            print("-> running", end="", flush=True)
            while True:
                await sleep(0.05)
                print(".", end="", flush=True)
        finally:
            print("stopped", flush=True)
            self.mock("stopped")

    async def on_event(self, event: dict[str, Any]) -> None:
        pass


class TestRealtimeObserver:
    @pytest.mark.asyncio
    async def test_shutdown(self) -> None:
        mock = MagicMock()
        observer = MyObserver(mock)

        agent = MagicMock()

        try:
            async with create_task_group() as tg:
                tg.soonify(observer.run)(agent)
                await sleep(1.0)
                tg.cancel_scope.cancel()

        except Exception as e:
            print(e)

        mock.assert_any_call("started")
        mock.assert_any_call("running")
        mock.assert_called_with("stopped")

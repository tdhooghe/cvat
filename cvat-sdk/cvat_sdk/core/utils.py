# Copyright (C) 2022 Intel Corporation
# Copyright (C) 2022 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Any, Dict, Sequence

import urllib3


def assert_status(code: int, response: urllib3.HTTPResponse) -> None:
    if response.status != code:
        raise Exception(f"Unexpected status code received {response.status}")


def filter_dict(
    d: Dict[str, Any], *, keep: Sequence[str] = None, drop: Sequence[str] = None
) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if (not keep or k in keep) and (not drop or k not in drop)}

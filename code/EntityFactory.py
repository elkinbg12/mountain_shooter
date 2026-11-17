#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Entity import Entity


class EntityFactory:

    def getEntity(self, entityType: str) -> -> Entity:
        pass

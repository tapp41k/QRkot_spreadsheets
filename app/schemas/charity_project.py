from typing import Optional
from datetime import datetime

from pydantic import Field, validator, PositiveInt, Extra

from .base import CommonBase


class CharityProjectBase(CommonBase):
    """Базовый класс схемы, от которого наследуем схемы для проекта."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)

    class Config:
        extra = Extra.forbid

    @validator('name')
    def name_not_empty(cls, value: str):
        if not value:
            raise ValueError('Не может быть пустым')
        return value

    @validator('description')
    def description_not_empty(cls, value: str):
        if not value:
            raise ValueError('Не может быть пустым')
        return value


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    @validator('fully_invested')
    def fully_invested_not_edit(cls, value: bool):
        if value:
            raise ValueError('Закрытый проект нельзя редактировать')
        return value

    @validator('invested_amount')
    def invested_amount_not_edit(cls, value: int):
        if value or value == 0:
            raise ValueError('invested_amount нельзя редактировать')
        return value

    @validator('create_date')
    def create_date_exit(cls, value: datetime):
        if value:
            raise ValueError('Нельзя редактировать')
        return value

    @validator('close_date')
    def close_date_exit(cls, value: datetime):
        if value:
            raise ValueError('Нельзя редактировать')
        return value


class CharityProjectDB(CharityProjectBase):
    id: int

    class Config:
        orm_mode = True

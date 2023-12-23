from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectCreate, CharityProjectUpdate


class CRUDCharityProject(CRUDBase[
    CharityProject,
    CharityProjectCreate,
    CharityProjectUpdate
]):
    """Класс круд для CharityProject, унаследованный от CRUDBase."""

    async def get_multi_not_closed(
            self,
            session: AsyncSession
    ) -> List[CharityProject]:
        """Получение не закрытых проектов."""
        charity_projects = await session.execute(
            select(self.model.id).where(
                self.model.fully_invested.is_(False)
            )
        )
        return charity_projects.scalars().all()

    async def get_charity_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        """Получение id проекта по имени."""
        charity_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        charity_project_id = charity_project_id.scalars().first()
        return charity_project_id

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list[CharityProject]:
        """Получение закрытых проектов отсортированых по дате закрытия."""
        charity_projects = await session.execute(
            select(
                self.model.id,
                self.model.name,
                self.model.description,
                self.model.create_date,
                self.model.close_date
            ).where(
                self.model.fully_invested.is_(True)
            ).order_by(self.model.close_date - self.model.create_date)
        )
        return charity_projects.all()


charity_project_crud = CRUDCharityProject(CharityProject)

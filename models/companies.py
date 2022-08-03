from pydantic import BaseModel

from pycamel import CamelEnum


class CompanyStatuses(CamelEnum):
    ACTIVE = 'ACTIVE'
    BANKRUPT = 'BANKRUPT'
    CLOSED = 'CLOSED'


class Company(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: CompanyStatuses

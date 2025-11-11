# Ensure every model module is imported so SQLAlchemy registers all table classes
from . import (
    customers,
    categories,
    menu_items,
    resources,
    recipes,
    orders,
    order_details,
    payments,
    promotions,
    reviews,
)

# Import the shared Base + engine used across all models
from ..dependencies.database import Base, engine


def create_tables() -> None:
    """
    Create all tables defined on the shared Base.
    This works because importing the modules above registers their table classes.
    """
    Base.metadata.create_all(bind=engine)

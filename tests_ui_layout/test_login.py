import time
from playwright.sync_api import Playwright, sync_playwright
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_logged_user_can_view_my_orders_menu(login_set_up) -> None:
    # Assess - Given
    page = login_set_up

    # Act - When/And
    page.click("[aria-label='symon.storozhenko account menu']")

    # Assert - Then
    assert page.is_visible("text=My Orders")



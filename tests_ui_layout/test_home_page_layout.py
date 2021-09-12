from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright
import pytest

@pytest.mark.integration
def test_about_us_section_verbiage(login_set_up) -> None:
    # Assess - Given
    page = login_set_up

    assert not page.is_visible(HomePage.celebrating_beauty_header)
    # Click text=playwright-practice was founded by a group of like-minded fashion devotees, dete
    assert page.is_visible(HomePage.celebrating_beauty_body)


@pytest.mark.regression
def test_about_us_section_verbiage_2(login_set_up) -> None:
    # Assess - Given
    page = login_set_up

    assert page.is_visible(HomePage.celebrating_beauty_header)
    # Click text=playwright-practice was founded by a group of like-minded fashion devotees, dete
    assert page.is_visible(HomePage.celebrating_beauty_body)

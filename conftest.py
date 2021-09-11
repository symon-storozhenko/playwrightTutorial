import time
import pytest
from playwright.sync_api import Browser, Page



@pytest.fixture(scope="function")
def set_up(browser):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page
    page.close()


@pytest.fixture(scope="function")
def login_set_up(set_up):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()

    page = set_up

    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log In\")")
        else:
            login_issue = False
        time.sleep(0.1)
    # Click [data-testid="signUp.switchToSignUp"]
    page.click("[data-testid=\"signUp.switchToSignUp\"]", timeout=2000)
    # page.click(":nth-match(:text('Log In'), 2)", timeout=2000)
    page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
    # page.click("[data-testid='siteMembers.container'] input[type='email']")
    # page.fill("[data-testid='siteMembers.container'] input[type='email']", "symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    page.fill("input[type='password']", 'test123')
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")

    yield page


@pytest.fixture
def go_to_new_collection_page(page):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page
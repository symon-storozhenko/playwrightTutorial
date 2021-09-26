import os
import time
import pytest

headless_bool = True
slowmo_value = 0

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD
    headless_bool = False
    slowmo_value = 300


@pytest.fixture()
def set_up(page):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page
    page.close()


@pytest.fixture(scope='session')
def context_creation(playwright):
    # Assess - Given
    browser = playwright.chromium.launch(headless=headless_bool, slow_mo=slowmo_value)
    context = browser.new_context()
    # # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

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
    page.fill("input[type='password']", PASSWORD)
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")

    # Save storage state into the file.
    storage = context.storage_state(path="state.json")

    # Create a new context with the saved storage state.

    yield context
    # time.sleep(5)


@pytest.fixture()
def login_set_up(context_creation, browser):
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page
    # time.sleep(3)
    page.close()


# @pytest.fixture()
# def login_set_up(context_creation):
#     context = context_creation
#     page = context.new_page()
#     page.goto("https://symonstorozhenko.wixsite.com/website-1")
#     page.set_default_timeout(3000)
#
#     yield page
#     time.sleep(3)
#     page.close()


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
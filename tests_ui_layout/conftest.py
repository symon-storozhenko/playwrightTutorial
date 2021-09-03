import pytest


@pytest.fixture(scope="function")
def login(browser):
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(5000)

    # Act - When/And
    # page.click("button:has-text('Log In')", timeout=2000)
    page.click("text=Log In")
    # page.click("'Log In'", timeout=2000)
    page.click("[data-testid='signUp.switchToSignUp']")
    page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
    # page.click("[data-testid='siteMembers.container'] input[type='email']")
    # page.fill("[data-testid='siteMembers.container'] input[type='email']", "symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    page.fill("input[type='password']", "test123")
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")
    # page.click("[aria-label='symon.storozhenko account menu']")

    # Assert - Then
    # assert page.is_visible("text=My Orders")
    yield page
    page.close()
    # ---------------------
    # context.close()
    # browser.close()
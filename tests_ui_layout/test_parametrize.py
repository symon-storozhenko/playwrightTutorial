import time

import pytest
from playwright.sync_api import Playwright, sync_playwright


@pytest.mark.parametrize("email", ["symon.storozhenko@gmail.com",
                                            pytest.param("fakeemail", marks=pytest.mark.xfail),
                                            pytest.param("symon.storozhenko@gmail", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("passwrd", ["test123",
                                            pytest.param("fakepasswrd", marks=pytest.mark.xfail),
                                            "test123"])
def test_user_can_login(page, email, passwrd) -> None:
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
    page.fill('input:below(:text("Email"))', email)
    page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    page.fill("input[type='password']", passwrd)
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")
    # page.goto("https://symonstorozhenko.wixsite.com/website-1/shop")
    page.wait_for_load_state()
    page.expect_navigation(url="https://symonstorozhenko.wixsite.com/website-1",
                           wait_until="domcontentloaded",
                           timeout=5000)
    page.wait_for_selector("[aria-label=\"symon.storozhenko account menu\"]")
    assert not page.is_visible("text=Log In")


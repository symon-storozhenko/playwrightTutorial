import os
import time

from playwright.sync_api import Playwright, sync_playwright

import pytest


def use_storage_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # Open new page

    os_environ = os.environ
    # storage = context.storage_state(path='../state.json')
    context = browser.new_context(storage_state="../state.json")
    context.new_page().goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.click("[aria-label='symon.storozhenko account menu']")
    time.sleep(2000)
    # Assert - Then
    # assert page.is_visible("text=My Orders")
    browser.close()
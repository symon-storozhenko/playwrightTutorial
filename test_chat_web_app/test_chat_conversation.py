import time


def otest_private_chat_messsage_was_delivered_successfully(login_set_up_for_chat):
    page, page2 = login_set_up_for_chat
    page.click("#container_user >> :nth-match(div:has-text(\"symon_storozhenko\"), 3)")
    # Click text=Private
    page.click("text=Private")
    # Click #message_content
    page.click("#message_content")
    # Fill #message_content
    page.fill("#message_content", "yo")
    # Press Enter
    page.press(
        "text=symon_storozhenko Ignore Settings Report Delete hey 29/09 20:05 hi 29/09 20:15 h >> [placeholder=\"Type something ...\"]",
        "Enter")

    # Validate the message was delivered

    page2.click("#get_private i")
    # Click #large_modal_content >> text=stosymon
    page2.click("#large_modal_content >> text=stosymon")
    # Click #priv246994882 >> text=yo!2
    page2.click("#priv246994882 >> text=yo!2")
    # Click #private_content
    # time.sleep(5)
    assert page2.is_visible("#priv246994882 >> text=yo!2")

    # Click #priv246775542 >> text=hey
    # page.click("#priv246775542 >> text=hey")
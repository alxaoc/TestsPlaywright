from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dex-trade.com/")
    page.frame_locator("iframe[name='helpcrunch-iframe']").locator("[data-test-id='popup_close_button']").get_by_role("img").click()
    page.get_by_role("button", name="Accept").click()
    page.wait_for_timeout(1000)

    page.locator("[data-test-id='header login']").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("qa-@ukr.net")
    page.get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("@Dex-Trade17")
    page.wait_for_timeout(2000)
    page.locator("[data-test-id='login btn']").click()

    page.locator("[data-test-id='buy-crypto']").click()
    page.wait_for_timeout(2000)
    page.frame_locator("iframe[name='helpcrunch-iframe']").locator("path").nth(1).click()
    page.wait_for_timeout(2000)
    page.locator("[data-test-id='markets']").click()
    page.wait_for_timeout(3000)
    page.get_by_text("Trade Spot Trading Work with your own funds Demo Trading No-risk trading Quick E").hover()
    page.wait_for_timeout(100)
    page.locator("[data-test-id='spot trading']").click()
    page.wait_for_timeout(6000)
    page.get_by_text("Trade Spot Trading Work with your own funds Demo Trading No-risk trading Quick E").hover()
    page.wait_for_timeout(100)
    page.locator("[data-test-id='demo trading']").click()
    page.wait_for_timeout(3000)
    page.get_by_text("Trade Spot Trading Work with your own funds Demo Trading No-risk trading Quick E").hover()
    page.wait_for_timeout(100)
    page.locator("[data-test-id='quick exchange']").click()
    page.wait_for_timeout(3000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

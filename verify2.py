from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("file:///app/index.html")
    page.wait_for_timeout(500)

    # Click start to go to game screen
    page.get_by_role("button", name="Start Game ▶").click()
    page.wait_for_timeout(500)

    # Click view progress report
    page.get_by_role("button", name="View Progress Report").click()
    page.wait_for_timeout(500)

    # Take a screenshot
    page.screenshot(path="/home/jules/verification/screenshots/verification2.png")
    page.wait_for_timeout(500)

    # Click outside the modal
    page.mouse.click(10, 10)
    page.wait_for_timeout(500)

    # Take a screenshot
    page.screenshot(path="/home/jules/verification/screenshots/verification3.png")
    page.wait_for_timeout(500)

if __name__ == "__main__":
    import os
    os.makedirs("/home/jules/verification/videos", exist_ok=True)
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()  # MUST close context to save the video
            browser.close()

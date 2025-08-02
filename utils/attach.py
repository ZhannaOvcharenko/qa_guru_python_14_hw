import allure
import requests
from selene import browser
import os


def add_screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG
    )


def add_html():
    allure.attach(
        browser.driver.page_source,
        name="Page Source",
        attachment_type=allure.attachment_type.HTML
    )


def add_logs():
    try:
        logs = browser.driver.get_log("browser")
        log_text = "\n".join([f"{log['level']}: {log['message']}" for log in logs])
        allure.attach(log_text, name="Browser Logs", attachment_type=allure.attachment_type.TEXT)
    except:
        pass


def add_video(session_id: str):
    selenoid_url = os.getenv("SELENOID_URL")
    if not selenoid_url or not session_id:
        return

    video_url = f"https://{selenoid_url}/video/{session_id}.mp4"
    try:
        response = requests.get(video_url, verify=False)
        if response.status_code == 200:
            allure.attach(
                response.content,
                name="Test Video",
                attachment_type=allure.attachment_type.MP4
            )
    except Exception as e:
        print(f"[attach.py] Не удалось прикрепить видео: {e}")
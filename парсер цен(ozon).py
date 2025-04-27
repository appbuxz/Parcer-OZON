import asyncio
from playwright.async_api import async_playwright

async def scrape_page():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()

        url = "https://ozon.kz/product/xiaomi-smartfon-redmi-note-13-8-256-gb-chernyy-1398073212/?at=NOtw6mY1VclNWpvzCml0KWnh4rAnLZCnpOGR3FPrvxkp&avtc=1&avte=4&avts=1738065541"
        await page.goto(url)

        await page.wait_for_load_state('networkidle')
        page_content = await page.content()
        print(page_content)

        try:
            await page.wait_for_selector('.tl0_27 t0l_27 lt5_27', timeout=60000)
            print("Элемент найден.")
        except Exception as e:
            print(f"Ошибка: {e}")

        await browser.close()

async def main():
    while True:
        await scrape_page()
        print("Ждем час до следующего запуска...")
        await asyncio.sleep(3600)  # Ждем 1 час

# Запуск
if __name__ == "__main__":
    asyncio.run(main())
#13213213213

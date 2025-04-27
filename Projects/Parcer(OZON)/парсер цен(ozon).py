import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Запуск браузера Firefox
        browser = await p.firefox.launch(headless=False)  # headless=False — для отладки с открытым окном
        page = await browser.new_page()

        url = "https://ozon.kz/product/xiaomi-smartfon-redmi-note-13-8-256-gb-chernyy-1398073212/?at=NOtw6mY1VclNWpvzCml0KWnh4rAnLZCnpOGR3FPrvxkp&avtc=1&avte=4&avts=1738065541"  # Укажи нужный URL на Озоне
        await page.goto(url)

        # Дожидаемся, пока страница полностью загрузится
        await page.wait_for_load_state('networkidle')  # Ждем, пока все сетевые запросы завершатся

        # Печатаем HTML-контент страницы для диагностики
        page_content = await page.content()
        print(page_content)  # Проверим, что на странице есть нужные элементы

        # Ищем конкретный элемент с нужным классом
        try:
            await page.wait_for_selector('.tl0_27 t0l_27 lt5_27', timeout=60000)  # Поменяй на свой класс
            print("Элемент найден.")
        except Exception as e:
            print(f"Ошибка: {e}")

        # Закрываем браузер
        await browser.close()

# Запуск асинхронной функции
asyncio.run(main())

# 123

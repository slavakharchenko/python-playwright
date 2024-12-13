from playwright.sync_api import Page, Locator, expect
from po.blocks.base_block import BaseBlock
from utils import get_day_and_check_next_month


class DataPicker(BaseBlock):
    def __init__(self, page: Page, root: Locator):
        super().__init__(page, root)
        self._datePickerPopUp = self.page.locator(
            "[data-test='NewDatePickerOpen']"
        )
        self._submitBtn = self._datePickerPopUp.locator(
            "[data-test='SearchFormDoneButton']"
        )
        self._calendarContainer = self._datePickerPopUp.locator(
            "[data-test='CalendarContainer']"
        )

    def open(self):
        self.root.click()
        expect(
            self._datePickerPopUp, "DatePicker pop up is not visible"
        ).to_be_visible()

    def fillDay(self, day: int):
        day, is_next_month = get_day_and_check_next_month(day)

        calendar = (
            self._calendarContainer.all()[1]
            if (is_next_month)
            else self._calendarContainer.all()[0]
        )
        calendar.get_by_text(str(day)).click()

    def submit(self):
        self._submitBtn.click()

        date = self.root.text_content()
        return date

    def setOneWayDay(self, day: int):
        self.open()
        self.fillDay(day)
        date = self.submit()  # verify date after submit
        return date
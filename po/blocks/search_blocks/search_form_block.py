import re
from playwright.sync_api import Page, Locator
from data.enums import SearchMode, Way
from po.blocks.base_block import BaseBlock
from po.blocks.common_blocks import DataPicker


class SearchFormBlock(BaseBlock):
    _SEARCH_FIELD = "SearchPlaceField-"
    _PICKED_MODAL = "PlacepickerModalOpened-"

    def __init__(self, page: Page, root: Locator):
        super().__init__(page, root)

        self._search = self.root.locator("[data-test='LandingSearchButton']")
        self._bookingCheckbox = self.page.locator(
            "[data-test='bookingCheckbox'] .orbit-checkbox-icon-container"
        )

        # ----- Date Picker -----
        self._datePickerRoot = self.page.locator(
            "[data-test='SearchDateInput']"
        )
        self.datePicker = DataPicker(self.page, self._datePickerRoot)

        # ----- Mode pop up -----
        self._modeButton = self.root.locator(
            "[data-test^='SearchFormModesPicker-active']"
        )
        self._modePopUp = self.page.locator("[data-test='ModesPopup']")

        # ----- From - To block -----
        self._pickedWays = self.root.locator(
            "[data-test='PlacePickerInputPlace']"
        )

    def submit(self):
        self._search.click()

    def checkBookingAccommodation(self, state=False):
        expecterClass = (
            "[&>svg]:visible" if state else "[&>svg]:invisible"
        )
        classAttr = self._bookingCheckbox.get_attribute("class")

        if expecterClass not in classAttr:
            self._bookingCheckbox.click()

    # ----- Mode pop up -----
    def getMode(self):
        return self._modeButton.inner_text()

    def verifyModePopUp(self, actualMode: SearchMode):
        mode = self.getMode()

        assert (
            mode == actualMode.value
        ), f"Expected mode: {actualMode.value}, but got: {mode}"

    def chooseMode(self, modeType: SearchMode, verify=True):
        self._modeButton.click()

        modeOption = self._modePopUp.get_by_text(modeType.value)
        modeOption.click()
        if verify:
            self.verifyModePopUp(modeType)

    # ----- From - To block -----
    def deleteAllChoosenWays(self):
        pickedWaysName = [way.inner_text for way in self._pickedWays.all()]
        print(f"Delete picked ways: {pickedWaysName}")

        for way in self._pickedWays.all():
            way.locator("[data-test='PlacePickerInputPlace-close']").click()

    def fillWay(self, wayType: Way, inputWay: str, suggesterWay: str):
        way = (
            Way.ORIGIN.value
            if wayType == Way.ORIGIN
            else Way.DESTINATION.value
        )

        searchFieldSelector = f"[data-test='{self._SEARCH_FIELD + way}']"
        pickerModalSelector = f"[data-test='{self._PICKED_MODAL + way}']"

        self.root.locator(searchFieldSelector).locator(
            "[data-test='SearchField-input']"
        ).fill(inputWay)
        self.page.locator(pickerModalSelector).get_by_text(
            re.compile(suggesterWay)
        ).click()

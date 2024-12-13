import pytest
from po import SearchPage, ResultPage
from data.enums.common_enum import SearchMode, Way

@pytest.mark.test_id_0001
def test_basic_search(search_page: SearchPage, result_page: ResultPage):
    search_page.navigate()
    search_page.acceptCoockie()

    search_page.searchForm.chooseMode(SearchMode.ONY_WAY)
    search_page.searchForm.deleteAllChoosenWays()
    search_page.searchForm.fillWay(
        Way.ORIGIN, "RTM", "RTM Rotterdam The Hague"
    )
    search_page.searchForm.fillWay(
        Way.DESTINATION, "MAD", "MAD Adolfo Suárez Madrid–Barajas"
    )
    search_page.searchForm.datePicker.setOneWayDay(day=7)
    search_page.searchForm.checkBookingAccommodation(state=False)
    search_page.searchForm.submit()

    result_page.check_url_includes()
    result_page.checkResultIsNotEmpty()

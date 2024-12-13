import pytest
from pytest_bdd import scenarios, given, when, then
from po import SearchPage, ResultPage
from data.enums.common_enum import SearchMode, Way

scenarios('../features/search.feature')

@given('As an not logged user navigate to homepage')
def gotoHomePage(searchPage: SearchPage):
    searchPage.navigate()
    searchPage.acceptCoockie()

@when('I select one-way trip type')
def selectOneWay(searchPage: SearchPage):
    searchPage.searchForm.chooseMode(SearchMode.ONY_WAY)

@when('Set as departure airport RTM')
def fillDeparture(searchPage: SearchPage):
    searchPage.searchForm.deleteAllChoosenWays()
    searchPage.searchForm.fillWay(Way.ORIGIN, "RTM", "RTM Rotterdam The Hague")
    
@when('Set the arrival airport MAD')
def fillArrival(searchPage: SearchPage):
    searchPage.searchForm.fillWay(
        Way.DESTINATION, "MAD", "MAD Adolfo Suárez Madrid–Barajas"
    )

@when('Set the departure time 1 week in the future starting current date')
def setDate(searchPage: SearchPage):
    searchPage.searchForm.datePicker.setOneWayDay(day=7)

@when('Uncheck the `Check accommodation with booking.com` option')
def checkBookingAccommodation(searchPage: SearchPage):
    searchPage.searchForm.checkBookingAccommodation(state=False)
    
@when('Click the search button')
def submit(searchPage: SearchPage):
    searchPage.searchForm.submit()

@then('I am redirected to search results page')
def checkResult(resultPage: ResultPage):
    resultPage.check_url_includes()
    resultPage.checkResultIsNotEmpty()


### --------------------------- CLASSIC TEST --------------------------- ###

# @pytest.mark.test_id_0001
# def test_basic_search(searchPage: SearchPage, resultPage: ResultPage):
#     searchPage.navigate()
#     searchPage.acceptCoockie()

#     searchPage.searchForm.chooseMode(SearchMode.ONY_WAY)
#     searchPage.searchForm.deleteAllChoosenWays()
#     searchPage.searchForm.fillWay(
#         Way.ORIGIN, "RTM", "RTM Rotterdam The Hague"
#     )
#     searchPage.searchForm.fillWay(
#         Way.DESTINATION, "MAD", "MAD Adolfo Suárez Madrid–Barajas"
#     )
#     searchPage.searchForm.datePicker.setOneWayDay(day=7)
#     searchPage.searchForm.checkBookingAccommodation(state=False)
#     searchPage.searchForm.submit()

#     resultPage.check_url_includes()
#     resultPage.checkResultIsNotEmpty()

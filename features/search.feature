Feature: Basic search form
    @test_id_0001
    Scenario: T1 - One way flight search
        Given As an not logged user navigate to homepage
        When I select one-way trip type
        And Set as departure airport RTM
        And Set the arrival airport MAD
        And Set the departure time 1 week in the future starting current date
        And Uncheck the `Check accommodation with booking.com` option
        And Click the search button
        Then I am redirected to search results page
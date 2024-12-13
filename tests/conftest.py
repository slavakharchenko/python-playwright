import pytest
from playwright.sync_api import Page
from po import SearchPage, ResultPage

@pytest.fixture(scope="function", autouse=True)
def trace_on_failure(context, request):
    # Start tracing before each test
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield

    # Stop tracing and save only on failure
    if request.node.rep_call.failed:
        trace_path = f"reports/traces/{request.node.name}.zip"
        context.tracing.stop(path=trace_path)
    else:
        context.tracing.stop()
        
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
           "user_agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.124 Safari/537.36"
            ),
        "locale": "en-US",
    }


@pytest.fixture
def searchPage(page: Page) -> SearchPage:
    return SearchPage(page)


@pytest.fixture
def resultPage(page: Page) -> ResultPage:
    return ResultPage(page)
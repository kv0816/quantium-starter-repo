import time
import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app_runner():
    """Fixture to load the Dash app for testing."""
    return import_app("app")  # Ensure 'app.py' is the correct filename


def test_header_is_present(dash_duo, app_runner):
    """Test if the header is present."""
    dash_duo.start_server(app_runner)

    # Allow time for elements to load
    time.sleep(2)

    # Check for the header text
    assert dash_duo.wait_for_element("h1").text == "Pink Morsels Sales Data"


def test_graph_is_present(dash_duo, app_runner):
    """Test if the graph is present."""
    dash_duo.start_server(app_runner)

    time.sleep(2)

    # Ensure that the graph element exists
    assert dash_duo.find_element("#sales-chart")


def test_region_picker_is_present(dash_duo, app_runner):
    """Test if the region selection radio buttons are present."""
    dash_duo.start_server(app_runner)

    time.sleep(2)

    # Ensure the radio buttons exist
    radio_buttons = dash_duo.find_element("#region-selector")
    assert radio_buttons is not None


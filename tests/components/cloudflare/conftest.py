"""Define fixtures available for all tests."""
from pytest import fixture

from tests.async_mock import patch

@fixture
def cfupdate(hass):
    """Mock the CloudflareUpdater for easier testing."""
    with patch(
        "homeassistant.components.cloudflare.CloudflareUpdater"
    ) as mock_api:
        instance = mock_api.return_value
        instance.get_zone_id.return_value = "mock-zone-id"

        yield mock_api

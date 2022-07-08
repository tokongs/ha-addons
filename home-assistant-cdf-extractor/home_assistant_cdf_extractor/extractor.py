import datetime
import os
from typing import Iterable, List, NewType

import arrow
from cognite.client.data_classes.raw import Row
from cognite.extractorutils.base import Extractor
from cognite.extractorutils.rest import RestExtractor
from cognite.extractorutils.uploader_types import Event, InsertDatapoints, RawRow
from dateutil import parser

from home_assistant_cdf_extractor import __version__
from home_assistant_cdf_extractor.config import Config
from home_assistant_cdf_extractor.dto import StatesResponse

extractor = RestExtractor(
    name="home_assistant_cdf_extractor",
    description="Extract data from Home Assistant",
    version=__version__,
    config_class=Config,
    base_url=os.environ['HA_BASE_URL'],
    headers={
        "Authorization": f"Bearer {os.environ['HA_TOKEN']}",
        "Content-Type": "application/json",
    }
)


@extractor.get(f"/api/states", response_type=StatesResponse, interval=10)
def get_current_states(states: StatesResponse) -> Iterable[RawRow]:
    for state in states.items:
        entity_id = state.entity_id
        if not Extractor.get_current_config().ha.entity_should_be_exported(entity_id):
            continue
        state.attributes["entity_id"] = entity_id
        state.attributes["state"] = state.state
        state.attributes["last_updated"] = state.last_updated
        state.attributes["last_changed"] = state.last_changed

        yield RawRow(
            "ha",
            "states",
            Row(f"{entity_id}-{state.last_updated}", state.attributes, parser.parse(state.last_updated, ignoretz=True).timestamp()),
        )

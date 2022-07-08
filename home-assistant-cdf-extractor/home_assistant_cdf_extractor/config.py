import re
from dataclasses import dataclass
from typing import List, Optional

from cognite.extractorutils.rest.extractor import ExtractorConfig, SourceConfig
from cognite.extractorutils.uploader_extractor import UploaderExtractorConfig


@dataclass
class HAConfig:
    token: str
    base_url: str
    entities: List[str]

    def entity_should_be_exported(self, entity_id: str) -> bool:
        return entity_id in self.entities


@dataclass
class Config(UploaderExtractorConfig):
    ha: HAConfig
    source: SourceConfig = SourceConfig()
    extractor: ExtractorConfig = ExtractorConfig()

#!/usr/bin/env bashio
tempio -conf /data/options.json -template extractor_config.yaml.tmpl -out extractor_config.yaml

HA_BASE_URL=$(bashio::config 'ha_base_url')
export HA_BASE_URL

HA_TOKEN=$(bashio::config 'ha_token')
export HA_TOKEN

python src extractor_config.yaml

# Home Assistant CDF extractor

This extractor runs as a [Home Assistant Addon](https://www.home-assistant.io/addons/) and enables the export of entity states to CDF. It connects to 
the Home Assistant Core API to read the current states every 10 seconds. 

## Installation
This can be installed manually, explained [here](https://developers.home-assistant.io/docs/add-ons/tutorial). But the easier solution is to add the repository using the link in the [repo README](https://github.com/tokongs/ha-addons)


## Configuration

| name                                    | description                                                                                                           | default                     |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------|
| ha_base_url                             | Base URL of the HA Core API. If you are running HA OS without custom network config <br>the default should be enough. | http://homeassistant:8123   |
| ha_token                                | A token the extractor will use to authenticate against the HA API.                                                    | null                        |
| ha_entitites                            | A list of entities, ex: sensor.adguard_queries, sensor.healthy_home_coach_co2                                         | []                          |
| cognite_base_url                        | Base URL to CDF.                                                                                                      | https://api.cognitedata.com |
| cognite_client_secret                   | OIDC Client secret the extractor will use to authenticate against CDF.                                                | null                        |
| cognite_client_id                       | OIDC Client id the extractor will use to authenticate against CDF.                                                    | null                        |
| cognite_token_url                       | OIDC Token URL for authentication against CDF. ex: https://login.microsoftonline.com/${tenant_id}/oauth2/v2.0/token   | null                        |
| cognite_project                         | CDF project.                                                                                                          | null                        |
| cognite_dataset_id                      | The CDF dataset to extract to.                                                                                        | null                        |
| cognite_extraction_pipeline_external_id | External ID of the configured extraction pipeline.                                                                    | null                        |


The ADS events are illustrated in a diagram at the bottom of this document

## Event: ADS discovers that a journal article cites a Zenodo (software) record (not yet in the ADS database)

Little bit of background: the ADS reference resolving process stores data in a file of all citations where a publication in the ADS Universe has a reference string in its bibliography with one of a set of identifiers (doi:, ascl:, Github or Bitbucket URLs). In the ADS back-office, a pipeline ingests this data and tries to determine whether the object corresponding with the identifier represents software; currently this means that metadata is harvested for a DOI and it is checked whether the resource type is "software". If the pipeline determines that the DOI found corresponds with a software object, it constructs a payload that will be sent to the ADS webhook service, which will then send the following JSON data to all callback URLs that subscribed to the event `relation_created`:
```
{
  "id": "d969a56d-e520-405d-a24f-497ac6923781",
  "description": "ADS citation events",
  "creator": "ADS",
  "source": "ADS.Discovery",
  "time": 1441166640.359496,
  "event": "relation_created",
  "payload": {
             "relationship_type": {
                 "original_relationship_schema": "DataCite",
                 "original_relationship_name": "cites",
                 "scholix_relationship": "references"
             },
             "target": {
                 “identifier”: {
                     "id": "10.5281/zenodo.11020",
                     "id_schema": "DOI",
                     “id_url”: “https://doi.org”
                 },
	    	         “type”:  {
		                 “name”: “software”
                 },
             },
             "source": {
                 “identifier”:{
                     "id": "2016ApJ...818..156C",
                     "id_schema": "bibcode",
                     “id_url”: “http://adsabs.harvard.edu/abs/”
                 },
             },
             "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
  },
}
```

## Event: The Zenodo (software) record is added to the ADS index

The metadata harvested for the Zenodo (software) record in the ADS back-office pipeline is submitted to the indexing process. As a result, a bibcode is minted for this Zenodo record. The pipeline (which is different from the one above) prepares a payload and submits this to the webhook service, which then sends out the following `relation_created`to all callback URLs that subscribed to this event type:
```
{
  "id": "d969a56d-e520-405d-a24f-497ac6923781",
  "description": "ADS citation events",
  "creator": "ADS",
  "source": "ADS.Discovery",
  "time": 1441166640.359496,
  "event": "relation_created",
  "payload": {
             "relationship_type": {
                 "original_relationship_schema": "DataCite",
                 "original_relationship_name": "IsIdenticalTo"
                     },
             "target": {
                 “Identifier”: {
                     "id": "10.5281/zenodo.11020",
                     "id_schema": "DOI",
                     “id_url”: “https://doi.org”
                 },
		             “type”: {
		                “name”: “software”
                 },
             },
             "source": {
                 “identifier”:{
                     "id": "2016zen.soft123456X",
                     "id_schema": "bibcode",
                     “id_url”: “http://adsabs.harvard.edu/abs/”
                 }
             },
             "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
   },
}
```

## Event: ADS discovers that a journal article cites a Zenodo (software) record (already in the ADS database)

This will result in the emission of a `relation_added` event just like the one earlier. Since an `IsIdenticalTo` event has been transmitted, equating the Zenodo DOI with the ADS bibcode for that record, the broker will recognize this equivalency.

![Image of ADS events](https://github.com/asclepias/event-model/blob/master/ADS_events.png)

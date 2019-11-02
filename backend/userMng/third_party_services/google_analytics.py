import logging
import os, sys
import requests

from azure.keyvault import KeyVaultClient
from google.auth.transport.requests import *
from google.oauth2 import service_account
from googleapiclient.discovery import *
from myAzure.az_connect import AzureConnection

logger = logging.getLogger(__name__)


class Google_Analytics:
    """
    Google Analytics Reporting API V4.
    https://developers.google.com/analytics/devguides/reporting/core/dimsmets
    https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py
    """

    def getAzureSecret(self):
        azCon = AzureConnection()
        azCon.main()
        client = KeyVaultClient(azCon.credentials)
        GOOGLE_ANALYTICS = client.get_secret(
            "https://b40.vault.azure.net/",
            "GOOGLE-ANALYTICS-DROPBOX-LINK",
            "029892343cfa44c2a74a5a0968e6c18e",
        ).value
        return GOOGLE_ANALYTICS

    def download_file(self, dropbox_link):
        """
            Download google analytics file from dropbox. Link to it is stored in Azure KV
        """
        fl = os.path.abspath(os.path.join(os.path.dirname(__file__), "client_secrets.json"))
        r = requests.get(dropbox_link, allow_redirects=True)
        open(fl, "wb").write(r.content)

    def initialize_analyticsreporting(self):
        """
        Initializes an Analytics Reporting API V4 service object.

        Returns:
        An authorized Analytics Reporting API V4 service object.
        """
        SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]
        KEY_FILE_LOCATION = "client_secrets.json"

        try:
            fl = os.path.abspath(
                os.path.join(os.path.dirname(__file__), KEY_FILE_LOCATION)
            )
        except Exception:
            logger.exception("clients_secrets.json not found on the server")

        ga_credentials = service_account.Credentials.from_service_account_file(
            fl
        )
        scoped_credentials = ga_credentials.with_scopes(SCOPES)
        authed_session = AuthorizedSession(scoped_credentials)

        # Build the service object.
        analytics = build(
            "analyticsreporting",
            "v4",
            credentials=scoped_credentials,
            cache_discovery=False,
        )

        return analytics

    def get_report(self, analytics):
        """
        Queries the Analytics Reporting API V4.

        Args:
            analytics: An authorized Analytics Reporting API V4 service object.
        Returns:
            The Analytics Reporting API V4 response.

        """
        VIEW_ID = "181239651"
        return (
            analytics.reports()
            .batchGet(
                body={
                    "reportRequests": [
                        {
                            "viewId": VIEW_ID,
                            "dateRanges": [
                                {"startDate": "7daysAgo", "endDate": "today"}
                            ],
                            "metrics": [
                                {
                                    "expression": "ga:sessions",
                                    "expression": "ga:pageviews",
                                }
                            ],
                            "dimensions": [
                                {"name": "ga:country", "name": "ga:browser"}
                            ],
                        }
                    ]
                }
            )
            .execute()
        )

    def print_response(self, response):
        """
        Parses and prints the Analytics Reporting API V4 response.

        Args:
            response: An Analytics Reporting API V4 response.
        """
        google_analytics_dimensions_metrics_dict = dict()

        for report in response.get("reports", []):
            columnHeader = report.get("columnHeader", {})
            dimensionHeaders = columnHeader.get("dimensions", [])
            metricHeaders = columnHeader.get("metricHeader", {}).get(
                "metricHeaderEntries", []
            )

            for row in report.get("data", {}).get("rows", []):
                dimensions = row.get("dimensions", [])
                dateRangeValues = row.get("metrics", [])

                for header, dimension in zip(dimensionHeaders, dimensions):
                    print(header + ": " + dimension)

                for i, values in enumerate(dateRangeValues):
                    print("Date range: " + str(i))
                    for metricHeader, value in zip(metricHeaders, values.get("values")):
                        # Add dict here: key value
                        google_analytics_dimensions_metrics_dict[
                            metricHeader.get("name")
                        ] = value
                        print(metricHeader.get("name") + ": " + value)

        return google_analytics_dimensions_metrics_dict

    # def main(self):
    #     keyAzure = GetAzureSecret()
    #     download_file(keyAzure)
    #     analytics = initialize_analyticsreporting()
    #     response = get_report(analytics)
    #     print_response(response)

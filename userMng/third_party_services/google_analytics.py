from googleapiclient.discovery import *
from oauth2client.service_account import *

class Google_Analytics:
	"""
	Google Analytics Reporting API V4.
	https://developers.google.com/analytics/devguides/reporting/core/dimsmets
	https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py
	"""

	
	def initialize_analyticsreporting(self):
		"""
		Initializes an Analytics Reporting API V4 service object.
	
		Returns:
		An authorized Analytics Reporting API V4 service object.
		"""
		SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
		KEY_FILE_LOCATION = 'client_secrets.json'
		credentials = ServiceAccountCredentials.from_json_keyfile_name(self.KEY_FILE_LOCATION, self.SCOPES)
	
		# Build the service object.
		analytics = build('analyticsreporting', 'v4', credentials=credentials)
	
		return analytics
		
		
	def get_report(self, analytics):
		"""
		Queries the Analytics Reporting API V4.
	
		Args:
			analytics: An authorized Analytics Reporting API V4 service object.
		Returns:
			The Analytics Reporting API V4 response.
			
		"""
		VIEW_ID = '181239651'
		return analytics.reports().batchGet(
				body={
					'reportRequests': [
					{
						'viewId': self.VIEW_ID,
						'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
						'metrics': [{'expression': 'ga:sessions', "expression":"ga:pageviews"}],
						'dimensions': [{'name': 'ga:country', "name":"ga:browser"}]
					}]
				}
		).execute()
	
	
	def print_response(self, response):
		"""
		Parses and prints the Analytics Reporting API V4 response.
	
		Args:
			response: An Analytics Reporting API V4 response.
		"""
		google_analytics_dimensions_metrics_dict = dict()
		
		for report in response.get('reports', []):
			columnHeader = report.get('columnHeader', {})
			dimensionHeaders = columnHeader.get('dimensions', [])
			metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
	
			for row in report.get('data', {}).get('rows', []):
				dimensions = row.get('dimensions', [])
				dateRangeValues = row.get('metrics', [])
	
				for header, dimension in zip(dimensionHeaders, dimensions):
					print(header + ': ' + dimension)
	
				for i, values in enumerate(dateRangeValues):
					print('Date range: ' + str(i))
					for metricHeader, value in zip(metricHeaders, values.get('values')):
						# Add dict here: key value
						google_analytics_dimensions_metrics_dict[metricHeader.get('name')] = value
						print(metricHeader.get('name') + ': ' + value)
						
		print(google_analytics_dimensions_metrics_dict)
		return google_analytics_dimensions_metrics_dict
	
	def main(self):
		analytics = initialize_analyticsreporting()
		response = get_report(analytics)
		print_response(response)
	
# if __name__ == '__main__':
# 	gh = Google_Analytics()
# 	analytics = gh.initialize_analyticsreporting()
# 	response = gh.get_report(analytics)
# 	gh.print_response(response)



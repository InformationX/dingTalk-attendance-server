'''
Created by auto_sdk on 2019.07.01
'''
from dingtalk.api.base import RestApi
class OapiReportReceiverListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.offset = None
		self.report_id = None
		self.size = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.report.receiver.list'

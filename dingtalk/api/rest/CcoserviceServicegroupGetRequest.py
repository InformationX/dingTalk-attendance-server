'''
Created by auto_sdk on 2019.07.03
'''
from dingtalk.api.base import RestApi
class CcoserviceServicegroupGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.open_group_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.ccoservice.servicegroup.get'

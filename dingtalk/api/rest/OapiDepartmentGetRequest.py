'''
Created by auto_sdk on 2018.08.17
'''
from dingtalk.api.base import RestApi
class OapiDepartmentGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.id = None
		self.lang = None

	def getHttpMethod(self):
		return 'GET'

	def getapiname(self):
		return 'dingtalk.oapi.department.get'

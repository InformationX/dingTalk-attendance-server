'''
Created by auto_sdk on 2019.09.16
'''
from dingtalk.api.base import RestApi
class OapiWorkspaceProjectCreateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.belong_corp_userid = None
		self.desc = None
		self.name = None
		self.open_conversation_id = None
		self.type = None
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.workspace.project.create'

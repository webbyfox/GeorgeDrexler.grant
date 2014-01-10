from georgedrexler.grant.interfaces import ITitleForApplication
from zope.interface import implements

class TitleForApplication(object):
	implements(ITitleForApplication)

	def __init__(self, context):
		self.context = context
		
	@property
	def title(self):
		return u"%s %s" % (self.context.first_name, self.context.surname)
	
	def setTitle(self, value):
		return
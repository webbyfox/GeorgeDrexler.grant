from plone.app.content.interfaces import INameFromTitle

class ITitleForApplication(INameFromTitle):

    def title():
	"""Return a custom title"""
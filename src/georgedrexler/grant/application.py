from georgedrexler.grant import MessageFactory as _
from five import grok

from plone.directives.form import default_value
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from z3c.form.interfaces import IEditForm, IAddForm

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope import schema
from zope.schema import Date	
from zope.security import checkPermission
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation
from plone.directives.form import default_value

from plone.app.content.interfaces import INameFromTitle
from rwproperty import getproperty, setproperty
from zope.interface import implements, Interface
from zope.component import adapts

import z3c.form 
from z3c.form import field, button

from DateTime import DateTime

YNList = SimpleVocabulary(
	[
	SimpleTerm(value=None, title=_(u'')),
	SimpleTerm(value=u'Yes', title=_(u'Yes')),
	SimpleTerm(value=u'No', title=_(u'No')),
	]
)


class IApplication(form.Schema):
	"""
	Interface class for application schema
	"""
	
	first_name = schema.TextLine(
		title =_(u"First name"), 
		default=u""
		)
	
	surname = schema.TextLine(
		title =_(u"Surname"), 
		default=u""
		)
	
	
	dob = schema.Date(
		title=_(u"Date of birth"),
		)
    
	citizen = schema.Choice(
		title=_(u"Are you a UK citizen?"),
		vocabulary = YNList,
		)
		
	address = schema.Text(
		title=_(u"Address:"),
		)
		
	telephone = schema.Int(
		title=_(u"Telephone number")
		)
		
	email = schema.TextLine(
		title=_(u"Email address"),
		)
	
	education = schema.Text(
		title = _(u"Education History (including qualifications)"),
		)
	
	course = schema.TextLine(
		title = _(u"Course title")
	)
	
	institution = schema.TextLine(
		title = _(u"Institution")
	)
	
	commencement = schema.TextLine(
		title = _(u"Date of commencement")
	)
	
	value_sought = schema.TextLine(
		title = _(u"Value of funding sought (\u00A31,000 to \u00A310,000)"),
		)
	
	commercial = schema.Choice(
		title = _(u"Commercial link (see guidance notes)"),
		vocabulary = YNList,
		)
		
	previous_grant = schema.Choice(
		title = _(u"Have you received a grant from us before?"),
		vocabulary = YNList,
		)
		
	received_grant_before = schema.Text(
		title =_(u"If yes, give details. (Years received and amounts awarded)"),
		required = False,
		)
		
	detail_additional_app = schema.Text(
		title = _(u"Details of all additional applications pending and awarded"),
		required = False,
		)
	
	statement_text = schema.Text(
		title = _(u"Personal statement"),
		required = False,
		)
	
	statement_file = NamedBlobFile(
        title = _(u"Personal statement"),
        description = _(u"No more than two sides of A4 paper"),
        required = False,
		)	
		
	reference = NamedBlobFile(
        title = _(u"Reference"),
        description = _(u"No more than two sides of A4 paper"),
        required = False,
		)	
		

	
class Application_View(grok.View):
    grok.context(IApplication)
    grok.require('zope2.View')
    grok.name('view')
	enable_form_tabbing = False
       
    def canEdit(self):
        if self.context.portal_workflow.getInfoFor(self.context,'review_state') == 'private':
           return True
        return False
	
    def canSubmit(self):
        if self.context.portal_workflow.getInfoFor(self.context,'review_state') == 'private':
           return True
        return False
	

@form.default_value(field = IExcludeFromNavigation['exclude_from_nav'])
def excludeFromNavDefaultValue(data):
    return True
	
class IApplicationTitle(INameFromTitle):
    def title():
        """Return a processed title"""	
		
class ApplicationTitle(object):
   implements(IApplicationTitle)

   def __init__(self, context):
       self.context = context
   
   @property
   def title(self):
       return '%s-%s' % (self.context.surname, self.context.first_name)
	
	
	
	
	
	
	
	
	
	
	
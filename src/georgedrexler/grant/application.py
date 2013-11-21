from georgedrexler.grant import MessageFactory as _
from five import grok

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope import schema
from zope.schema import Date

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
		title =_(u"First Name"), 
		default=u""
		)
	
	surname = schema.TextLine(
		title =_(u"Surname"), 
		default=u""
		)
	
	
	dob = schema.Date(
		title=_(u"Date of Birth"),
		)
    
	citizen = schema.Choice(
		title=_(u"Are you a UK citizen?"),
		vocabulary = YNList,
		)
		
	address = schema.Text(
		title=_(u"Address:"),
		)
		
	telephone = schema.Int(
		title=_(u"Telephone Number")
		)
		
	email = schema.TextLine(
		title=_(u"Email Address"),
		)
	
	education = schema.Text(
		title = _(u"Education History (including Qualifications)"),
		)
	
	course = schema.TextLine(
		title = _(u"Course Title")
	)
	
	institution = schema.TextLine(
		title = _(u"Institution")
	)
	
	commencement = schema.Date(
		title = _(u"Date of commencement")
	)
	
	value_sought = schema.TextLine(
		title = _(u"Value of Funding Sought (maximum \u00A310,000)"),
		)
	
	commercial = schema.Choice(
		title = _(u"Commercial Link (see guidence notes)"),
		vocabulary = YNList,
		)
		
	previous_grant = schema.Choice(
		title = _(u"Have you received a grant from us before?"),
		vocabulary = YNList,
		)
		
	received_grant_before = schema.Text(
		title =_(u"If yes, give details. (Years received and amounts awarded"),
		required = False,
		)
		
	detail_additional_app = schema.Text(
		title = _(u"Details of all additional applications pending and awarded"),
		required = False,
		)
	
	statement_text = schema.Text(
		title = _(u"Personal Satetment"),
		required = False,
		)
	
	statement_file = NamedBlobFile(
        title = _(u"Personal Statement"),
        description = _(u"No more than two sides of A4 paper"),
        required = False,
		)	
		
	reference = NamedBlobFile(
        title = _(u"Reference"),
        description = _(u"No more than two sides of A4 paper"),
        required = False,
		)	
		
	#@button.buttonAndHandler(_(u'Submit'))
	#def handleSubmission(self, action):
	
#			self.status = _(u"Application Submitted")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
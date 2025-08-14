# -*- coding: utf-8 -*-
from udala.aktak.views.vocabutils import vocab_term_title

# from plone.app.textfield import RichText
# from plone.autoform import directives
from udala.aktak import _
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


class IBilkura(model.Schema):
    """Marker interface and Dexterity Python Schema for Bilkura"""

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('bilkura.xml')

    data = schema.Datetime(
        title=_("Data"),
        required=True,
    )

    mota = schema.Choice(
        title=_("Mota"),
        vocabulary="udala.aktak.BilkuraMotak",
        required=True,
    )

    gaizerrenda = NamedBlobFile(title="Gai zerrendaren fitxategia", required=False)

    akta = NamedBlobFile(title=_("Aktaren fitxategia"), required=False)

    eranskinak = NamedBlobFile(title=_("Eranskinak"), required=False)

    bideoa = schema.TextLine(
        title=_("Bideoaren helbidea"),
        required=False,
    )

    bideoakta = schema.TextLine(
        title=_("Bideo-aktaren helbidea"),
        required=False,
    )


@implementer(IBilkura)
class Bilkura(Container):
    """Content-type class for IBilkura"""

    def get_mota_title(self):
        return vocab_term_title(
            self,
            "udala.aktak.BilkuraMotak",
            self.mota,
        )

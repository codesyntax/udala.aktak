from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from udala.aktak import _
from udala.aktak.views.vocabutils import vocab_term_title
from zope import schema
from zope.interface import implementer


class IBilkura(model.Schema):
    """Marker interface and Dexterity Python Schema for Bilkura"""

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('bilkura.xml')

    data = schema.Datetime(
        title=_("Date"),
        required=True,
    )

    mota = schema.Choice(
        title=_("Type"),
        vocabulary="udala.aktak.SessionTypes",
        required=True,
    )

    gaizerrenda = NamedBlobFile(
        title="File with the agenda of the meeting", required=False
    )

    akta = NamedBlobFile(title=_("File with the meeting minutes"), required=False)

    eranskinak = NamedBlobFile(
        title=_("File with the annexes to the meeting minutes"), required=False
    )

    bideoa = schema.TextLine(
        title=_("URL of the video"),
        required=False,
    )

    bideoakta = schema.TextLine(
        title=_("URL of the meeting minutes video"),
        required=False,
    )


@implementer(IBilkura)
class Bilkura(Container):
    """Content-type class for IBilkura"""

    def get_session_title(self):
        return vocab_term_title(
            self,
            "udala.aktak.SessionTypes",
            self.mota,
        )

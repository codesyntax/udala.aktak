from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from udala.aktak import _
from udala.aktak.views.vocabutils import vocab_term_title
from zope import schema
from zope.interface import implementer


class IMeeting(model.Schema):
    """Marker interface and Dexterity Python Schema for Meeting"""

    meeting_date = schema.Datetime(
        title=_("Date"),
        required=True,
    )

    meeting_type = schema.Choice(
        title=_("Type"),
        vocabulary="udala.aktak.MeetingTypes",
        required=True,
    )

    meeting_agenda = NamedBlobFile(
        title="File with the agenda of the meeting", required=False
    )

    meeting_minutes = NamedBlobFile(
        title=_("File with the meeting minutes"), required=False
    )

    meeting_minutes_annexes = NamedBlobFile(
        title=_("File with the annexes to the meeting minutes"), required=False
    )

    video_url = schema.TextLine(
        title=_("URL of the video"),
        required=False,
    )

    video_minutes_url = schema.TextLine(
        title=_("URL of the meeting minutes video"),
        required=False,
    )


@implementer(IMeeting)
class Meeting(Container):
    """Content-type class for IMeeting"""

    def get_meeting_type_title(self):
        return vocab_term_title(
            self,
            "udala.aktak.MeetingTypes",
            self.meeting_type,
        )

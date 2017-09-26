"""A simple XBlock for signposting student activities"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

class signpostXBlock(StudioEditableXBlockMixin, XBlock):
    display_name = String(display_name="Display name", default='signpost', scope=Scope.settings)
    signposticon = String(display_name="Icon", default="book", scope=Scope.content,
        help="Pick the icon to appear alongside your signpost. Any icon from <a href=\"http://fontawesome.io/icons/\">Font Awesome</a> may be used. Simply use the icon name as listed, for example: eye, comments, book.")
    signposttext = String(display_name="Contents", multiline_editor='html', resettable_editor=False,
        default="", scope=Scope.content,
        help="Enter the text to be displayed within your signpost, instructing students on what to do.")
    signpostheading = String(display_name="Heading", default="", scope=Scope.content, help="Examples- Discussion: Introduce yourself, Activity 2: Researching the Truth")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the signpostXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/signpost.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/signpost.css"))
        frag.add_javascript(self.resource_string("static/js/src/signpost.js"))
        frag.initialize_js('signpostXBlock')
        return frag
    # Make fields editable in studio
    editable_fields = ('display_name', 'signpostheading', 'signposticon', 'signposttext', )

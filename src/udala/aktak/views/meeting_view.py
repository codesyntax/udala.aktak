from Products.Five.browser import BrowserView


class MeetingView(BrowserView):
    def __call__(self):
        # Implement your own actions:
        return self.index()

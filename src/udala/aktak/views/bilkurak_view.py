# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from plone.memoize.view import memoize
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface
from plone import api


class IBilkurakView(Interface):
    """Marker Interface for IBilkurakView"""


@implementer(IBilkurakView)
class BilkurakView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('bilkurak_filter_view.pt')

    @memoize
    def folders(self):
        context = aq_inner(self.context)
        folders = api.content.find(
            context=context,
            portal_type="Folder",
            sort_on="sortable_title",
            sort_order="reverse",
            depth=1,
        )

        return_folders = []
        if folders:
            for folder in folders:
                folder_dict = {"id": folder.id, "title": folder.Title}
                obj = folder.getObject()
                bilkurak = api.content.find(
                    context=obj,
                    portal_type="Bilkura",
                    sort_on="meeting_date",
                    sort_order="reverse",
                    depth=1,
                )
                if bilkurak:
                    bilkurak_list = []
                    for bilkura in bilkurak:
                        obj = bilkura.getObject()
                        bilkura_dict = {"title": obj.Title()}
                        bilkura_dict["data"] = self.context.toLocalizedTime(obj.data)
                        bilkura_dict["bideoa"] = obj.bideoa
                        bilkura_dict["bideoakta"] = obj.bideoakta
                        bilkura_dict["mota"] = obj.get_mota_title()
                        bilkura_dict["gaizerrenda"] = (
                            obj.gaizerrenda
                            and f"{obj.absolute_url()}/@@download/gaizerrenda"
                        ) or ""
                        bilkura_dict["akta"] = (
                            obj.akta and f"{obj.absolute_url()}/@@download/akta" or ""
                        )

                        bilkura_dict["eranskinak"] = (
                            obj.eranskinak
                            and f"{obj.absolute_url()}/@@download/eranskinak"
                            or ""
                        )

                        bilkurak_list.append(bilkura_dict)
                    folder_dict["bilkurak"] = bilkurak_list
                    return_folders.append(folder_dict)
                else:
                    folder_dict["bilkurak"] = []
        return return_folders

    def bilkurak_items(self):
        context = aq_inner(self.context)
        bilkurak = api.content.find(
            context=context,
            portal_type="Bilkura",
            sort_on="meeting_date",
            sort_order="reverse",
            depth=1,
        )
        bilkurak_list = []
        for bilkura in bilkurak:
            obj = bilkura.getObject()
            bilkura_dict = {"title": obj.Title()}
            bilkura_dict["data"] = self.context.toLocalizedTime(obj.data)
            bilkura_dict["bideoa"] = obj.bideoa
            bilkura_dict["bideoakta"] = obj.bideoakta
            bilkura_dict["mota"] = obj.get_mota_title()
            bilkura_dict["gaizerrenda"] = (
                obj.gaizerrenda and f"{obj.absolute_url()}/@@download/gaizerrenda" or ""
            )
            bilkura_dict["akta"] = (
                obj.akta and f"{obj.absolute_url()}/@@download/akta" or ""
            )
            bilkura_dict["eranskinak"] = (
                obj.eranskinak and f"{obj.absolute_url()}/@@download/eranskinak" or ""
            )
            bilkurak_list.append(bilkura_dict)
        return bilkurak_list

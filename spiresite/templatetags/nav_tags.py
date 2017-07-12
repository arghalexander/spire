from datetime import date
from django import template
from django.conf import settings

from wagtail.wagtailcore.models import Site
from wagtail.wagtailcore.query import PageQuerySet
from itertools import chain
from spiresite.models import HomePage

register = template.Library()



@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('spiresite/tags/top_menu.html', takes_context=True)
def top_menu(context, calling_page=None):

    root= context['request'].site.root_page
    menuitems = root.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }



@register.inclusion_tag('spiresite/tags/srec_menu.html', takes_context=True)
def srec_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live()


    for menuitem in menuitems:
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }



@register.inclusion_tag('spiresite/tags/sub_page_nav.html', takes_context=True)
def sub_page_nav(context, parent, calling_page=None, overview_name="Overview"):
    menuitems = parent.get_children().live().not_in_menu()

    for menuitem in menuitems:
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)


    parent.active = (calling_page.url == parent.url if calling_page else False)
    parent.title = overview_name

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'parent': parent,
        'request': context['request'],
    }


@register.inclusion_tag('spiresite/tags/leadership_menu.html', takes_context=True)
def leadership_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('spiresite/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('spiresite/tags/top_menu_children_mobile.html', takes_context=True)
def top_menu_children_mobile(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }





@register.inclusion_tag('spiresite/tags/footer.html', takes_context=True)
def footer_menu(context):
    pass

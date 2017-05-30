from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks

class MenuItemBlock(blocks.StreamBlock):
    title = blocks.CharBlock(classname="full title")
    links = blocks.ListBlock(blocks.StructBlock([
        ('internal', blocks.PageChooserBlock(required=False)),
        ('exernal', blocks.URLBlock(required=False)),
    ]))
   
    class Meta:
        icon='cogs'
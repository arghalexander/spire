from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class MenuItemBlock(blocks.StreamBlock):
	title = blocks.CharBlock(classname="full title")
	links = blocks.ListBlock(blocks.StructBlock([
		('internal', blocks.PageChooserBlock(required=False)),
		('exernal', blocks.URLBlock(required=False)),
	]))
   
	class Meta:
		icon='cogs'




class ImageTextBlock(blocks.StreamBlock):
	image = ImageChooserBlock()
	text = blocks.RichTextBlock()
   
	class Meta:
		icon='doc-full-inverse'


class ButtonBlock(blocks.StructBlock):
	link = blocks.URLBlock()
	label = blocks.CharBlock()

	class Meta:
		template = 'spiresite/blocks/button.html'
		icon = 'link'


class LeaderBlock(blocks.StructBlock):
	name = blocks.CharBlock(required=True)
	company = blocks.CharBlock(required=True)

	class Meta:
		template = 'spiresite/blocks/leader.html'
		icon = 'user'




class GalleryBlock(blocks.StructBlock):
	caption = blocks.CharBlock(required=True)
	images = blocks.ListBlock(blocks.StructBlock([		
		('image', ImageChooserBlock(null=True)),
	]))


	class Meta:
		template = 'spiresite/blocks/gallery.html'
		icon = 'image'


class TwoImageBlock(blocks.StructBlock):
	image_one = ImageChooserBlock(null=True)
	image_two = ImageChooserBlock(null=True)

	class Meta:
		template = 'spiresite/blocks/2_images.html'
		icon = 'image'


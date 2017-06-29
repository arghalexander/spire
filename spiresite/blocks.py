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



class PersonBlock(blocks.StructBlock):
	image = ImageChooserBlock(null=True)
	name =  blocks.CharBlock(required=False)
	title = blocks.CharBlock(required=False)
	description = blocks.RichTextBlock()
   
	class Meta:
		icon='user'



class PeopleListBlock(blocks.StreamBlock):
	person = blocks.ListBlock(PersonBlock())

	class Meta:
		template = 'spiresite/blocks/people_list.html'
		icon = 'group'



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




class ThreeColumnBlock(blocks.StructBlock):
	one = blocks.RichTextBlock()
	two = blocks.RichTextBlock()
	three = blocks.RichTextBlock()

	class Meta:
		template = 'spiresite/blocks/three_columns.html'
		icon = 'placeholder'



class TwoColumnBlock(blocks.StructBlock):
	one = blocks.RichTextBlock()
	two = blocks.RichTextBlock()

	class Meta:
		template = 'spiresite/blocks/two_columns.html'
		icon = 'placeholder'





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



class RedirectBlock(blocks.StructBlock):
	page = blocks.PageChooserBlock()

	class Meta:
		template = 'spiresite/blocks/redirect.html'
		icon = 'link'

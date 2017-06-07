# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('events', '0001_initial'),
        ('products', '0001_initial'),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('pillar_one', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('pillar_two', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('pillar_three', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('page_content', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ticket_quantity', models.IntegerField()),
                ('event', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_pricings', to='events.Event')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_level', to='members.MembershipLevel')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('sponsor_one', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('sponsor_one_link', models.URLField(blank=True)),
                ('sponsor_two', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('sponsor_two_link', models.URLField(blank=True)),
                ('sponsor_three', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('sponsor_three_link', models.URLField(blank=True)),
                ('join_content', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('join_link', models.URLField(blank=True)),
                ('contact_content', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('contact_link', models.URLField(blank=True)),
                ('featured_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_event', to='events.Event')),
                ('join_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='join_image', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('background', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_gallery_background', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeadershipOverviewPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='LeadershipRegionalLeadersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.wagtailcore.fields.StreamField([('region', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('leader', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'company', wagtail.wagtailcore.blocks.CharBlock(required=True))])))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='LeadershipStaffGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_gallery_image', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeadershipStaffPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MemberDirectoryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MembershipBenefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('icon_class', models.CharField(help_text=b'Icon CSS class', max_length=255)),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MembershipPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('full_membership', models.TextField(blank=True)),
                ('full_young_membership', models.TextField(blank=True)),
                ('full_friends_membership', models.TextField(blank=True)),
                ('guest_membership', models.TextField(blank=True)),
                ('student_membership', models.TextField(blank=True)),
                ('people_review_one', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('people_review_two', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('member_closing', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('full_friends_yearly', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_full_friends', to='products.MembershipProduct')),
                ('full_membership_5_years', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_full_5_years', to='products.MembershipProduct')),
                ('full_membership_yearly', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_full_year', to='products.MembershipProduct')),
                ('full_young_yearly', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_full_young', to='products.MembershipProduct')),
                ('guest_yearly', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_guest', to='products.MembershipProduct')),
                ('people_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='people_image', to='wagtailimages.Image')),
                ('student_yearly', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_student', to='products.MembershipProduct')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProfessionalsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SCRECPageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='srec_gallery_image', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(help_text=b'Your Facebook page URL')),
                ('instagram', models.CharField(help_text=b'Your Instagram username, without the @', max_length=255)),
                ('twitter', models.URLField(help_text=b'Your twitter page URL')),
                ('linkedin', models.URLField(help_text=b'Your Linkedin Profile URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SrecConferencePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.wagtailcore.fields.StreamField([('text_image', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'text', wagtail.wagtailcore.blocks.RichTextBlock())]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SrecMembersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('page_content', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('heading', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SRECPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('page_content', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('gallery_caption', models.CharField(blank=True, max_length=255)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='srec_event', to='events.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StandardLeadershipPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.wagtailcore.fields.StreamField([('text', wagtail.wagtailcore.blocks.RichTextBlock())])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.wagtailcore.fields.StreamField([('text', wagtail.wagtailcore.blocks.RichTextBlock())])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='screcpagegallery',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='srec_gallery', to='spiresite.SRECPage'),
        ),
        migrations.AddField(
            model_name='membershipbenefits',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_benefits', to='spiresite.MembershipPage'),
        ),
        migrations.AddField(
            model_name='leadershipstaffgallery',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='leadership_gallery', to='spiresite.LeadershipStaffPage'),
        ),
        migrations.AddField(
            model_name='homepagegallery',
            name='learn_more_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_gallery_learn_more', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='homepagegallery',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_gallery', to='spiresite.HomePage'),
        ),
    ]

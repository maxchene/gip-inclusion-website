# Generated by Django 4.1.5 on 2023-01-17 14:20

import django.core.validators
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contentpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "hero",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "bg_image",
                                    wagtail.images.blocks.ImageChooserBlock(label="Image d'arrière plan"),
                                ),
                                (
                                    "bg_color",
                                    wagtail.blocks.CharBlock(
                                        label="Couleur d'arrière plan au format hexa (Ex: #f5f5fe)",
                                        max_length=7,
                                        min_length=4,
                                        validators=[
                                            django.core.validators.RegexValidator(
                                                "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                                                "La couleur n'est pas correcte, le format doit être #fff ou #f5f5fe",
                                            )
                                        ],
                                    ),
                                ),
                                ("title", wagtail.blocks.CharBlock(label="Titre")),
                                (
                                    "cta_label",
                                    wagtail.blocks.CharBlock(label="Texte du bouton", required=False),
                                ),
                                (
                                    "cta_link",
                                    wagtail.blocks.URLBlock(label="Lien du bouton", required=False),
                                ),
                            ],
                            label="Section promotionnelle",
                        ),
                    ),
                    (
                        "title",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(label="Titre")),
                                (
                                    "large",
                                    wagtail.blocks.BooleanBlock(label="Large", required=False),
                                ),
                            ],
                            label="Titre de page",
                        ),
                    ),
                    (
                        "paragraph",
                        wagtail.blocks.RichTextBlock(label="Texte avec mise en forme"),
                    ),
                    (
                        "paragraphlarge",
                        wagtail.blocks.RichTextBlock(label="Texte avec mise en forme (large)"),
                    ),
                    (
                        "image",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(label="Titre", required=False),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(label="Illustration"),
                                ),
                                (
                                    "alt",
                                    wagtail.blocks.CharBlock(
                                        label="Texte alternatif (description textuelle de l'image)",
                                        required=False,
                                    ),
                                ),
                                (
                                    "caption",
                                    wagtail.blocks.CharBlock(label="Légende", required=False),
                                ),
                                (
                                    "url",
                                    wagtail.blocks.URLBlock(label="Lien", required=False),
                                ),
                            ]
                        ),
                    ),
                    (
                        "imageandtext",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(label="Illustration (à gauche)"),
                                ),
                                (
                                    "image_ratio",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("3", "3/12"),
                                            ("5", "5/12"),
                                            ("6", "6/12"),
                                        ],
                                        label="Largeur de l'image",
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(label="Texte avec mise en forme (à droite)"),
                                ),
                                (
                                    "link_label",
                                    wagtail.blocks.CharBlock(
                                        help_text="Le lien apparait en bas du bloc de droite, avec une flèche",
                                        label="Titre du lien",
                                        required=False,
                                    ),
                                ),
                                (
                                    "link_url",
                                    wagtail.blocks.URLBlock(label="Lien", required=False),
                                ),
                            ],
                            label="Bloc image à gauche et texte à droite",
                        ),
                    ),
                    (
                        "alert",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(label="Titre du message", required=False),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.TextBlock(label="Texte du message", required=False),
                                ),
                                (
                                    "level",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("error", "Erreur"),
                                            ("success", "Succès"),
                                            ("info", "Information"),
                                            ("warning", "Attention"),
                                        ],
                                        label="Type de message",
                                    ),
                                ),
                            ],
                            label="Message d'alerte",
                        ),
                    ),
                    (
                        "callout",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(label="Titre de la mise en vant", required=False),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.TextBlock(label="Texte mis en avant", required=False),
                                ),
                                (
                                    "color",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Bleu/Gris"),
                                            ("fr-callout--brown-caramel", "Marron"),
                                            ("fr-callout--green-emeraude", "Vert"),
                                        ],
                                        label="Couleur",
                                        required=False,
                                    ),
                                ),
                            ],
                            label="Texte mise en avant",
                        ),
                    ),
                    (
                        "quote",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Illustration (à gauche)", required=False
                                    ),
                                ),
                                ("quote", wagtail.blocks.CharBlock(label="Citation")),
                                (
                                    "author_name",
                                    wagtail.blocks.CharBlock(label="Nom de l'auteur"),
                                ),
                                (
                                    "author_title",
                                    wagtail.blocks.CharBlock(label="Titre de l'auteur"),
                                ),
                            ],
                            label="Citation",
                        ),
                    ),
                    (
                        "video",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(label="Titre", required=False),
                                ),
                                ("caption", wagtail.blocks.CharBlock(label="Légende")),
                                (
                                    "url",
                                    wagtail.blocks.URLBlock(
                                        help_text=(
                                            "URL au format 'embed' (Ex. : https://www.youtube.com/embed/gLzXOViPX-0)"
                                        ),
                                        label="Lien de la vidéo",
                                    ),
                                ),
                            ],
                            label="Vidéo",
                        ),
                    ),
                    (
                        "multicolumns",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(label="Texte avec mise en forme"),
                                ),
                                (
                                    "image",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(label="Titre", required=False),
                                            ),
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(label="Illustration"),
                                            ),
                                            (
                                                "alt",
                                                wagtail.blocks.CharBlock(
                                                    label="Texte alternatif (description textuelle de l'image)",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "caption",
                                                wagtail.blocks.CharBlock(label="Légende", required=False),
                                            ),
                                            (
                                                "url",
                                                wagtail.blocks.URLBlock(label="Lien", required=False),
                                            ),
                                        ],
                                        label="Image",
                                    ),
                                ),
                                (
                                    "video",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(label="Titre", required=False),
                                            ),
                                            (
                                                "caption",
                                                wagtail.blocks.CharBlock(label="Légende"),
                                            ),
                                            (
                                                "url",
                                                wagtail.blocks.URLBlock(
                                                    help_text=(
                                                        "URL au format 'embed' "
                                                        "(Ex. : https://www.youtube.com/embed/gLzXOViPX-0)"
                                                    ),
                                                    label="Lien de la vidéo",
                                                ),
                                            ),
                                        ],
                                        label="Vidéo",
                                    ),
                                ),
                                (
                                    "card",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(label="Titre"),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.TextBlock(label="Texte"),
                                            ),
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(label="Image"),
                                            ),
                                            (
                                                "url",
                                                wagtail.blocks.URLBlock(label="Lien", required=False),
                                            ),
                                            (
                                                "document",
                                                wagtail.documents.blocks.DocumentChooserBlock(
                                                    help_text=(
                                                        "Sélectionnez un document pour rendre la carte cliquable "
                                                        "vers celui ci (si le champ `Lien` n'est pas renseigné)."
                                                    ),
                                                    label="ou Document",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "badge_text",
                                                wagtail.blocks.CharBlock(
                                                    label="Texte du badge",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "badge_level",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("error", "Erreur"),
                                                        ("success", "Succès"),
                                                        ("info", "Information"),
                                                        ("warning", "Attention"),
                                                        ("new", "Nouveau"),
                                                        ("grey", "Gris"),
                                                        ("green-emeraude", "Vert"),
                                                        ("blue-ecume", "Bleu"),
                                                    ],
                                                    label="Type de badge",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "badge_icon",
                                                wagtail.blocks.BooleanBlock(
                                                    label="Masquer l'icon du badge",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        label="Carte",
                                    ),
                                ),
                                (
                                    "quote",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    label="Illustration (à gauche)",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "quote",
                                                wagtail.blocks.CharBlock(label="Citation"),
                                            ),
                                            (
                                                "author_name",
                                                wagtail.blocks.CharBlock(label="Nom de l'auteur"),
                                            ),
                                            (
                                                "author_title",
                                                wagtail.blocks.CharBlock(label="Titre de l'auteur"),
                                            ),
                                        ],
                                        label="Citation",
                                    ),
                                ),
                            ],
                            label="Multi-colonnes",
                        ),
                    ),
                    (
                        "faq",
                        wagtail.blocks.StreamBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(label="Titre")),
                                (
                                    "question",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "question",
                                                wagtail.blocks.CharBlock(label="Question"),
                                            ),
                                            (
                                                "answer",
                                                wagtail.blocks.RichTextBlock(label="Réponse"),
                                            ),
                                        ],
                                        label="Question",
                                        max_num=15,
                                        min_num=1,
                                    ),
                                ),
                            ],
                            label="Questions fréquentes",
                        ),
                    ),
                    (
                        "stepper",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(label="Titre")),
                                (
                                    "total",
                                    wagtail.blocks.IntegerBlock(label="Nombre d'étape"),
                                ),
                                (
                                    "current",
                                    wagtail.blocks.IntegerBlock(label="Étape en cours"),
                                ),
                                (
                                    "steps",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "step",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(label="Titre de l'étape"),
                                                        ),
                                                        (
                                                            "detail",
                                                            wagtail.blocks.TextBlock(label="Détail"),
                                                        ),
                                                    ],
                                                    label="Étape",
                                                ),
                                            )
                                        ],
                                        label="Les étapes",
                                    ),
                                ),
                            ],
                            label="Étapes",
                        ),
                    ),
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
    ]

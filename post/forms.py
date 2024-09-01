from django import forms

from .models import Post
from .models import Tag
from image.models import Image


class PostCreateForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "1",
                "placeholder": "business, finance, health ...",
            }
        ),
    )
    image_id = forms.IntegerField(
        required=False, widget=forms.HiddenInput(attrs={"id": "imageId"})
    )

    class Meta:
        model = Post
        fields = ["title", "description", "content", "status", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "required": True,
                    "id": "con-name",
                    "name": "name",
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Post title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "required": True,
                    "class": "form-control",
                    "rows": "3",
                    "placeholder": "Add description",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "d-none",
                    "rows": "10",
                    "placeholder": "Add content",
                    "id": "quill-content",
                }
            ),
            "category": forms.Select(
                attrs={"class": "form-select", "aria-label": "Default select example"}
            ),
            "status": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "type": "checkbox",
                    "id": "postCHeck",
                }
            ),
        }

    def clean_tags(self):
        tags_string = self.cleaned_data.get("tags", "")
        tags = [tag.strip() for tag in tags_string.split(",") if tag.strip()]
        if len(tags) > 14:
            raise forms.ValidationError("최대 14개의 태그만 입력할 수 있습니다.")
        return tags

    def save(self, commit=True):
        post = super().save(commit=False)

        image_id = self.cleaned_data.get("image_id")
        if image_id:
            image = Image.objects.get(id=image_id)
            if image.user != post.author:
                raise forms.ValidationError("Invalid Image")
            post.image = image
        else:
            post.image = None

        post.save()
        tags_names = self.cleaned_data.get("tags", [])
        tags = []
        for tag_name in tags_names:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
        if tags:
            post.tags.set(tags)
        return post

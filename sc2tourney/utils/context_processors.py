from django.conf import settings

from django.contrib.sites.models import Site


def template_settings(request):
    ctx = {}
    extra_ctx = getattr(settings, 'ADD_TO_CONTEXT', {})

    if Site._meta.installed:
        site = Site.objects.get_current()
        ctx.update({
            "SITE_NAME": site.name,
            "SITE_DOMAIN": site.domain
        })

    ctx.update(extra_ctx)

    return ctx

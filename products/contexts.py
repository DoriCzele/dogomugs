from products.models import Category


def categories_context(request):
    """Provide categories in a context.

    Handling of no existing categories is not required here as nav dropdown expected to
    be empty in that scenario.
    """
    categories = Category.objects.all()

    return {"categories": categories}

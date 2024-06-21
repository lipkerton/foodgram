from django_filters import rest_framework

from recipes.models import Favorite, Recipe, ShoppingCart, Ingredient


class RecipeFilter(rest_framework.FilterSet):

    tags = rest_framework.AllValuesMultipleFilter(
        field_name='tags__slug'
    )
    is_in_shopping_cart = rest_framework.BooleanFilter(
        method='filter_is_in_shopping_cart'
    )
    is_favorited = rest_framework.BooleanFilter(
        method='filter_is_favorite'
    )

    def filter_is_in_shopping_cart(self, queryset, name, value):
        if (
            self.request.user.is_authenticated
            and value
        ):
            shop_cart = ShoppingCart.objects.filter(
                user=self.request.user,
            )
            return queryset.filter(id__in=shop_cart)
        if (
            self.request.user.is_authenticated
            and not value
        ):
            shop_cart = ShoppingCart.objects.filter(
                user=self.request.user,
            )
            return queryset.exclude(id_in=shop_cart)
        return queryset

    def filter_is_favorite(self, queryset, name, value):

        if (
            self.request.user.is_authenticated
            and value
        ):
            fav = Favorite.objects.filter(
                user=self.request.user
            )
            return queryset.filter(id__in=fav)
        if (
            self.request.user.is_authenticated
            and not value
        ):
            fav = Favorite.objects.filter(
                user=self.request.user
            )
            return queryset.exclude(id_in=fav)
        return queryset

    class Meta:
        model = Recipe
        fields = ('tags', 'author')


class IngredientFilter(rest_framework.FilterSet):

    name = rest_framework.CharFilter(
        lookup_expr='istartswith'
    )

    class Meta:
        model = Ingredient
        fields = ('name',)

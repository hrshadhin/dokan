from django.shortcuts import render
from django.db import transaction, connection
from django.db.models import Q, F, Func, Value, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg
from store.models import Product, Order, Customer, Collection, OrderItem
from tags.models import TaggedItem


def play(request):
    products = Product.objects.filter(collection__id__range=(1, 5)).all()[:10]
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__gt=200))
    # query_set = Product.objects.filter(inventory=F('collection__id'))
    # query_set = Product.objects.filter(title__icontains='Fo').values('id', 'title', 'unit_price', 'collection__title')
    # query_set = Product.objects.select_related('collection').all()
    # query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # query_set = query_set.order_by('-unit_price')

    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set').all()
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').all()
    # result = list(query_set[0:25])
    # result = Product.objects.aggregate(count=Count('slug'),
    #                                    min_price=Min('unit_price'),
    #                                    max_price=Max('unit_price'),
    #                                    avg_price=Avg('unit_price')
    #                                    )
    # result = Product.objects.filter(collection_id=5).aggregate(count=Count('slug'),
    #                                                            min_price=Min('unit_price'),
    #                                                            max_price=Max('unit_price'),
    #                                                            avg_price=Avg('unit_price')
    #                                                            )

    # query_set = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    # query_set = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )
    # res = list(query_set)
    # query_set = Customer.objects.annotate(
    #     orders=Count('order')
    # ).order_by('-orders')
    # res = list(query_set)
    #
    # discount_exp = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # query_set = Product.objects.annotate(
    #     discounted_price=discount_exp
    # )
    # rest = list(query_set)

    # query_set = TaggedItem.objects.get_tags_for(Product, 1)
    # list(query_set)

    # Collection.objects.create(title='Foobar')
    # collection = Collection.objects.filter(pk=1).update(featured_product_id=1)

    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()
    #
    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 3
    #     item.unit_price = 50.50
    #     item.save()

    # with connection.cursor() as cursor:
    #     cursor.execute('select * from products')
    #     cursor.callproc('get_customer', [1, 3, 'q'])

    return render(request, 'play.html', {
        'products': products,
        'result': None
    })

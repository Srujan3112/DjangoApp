from django.test import TestCase
from Base.models import Product, Categorie
from Cart.models import CartItem, Cart, Order
from django.contrib.auth.models import User
from model_bakery import baker
from pprint import pprint


class TestCategory(TestCase):
    def test_category_title(self):
        title = Categorie.objects.create(title="Django Testing")
        self.assertEqual(str(title), "Django Testing")


class TestProduct(TestCase):
    def setUp(self):
        self.product = baker.make('Base.Product')
        pprint(self.product.__dict__)

    def test_product_title(self):
        title = Product.objects.create(title="Django Testing")
        self.assertEqual(str(title), "Django Testing")

    def test_product_category(self):
        category = Categorie.objects.create(title="Testing")
        product_category = Product.objects.create(category=category)
        self.assertEqual(category, product_category.category)

    def test_product_user(self):
        user = User.objects.create_user(username='Testing', password='Test@123')
        product_user = Product.objects.create(user=user)
        self.assertEqual(user, product_user.user)


class TestCartItem(TestCase):
    def setUp(self):
        self.cart_item = baker.make('Cart.CartItem')
        pprint(self.cart_item.__dict__)

    def test_cart_item_user(self):
        user = User.objects.create_user(username='Testing', password='Test@123')
        cart_item_user = CartItem.objects.create(user=user)
        self.assertEqual(cart_item_user.user, user)

    def test_cart_item_product(self):
        product = Product.objects.create(title="Test Product")
        cart_item_product = CartItem.objects.create(product=product)
        self.assertEqual(cart_item_product.product, product)

    def test_cart_item_cart(self):
        user = User.objects.create_user(username='Testing', password='Test@123')
        cart = Cart.objects.create(user=user)
        cart_item_cart = CartItem.objects.create(cart=cart)
        self.assertEqual(cart_item_cart.cart, cart)


class TestCart(TestCase):
    def setUp(self):
        self.cart = baker.make('Cart.Cart')
        pprint(self.cart.__dict__)

    def test_cart_user(self):
        user = User.objects.create_user(username='Testing', password='Test@123')
        cart = Cart.objects.create(user=user)
        self.assertEqual(cart.user, user)


class TestOrder(TestCase):
    def setUp(self):
        self.order = baker.make('Cart.Order')
        pprint(self.order.__dict__)

    def test_order_user(self):
        user = User.objects.create_user(username='Testing', password='Test@123')
        order = Order.objects.create(user=user)
        self.assertEqual(order.user, user)

    def test_order_product(self):
        product = Product.objects.create(title="Testing")
        order = Order.objects.create(order_item=product)
        self.assertEqual(order.order_item, product)

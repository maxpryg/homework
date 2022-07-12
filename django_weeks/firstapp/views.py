from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from firstapp.models import Store
from firstapp.serializers import StoreSerializer

from datetime import date


@api_view()
def hello_world(request):
    return Response({'msg': 'Hello, world!'})


@api_view()
def today(request):
    full_date = date.today().strftime('%d/%m/%Y')
    year = date.today().year
    month = date.today().strftime('%m')
    day = date.today().strftime('%d')

    return Response({'date': full_date,
                     'year': year,
                     'month': month,
                     'day': day
                     })


@api_view()
def my_name(request):
    name_of_hacker = request.query_params.get('name_of_hacker')
    if not name_of_hacker:
        return Response(
            {'error': 'Wrong parameter. Need param <name_of_hacker>'})
    return Response({'name': name_of_hacker})


@api_view(['POST'])
def calculator(request):
    actions = {'plus': lambda x, y: x + y,
               'minus': lambda x, y: x - y,
               'multiply': lambda x, y: x * y,
               'divide': lambda x, y: x / y
               }

    action = request.data.get('action')
    number1 = request.data.get('number1')
    number2 = request.data.get('number2')

    if action not in actions.keys():
        return Response({'error':
                         f'Bad action value. Acceptable values are: '
                         f'{", ".join(key for key in actions.keys())}'})

    if action == 'divide' and number2 == 0:
        return Response({'error': 'Division by zero.'})

    result = actions[action](number1, number2)

    return Response({'result': result})


class StoreList(APIView):
    """List all stores, or create a new store"""
    def get(self, request, format=None):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class UserStoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(**{"owner": self.request.user})

    @action(detail=True, methods=['post'])
    def mark_as_active(self, request, pk=None):
        store = self.get_object()
        if store.status == 'deactivated':
            store.status = 'active'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def mark_as_deactivated(self, request, pk=None):
        store = self.get_object()
        if store.status == 'active':
            store.status = 'deactivated'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)


class AdminStoreViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['name']

    @action(detail=True, methods=['post'])
    def mark_as_active(self, request, pk=None):
        store = self.get_object()
        if store.status == 'in_review':
            store.status = 'active'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)

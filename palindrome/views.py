from rest_framework import viewsets,status
from .models import User, Game
from .serializers import UserSerializer, GameSerializer
from django.contrib.auth.models import User
import random
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def create(self, request, *args, **kwargs):
        user = self.request.user 
        game_id = f'game_{random.randint(10000, 99999)}'  # Generate a random game ID

        # Create a new game for the user
        game = Game.objects.create(user=user, game_id=game_id)
        serializer = self.get_serializer(game)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def getBoard(self, request, *args, **kwargs):
        game = self.get_object()
        serializer = self.get_serializer(game)

        return Response({'board': serializer.data['string_value']})

    def updateBoard(self, request, *args, **kwargs):
        game = self.get_object()

        # Check if the length of the string is less than 6
        if len(game.string_value) < 6:
            # Append a random character between 'a' and 'z'
            new_char = chr(random.randint(ord('a'), ord('z')))
            game.string_value += new_char
            game.random_number = random.randint(100, 999)
            game.save()

            # Check if the length is now 6 and whether the string is a palindrome
            if len(game.string_value) == 6 and game.string_value == game.string_value[::-1]:
                return Response({'message': 'Palindrome!'}, status=status.HTTP_200_OK)

            return Response({'message': 'Character added successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Game completed, string length is already 6.'}, status=status.HTTP_400_BAD_REQUEST)
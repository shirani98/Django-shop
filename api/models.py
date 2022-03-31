from rest_framework.response import Response
from rest_framework import status


from accounts.models import User


def create_user_api(serializer):
    if serializer.is_valid():
        user = User.objects.create_user(
            serializer.data.get('username'), serializer.data.get('email'), serializer.data.get('phone'))
        user.set_password(serializer.data.get('password'))
        user.save()
        return Response({"message": "User create successfully"}, status=status.HTTP_200_OK)
    return Response({"serializer": "no valid data"}, status=status.HTTP_400_BAD_REQUEST)

def update_password_api(object,serializer):
    if serializer.is_valid():
        if not object.check_password(serializer.data.get('old_password')):
                return Response({"password": "wrong"}, status=status.HTTP_400_BAD_REQUEST)
        object.set_password(serializer.data.get('new_password'))
        object.save()
        return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
    return Response({"serializer": "no valid data"}, status=status.HTTP_400_BAD_REQUEST)

    
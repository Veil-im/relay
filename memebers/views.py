from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AddMemberView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"message": "Member added"})


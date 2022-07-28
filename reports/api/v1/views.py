from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from reports.models import ReportRefill
from .serializers import ReportRefillIngredientSerializer
from accounts.models import User
from machines.models import Unit
from lookups.models import Ingredients, Cup
from django.db.models import Q
# Create your views here.


class ReportRefillIngredientView(APIView):

    @permission_classes((AllowAny,))
    def post(self, request, filter):
        lang = request.headers["lang"]
        response_data = {
            "state": True,
            "message": "Ok",
            "data": {}
        }
        report = []
        if filter == "all":
            report = ReportRefill.objects.all()
        elif filter =="tech":
            name = request.data.get("name")
            user = User.objects.all()
            for term in name.split():
                user = user.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
            for u in user:
                report_query = ReportRefill.objects.filter(user=u.pk)
                for r in report_query:
                    report.append(r)
        elif filter == "date":
            date = request.data.get("date")
            year, month, day = date.split("-")
            report = ReportRefill.objects.filter(time__year=year, time__month=month, time__day=day)

        serializer = ReportRefillIngredientSerializer(instance=report, many=True)
        response_data["data"] = serializer.data
        for r in response_data["data"]:
            user = User.objects.get(pk=r["user"])
            r["user"] = user.first_name + " " + user.last_name
            if lang == "ar":
                r["unit"] = Unit.objects.get(pk=r["unit"]).ar_name
                r["ingredient"] = Ingredients.objects.get(pk=r["ingredient"]).ar_name
            elif lang == "en":
                r["unit"] = Unit.objects.get(pk=r["unit"]).en_name
                r["ingredient"] = Ingredients.objects.get(pk=r["ingredient"]).en_name

        return Response(data=response_data, status=status.HTTP_200_OK)

from django.shortcuts import render
from .tasks import My_Work
from rest_framework.views import APIView
from rest_framework.response import Response


class ScheduleAPI(APIView):

    def post(self, request):

        data = request.data

        print("excecute")

        My_Work.delay()

        return Response(data={"msg":"Ok"})
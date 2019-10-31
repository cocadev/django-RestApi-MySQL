from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from management.models import Project
from management.serializers import ProjectSerializer
from .forms import ProjectChangeForm

########################################
############ Project View ##############
########################################
@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    projects_serializer = ProjectSerializer(projects, many=True)
    return JsonResponse(projects_serializer.data, safe=False)


@api_view(['POST'])
def create_project(request):
    project_data = JSONParser().parse(request)
    project_serializer = ProjectSerializer(data=project_data)
    if project_serializer.is_valid():
         project_serializer.save()
         return JsonResponse(project_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profile_project(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    project_serializer = ProjectSerializer(project)
    return JsonResponse(project_serializer.data)


@api_view(['PUT'])
def update_project(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    form = ProjectChangeForm(request.data or None, instance=project)

    if form.is_valid():
        form.save()
        return JsonResponse(form.data)
    return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)


    # request_data = JSONParser().parse(request)
    # project_serializer = ProjectSerializer(project, data=request_data)
    # if project_serializer.is_valid():
    #     project_serializer.save()
    #     return JsonResponse(project_serializer.data)
    # return JsonResponse(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_project(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    project.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)
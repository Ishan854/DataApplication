from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import File, Person
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as opy
import numpy as np  

def home(request):
    return render(request, 'home.html')

def create_db(file_path, data_name):
    df = pd.read_csv(file_path, delimiter=',')
    for index, row in df.iterrows():
        person = Person(column1=row['column1'], column2=row['column2'])
        person.save()

def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        data_name = request.POST.get('dataName', '')
        obj = File.objects.create(file=file, data_name=data_name)
        create_db(obj.file.path, data_name)
        return JsonResponse({'data_name': data_name})  
    return render(request, 'upload_data.html') 

def fetch_data(request):
    csv_files = File.objects.filter(file__icontains='.csv').exclude(data_name='')
    return render(request, 'fetch_data.html', {'csv_files': csv_files})

def compute_data(request):
    if request.method == 'POST':
        data_name = request.POST['data_name']
        column_name = request.POST['column_name']
        operation = request.POST['operation']
        try:
            data_object = File.objects.get(data_name=data_name)
            df = pd.read_csv(data_object.file.path)
            result = None

            if operation == 'min':
                result = df[column_name].min()
            elif operation == 'max':
                result = df[column_name].max()
            elif operation == 'sum':
                result = df[column_name].sum()

            return JsonResponse({'result': result.item()})  
        except File.DoesNotExist:
            return JsonResponse({'error': 'Data not found.'})

    return render(request, 'compute_data.html')    

def plot(request):
    if request.method == 'GET':
        data_name = request.GET.get('data_name', '')
        column1 = request.GET.get('column1', '')
        column2 = request.GET.get('column2', '')

        if not data_name or not column1 or not column2:
            return JsonResponse({'error': 'Invalid parameters.'})

        try:
            data_object = File.objects.get(data_name=data_name)
            df = pd.read_csv(data_object.file.path)

            
            if column1 not in df.columns or column2 not in df.columns:
                return JsonResponse({'error': 'Invalid columns provided.'})

            data_to_plot = df.head(30)

            
            x_data = data_to_plot[column1].values.tolist()
            y_data = data_to_plot[column2].values.tolist()

            
            trace = go.Scatter(x=x_data, y=y_data, mode='markers', type='scatter')
            layout = go.Layout(title=f'Scatter Plot of {column1} against {column2}', xaxis={'title': column1}, yaxis={'title': column2})
            fig = go.Figure(data=[trace], layout=layout)

            graph = opy.plot(fig, auto_open=False, output_type='div')

            return render(request, 'plot.html', {'graph': graph, 'column1': column1, 'column2': column2})
        except File.DoesNotExist:
            return JsonResponse({'error': 'Data not found.'})
    return render(request, 'plot.html')

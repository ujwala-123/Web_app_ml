from django.shortcuts import render
from .models import Iris

# Create an instance of the LogisticRegression model

def index(request):
    dataset = Iris.objects.all()
    return render(request, 'demoapp/index.html', {'dataset': dataset})


def predict(request):
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        # Create an instance of the Iris model with the provided data
        iris_instance = Iris(sepal_length=sepal_length, sepal_width=sepal_width,
                             petal_length=petal_length, petal_width=petal_width)

        # Perform prediction and save the instance
        prediction = iris_instance.predict_species()
        iris_instance.save()

        if prediction == 0:
            predicted_species = "Setosa"
        elif prediction == 1:
            predicted_species ="Versicolor"
        elif prediction == 2:
            predicted_species ="Virginica"

        context = {
            'predicted_species': predicted_species 
        }
        return render(request, 'demoapp/predict.html', context)
    else:
        return render(request, 'demoapp/predict.html')


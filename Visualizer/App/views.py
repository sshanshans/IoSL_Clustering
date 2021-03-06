import os, math, time

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.template import RequestContext

from time import strftime, gmtime

from .forms import *
from .models import Dataset
from .runners import StscRunner, OpticsRunner
from .noise import Noise

# Auxiliary function to delete old entries from the database
# Executed each time a page is requested
def deleteOldEntries() :
    until = int(time.time()) - 6*60*60 # 6h * 60m *60s
    Dataset.objects.filter(creationTime__lt = strftime('%Y-%m-%d %H:%M:%S', gmtime(until))).delete()

# Uploader view
def UploadDatasetView(request):
    if request.method == 'POST':
        form = UploadDatasetForm(request.POST, request.FILES)
        if form.is_valid() :
            ds = Dataset(data=request.FILES['file'].read())
            try :
                ds.full_clean()
            except ValidationError:
                return HttpResponseRedirect('/error')

            ds.save()
            request.session['ds'] = ds.id

            if form.cleaned_data['algorithm'] == 'STSC':
                return HttpResponseRedirect('/resultSTSC')
            elif form.cleaned_data['algorithm'] == 'OPTICSR' :
                return HttpResponseRedirect('/resultOPTICSR')
            elif form.cleaned_data['algorithm'] == 'OPTICSP' :
                return HttpResponseRedirect('/resultOPTICSP')
            elif form.cleaned_data['algorithm'] == 'OPTICSJ' :
                return HttpResponseRedirect('/resultOPTICSJ')
    else :
        # Trick to avoid None session_key at the first request
        request.session['noise'] = ''
        form = UploadDatasetForm()
    return render(request, 'UploadDatasetTemplate.html', {'form': form})

# Result View Optics - R
def ResultViewOPTICSR(request) :
    # You fool. Go back to the Uploader View. The ds is not set
    if request.session.get('ds', None) == None :
        return HttpResponseRedirect('/')

    # Get element
    dsId = request.session.get('ds')
    ds = Dataset.objects.get(id=dsId)

    if request.method == 'GET':
        # GET - First request prepare the form
        # Create Form
        form = ParametersOPTICSR(initial={'minPoints':15, 'eps':10, 'angle':120})
        # Set default parameters
        minPoints = 15
        eps = 10
        angleV = math.cos(math.radians(120))
    else :
        # POST - New calculation requested
        form = ParametersOPTICSR(request.POST)

        if form.is_valid() :
            minPoints = form.cleaned_data['minPoints']
            eps = form.cleaned_data['eps']
            angleV = math.cos(math.radians(form.cleaned_data['angle']))

            functions = form.cleaned_data['noiseFunctions']
            generateNoise = form.cleaned_data['generateNoise']

            if (functions != '' and generateNoise) :
                # Generate noise points
                noise = Noise(functions)
                noiseStr = noise.generatePoints()
                ds.noise = noiseStr
                ds.save()
            elif (functions == ''):
                ds.noise = ''
                ds.save()
        else :
            minPoints = 15
            eps = 10
            angleV = math.cos(math.radians(120))

    filePath = ds.writeFile() # Write dataset on disk
    optics = OpticsRunner(filePath, eps, minPoints, angle=angleV) # Execution of OPTICS
    output = optics.run('r')
    os.remove(filePath) # Delete File

    # Put the form in the output to display it
    output['form'] = form

    # Get the points from the db to be displayed
    output['points'] = ds.getPoints()

    deleteOldEntries()
    return render(request, 'ResultTemplateOPTICS.html', output)

# Result View Optics - Java
def ResultViewOPTICSJ(request) :
    # You fool. Go back to the Uploader View. The ds is not set
    if request.session.get('ds', None) == None :
        return HttpResponseRedirect('/')

    # Get element
    dsId = request.session.get('ds')
    ds = Dataset.objects.get(id=dsId)

    if request.method == 'GET':
        # GET - First request prepare the form
        # Create Form
        form = ParametersOPTICSJ(initial={'minPoints':15, 'eps':10, 'xi':0.1})
        # Set default parameters
        minPoints = 15
        eps = 10
        xiV = 0.1
    else :
        # POST - New calculation requested
        form = ParametersOPTICSJ(request.POST)

        if form.is_valid() :
            minPoints = form.cleaned_data['minPoints']
            eps = form.cleaned_data['eps']
            xiV = form.cleaned_data['xi']

            functions = form.cleaned_data['noiseFunctions']
            generateNoise = form.cleaned_data['generateNoise']

            if (functions != '' and generateNoise) :
                # Generate noise points
                noise = Noise(functions)
                noiseStr = noise.generatePoints()
                ds.noise = noiseStr
                ds.save()
            elif (functions == ''):
                ds.noise = ''
                ds.save()
        else :
            minPoints = 15
            eps = 10
            xiV = 0.1

    filePath = ds.writeFile() # Write dataset on disk
    optics = OpticsRunner(filePath, eps, minPoints, xi=xiV) # Execution of OPTICS
    output = optics.run('java')
    os.remove(filePath) # Delete File

    # Put the form in the output to display it
    output['form'] = form

    # Get the points from the db to be displayed
    output['points'] = ds.getPoints()

    deleteOldEntries()
    return render(request, 'ResultTemplateOPTICS.html', output)


# Result View Optics Python
def ResultViewOPTICSP(request) :
    # You fool. Go back to the Uploader View. The ds is not set
    if request.session.get('ds', None) == None :
        return HttpResponseRedirect('/')

    # Get element
    dsId = request.session.get('ds')
    ds = Dataset.objects.get(id=dsId)

    if request.method == 'GET':
        # GET - First request prepare the form
        # Create Form
        form = ParametersOPTICSP(initial={'minPoints':10, 'eps':0.5, 'threshold':75})
        # Set default parameters
        minPoints = 10
        eps = 0.5
        threshold = 0.75
    else :
        # POST - New calculation requested
        form = ParametersOPTICSP(request.POST)

        if form.is_valid() :
            minPoints = form.cleaned_data['minPoints']
            eps = form.cleaned_data['eps']
            threshold = float(form.cleaned_data['threshold']) / 100

            functions = form.cleaned_data['noiseFunctions']
            generateNoise = form.cleaned_data['generateNoise']

            if (functions != '' and generateNoise) :
                # Generate noise points
                noise = Noise(functions)
                noiseStr = noise.generatePoints()
                ds.noise = noiseStr
                ds.save()
            elif (functions == ''):
                ds.noise = ''
                ds.save()
        else :
            minPoints = 10
            eps = 0.5
            threshold = 0.75

    filePath = ds.writeFile() # Write dataset on disk
    optics = OpticsRunner(filePath, eps, minPoints, thres = threshold) # Execution of OPTICS
    output = optics.run('python')
    os.remove(filePath) # Delete File

    # Put the form in the output to display it
    output['form'] = form

    # Get the points from the db to be displayed
    output['points'] = ds.getPoints()

    deleteOldEntries()
    return render(request, 'ResultTemplateOPTICS.html', output)

# Result View STSC
def ResultViewSTSC(request) :
    # You fool. Go back to the Uploader View. The ds is not set
    if request.session.get('ds', None) == None :
        return HttpResponseRedirect('/')

    # Get element
    dsId = request.session.get('ds')
    ds = Dataset.objects.get(id=dsId)

    if request.method == 'GET':
        # GET - First request prepare the form
        # Create Form
        form = ParametersSTSC(initial={'numClusters':10, 'k':7, 'simCut':5, 'stop':0.001})
        # Set default parameters
        numClusters = 10
        k = 6
        simCut = 5
        stop = 0.001
    else :
        # POST - New calculation requested
        form = ParametersSTSC(request.POST)
        if form.is_valid() :
            numClusters = form.cleaned_data['numClusters']
            k = form.cleaned_data['k'] - 1
            simCut = form.cleaned_data['simCut']
            stop = form.cleaned_data['stop']

            functions = form.cleaned_data['noiseFunctions']
            generateNoise = form.cleaned_data['generateNoise']

            if (functions != '' and generateNoise) :
                # Generate noise points
                noise = Noise(functions)
                noiseStr = noise.generatePoints()
                ds.noise = noiseStr
                ds.save()
            elif (functions == ''):
                ds.noise = ''
                ds.save()
        else :
            numClusters = 10
            k = 6
            simCut = 5
            stop = 0.001

    print "Stop" + str(stop)
    filePath = ds.writeFile() # Write dataset on disk
    stsc = StscRunner(filePath, numClusters, k, simCut, stop) # Execution of STSC
    output = stsc.run()
    os.remove(filePath) # Delete File

    # Put the form in the output to display it
    output['form'] = form

    # Get the points from the db to be displayed
    output['points'] = ds.getPoints()

    deleteOldEntries()
    return render(request, 'ResultTemplateSTSC.html', output)


# Show the error page
def ErrorView(request) :
    return render(request, 'ErrorPage.html', {'error': 'Not supported dataset'})

def HomepageRedirect(request):
    return HttpResponseRedirect('/')

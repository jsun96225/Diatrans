from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .inference import run_s2st, run_s2tt, run_t2st, run_t2tt, run_asr

@api_view(['POST'])
def s2st(request):
    input_audio = request.data['input_audio']
    source_language = request.data['source_language']
    target_language = request.data['target_language']
    sample_rate, output_audio, output_text = run_s2st(input_audio, source_language, target_language)
    return Response({'sample_rate': sample_rate, 'output_audio': output_audio.tolist(), 'output_text': output_text})

@api_view(['POST'])
def s2tt(request):
    input_audio = request.data['input_audio']
    source_language = request.data['source_language']
    target_language = request.data['target_language']
    output_text = run_s2tt(input_audio, source_language, target_language)
    return Response({'output_text': output_text})

@api_view(['POST'])
def t2st(request):
    input_text = request.data['input_text']
    source_language = request.data['source_language']
    target_language = request.data['target_language']
    sample_rate, output_audio, output_text = run_t2st(input_text, source_language, target_language)
    return Response({'sample_rate': sample_rate, 'output_audio': output_audio.tolist(), 'output_text': output_text})

@api_view(['POST'])
def t2tt(request):
    input_text = request.data['input_text']
    source_language = request.data['source_language']
    target_language = request.data['target_language']
    output_text = run_t2tt(input_text, source_language, target_language)
    return Response({'output_text': output_text})

@api_view(['POST'])
def asr(request):
    input_audio = request.data['input_audio']
    target_language = request.data['target_language']
    output_text = run_asr(input_audio, target_language)
    return Response({'output_text': output_text})
